"""YouTube collector: fetches recent videos from configured channels and
enriches each with its auto-generated transcript for body text.

Requires www.youtube.com in the network allowlist.
"""
from __future__ import annotations

import asyncio
import logging
from datetime import datetime, timedelta, timezone

import feedparser
import httpx

from src.normalize import Item

log = logging.getLogger(__name__)

_TRANSCRIPT_CHARS = 1500
_TRANSCRIPT_TIMEOUT = 10.0


def _sync_get_transcript(video_id: str) -> str:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled

    try:
        chunks = YouTubeTranscriptApi.get_transcript(
            video_id, languages=["en", "en-US", "en-GB"]
        )
        return " ".join(c["text"] for c in chunks)[:_TRANSCRIPT_CHARS]
    except (TranscriptsDisabled, NoTranscriptFound):
        return ""
    except Exception as e:
        log.debug("youtube.transcript_fail video_id=%s error=%r", video_id, e)
        return ""


async def _fetch_transcript(video_id: str) -> str:
    try:
        return await asyncio.wait_for(
            asyncio.to_thread(_sync_get_transcript, video_id),
            timeout=_TRANSCRIPT_TIMEOUT,
        )
    except asyncio.TimeoutError:
        log.debug("youtube.transcript_timeout video_id=%s", video_id)
        return ""


def _entry_timestamp(entry) -> datetime:
    for key in ("published_parsed", "updated_parsed"):
        t = getattr(entry, key, None)
        if t:
            return datetime(*t[:6], tzinfo=timezone.utc)
    return datetime.now(timezone.utc)


def _video_id(entry) -> str | None:
    vid = getattr(entry, "yt_videoid", None)
    if vid:
        return vid
    link = entry.get("link", "")
    if "v=" in link:
        return link.split("v=")[-1].split("&")[0]
    return None


async def _noop() -> str:
    return ""


async def _fetch_channel(
    client: httpx.AsyncClient,
    channel: dict,
    since: datetime,
    vendors: list[str],
) -> list[Item]:
    channel_id = channel["channel_id"]
    name = channel.get("name", channel_id)
    rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    try:
        r = await client.get(rss_url, timeout=15.0)
        r.raise_for_status()
    except Exception as e:
        log.warning("youtube.feed_fail name=%s error=%s", name, e)
        return []

    parsed = feedparser.parse(r.content)
    recent = [e for e in parsed.entries if _entry_timestamp(e) >= since]
    if not recent:
        return []

    vids = [_video_id(e) for e in recent]
    transcripts = await asyncio.gather(*[
        _fetch_transcript(vid) if vid else _noop()
        for vid in vids
    ])

    items: list[Item] = []
    for entry, vid, body in zip(recent, vids, transcripts):
        ts = _entry_timestamp(entry)
        url = entry.get("link") or (f"https://www.youtube.com/watch?v={vid}" if vid else "")
        if not url:
            continue
        title = (entry.get("title") or "").strip()
        combined = f"{title} {body}"
        items.append(
            Item(
                source=name,
                source_family="youtube",
                url=url,
                title=title,
                body=body,
                author=name,
                timestamp=ts,
                engagement=0.0,
                vendors=[v for v in vendors if v.lower() in combined.lower()],
                raw={"channel_id": channel_id},
            )
        )
    log.info("youtube.channel_ok name=%s new=%d", name, len(items))
    return items


async def collect(config: dict) -> list[Item]:
    channels = config.get("youtube_channels", [])
    if not channels:
        return []
    lookback_hours = config.get("lookback_hours", 24)
    vendors = config.get("vendors", [])
    since = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)

    headers = {
        "User-Agent": "security-summary/0.1 (+https://github.com/pnikolaidis/security-summary)",
        "Accept": "application/atom+xml, application/rss+xml, */*;q=0.8",
    }
    async with httpx.AsyncClient(headers=headers, follow_redirects=True) as client:
        results = await asyncio.gather(
            *[_fetch_channel(client, ch, since, vendors) for ch in channels],
        )
    return [item for batch in results for item in batch]


if __name__ == "__main__":
    import json
    from pathlib import Path

    import yaml

    cfg = yaml.safe_load(Path("config/sources.yaml").read_text())
    items = asyncio.run(collect(cfg))
    print(json.dumps([i.to_dict() for i in items[:5]], indent=2, default=str))
    print(f"\nTotal: {len(items)}")
