from __future__ import annotations

import asyncio
import logging
from datetime import datetime, timedelta, timezone

import httpx

from src.normalize import Item

log = logging.getLogger(__name__)


def _strip_html(s: str) -> str:
    import re
    return re.sub(r"<[^>]+>", " ", s or "").strip()


async def _fetch_tag(client: httpx.AsyncClient, instance: str, tag: str, since: datetime, limit: int, vendors: list[str]) -> list[Item]:
    url = f"https://{instance}/api/v1/timelines/tag/{tag}"
    params = {"limit": min(limit, 40)}
    try:
        r = await client.get(url, params=params, timeout=15.0)
        r.raise_for_status()
    except Exception as e:
        log.warning("mastodon.fetch_fail tag=%s error=%s", tag, e)
        return []

    items: list[Item] = []
    for status in r.json():
        try:
            ts = datetime.fromisoformat(status["created_at"].replace("Z", "+00:00"))
        except (KeyError, ValueError):
            continue
        if ts < since:
            continue
        content = _strip_html(status.get("content", ""))
        if not content.strip():
            continue
        boosts = status.get("reblogs_count", 0) or 0
        likes = status.get("favourites_count", 0) or 0
        replies = status.get("replies_count", 0) or 0
        engagement = float(boosts * 2 + likes + replies * 0.5)
        account = status.get("account", {}) or {}
        items.append(
            Item(
                source=f"mastodon:{instance}#{tag}",
                source_family="mastodon",
                url=status.get("url") or status.get("uri") or "",
                title=content[:200],
                body=content[:2000],
                author=account.get("acct"),
                timestamp=ts,
                engagement=engagement,
                vendors=[v for v in vendors if v.lower() in content.lower()],
                raw={"tag": tag, "boosts": boosts, "likes": likes, "replies": replies},
            )
        )
    return items


async def collect(config: dict) -> list[Item]:
    masto = config.get("mastodon", {})
    instance = masto.get("instance", "infosec.exchange")
    tags = masto.get("hashtags", [])
    limit = int(masto.get("limit_per_tag", 60))
    lookback_hours = config.get("lookback_hours", 24)
    vendors = config.get("vendors", [])
    since = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)

    async with httpx.AsyncClient(headers={"User-Agent": "security-summary/0.1"}) as client:
        results = await asyncio.gather(
            *[_fetch_tag(client, instance, t, since, limit, vendors) for t in tags]
        )
    # dedupe by URL within this collector
    seen: set[str] = set()
    out: list[Item] = []
    for batch in results:
        for it in batch:
            if it.url and it.url not in seen:
                seen.add(it.url)
                out.append(it)
    return out


if __name__ == "__main__":
    import json
    from pathlib import Path

    import yaml

    cfg = yaml.safe_load(Path("config/sources.yaml").read_text())
    items = asyncio.run(collect(cfg))
    print(json.dumps([i.to_dict() for i in items[:5]], indent=2, default=str))
    print(f"\nTotal: {len(items)}")
