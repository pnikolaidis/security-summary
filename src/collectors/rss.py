from __future__ import annotations

import asyncio
import logging
from datetime import datetime, timedelta, timezone

import feedparser
import httpx

from src.normalize import Item

log = logging.getLogger(__name__)


def _entry_timestamp(entry) -> datetime:
    for key in ("published_parsed", "updated_parsed"):
        t = getattr(entry, key, None) or entry.get(key) if isinstance(entry, dict) else getattr(entry, key, None)
        if t:
            return datetime(*t[:6], tzinfo=timezone.utc)
    return datetime.now(timezone.utc)


async def _fetch_one(client: httpx.AsyncClient, feed: dict, since: datetime, vendors: list[str]) -> list[Item]:
    try:
        r = await client.get(feed["url"], timeout=15.0, follow_redirects=True)
        r.raise_for_status()
    except Exception as e:
        log.warning("rss.fetch_fail name=%s error=%s", feed["name"], e)
        return []

    parsed = feedparser.parse(r.content)
    items: list[Item] = []
    for entry in parsed.entries:
        ts = _entry_timestamp(entry)
        if ts < since:
            continue
        url = entry.get("link") or ""
        if not url:
            continue
        title = (entry.get("title") or "").strip()
        body = (entry.get("summary") or entry.get("description") or "")[:2000]
        author = entry.get("author")
        items.append(
            Item(
                source=feed["name"],
                source_family="news",
                url=url,
                title=title,
                body=body,
                author=author,
                timestamp=ts,
                engagement=0.0,
                vendors=[v for v in vendors if v.lower() in (title + " " + body).lower()],
                raw={"feed": feed["name"]},
            )
        )
    return items


async def collect(config: dict) -> list[Item]:
    feeds = config.get("rss", [])
    lookback_hours = config.get("lookback_hours", 24)
    vendors = config.get("vendors", [])
    since = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)

    headers = {
        "User-Agent": "security-summary/0.1 (+https://github.com/pnikolaidis/security-summary)",
        "Accept": "application/atom+xml, application/rss+xml, application/xml;q=0.9, */*;q=0.8",
    }
    async with httpx.AsyncClient(headers=headers) as client:
        results = await asyncio.gather(
            *[_fetch_one(client, f, since, vendors) for f in feeds],
            return_exceptions=False,
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
