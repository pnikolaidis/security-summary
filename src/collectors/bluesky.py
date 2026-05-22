from __future__ import annotations

import asyncio
import logging
from datetime import datetime, timedelta, timezone

import httpx

from src.normalize import Item

log = logging.getLogger(__name__)

# Unauthenticated AppView endpoint — no PDS login required for public search.
APPVIEW = "https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts"


async def _search(client: httpx.AsyncClient, query: str, since: datetime, limit: int, vendors: list[str]) -> list[Item]:
    params = {"q": query, "limit": min(limit, 100), "sort": "latest"}
    try:
        r = await client.get(APPVIEW, params=params, timeout=15.0)
        r.raise_for_status()
    except Exception as e:
        log.warning("bluesky.fetch_fail query=%s error=%s", query, e)
        return []

    items: list[Item] = []
    for post in r.json().get("posts", []):
        rec = post.get("record", {}) or {}
        text = (rec.get("text") or "").strip()
        if not text:
            continue
        created_at = rec.get("createdAt") or post.get("indexedAt")
        try:
            ts = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        except (AttributeError, ValueError):
            continue
        if ts < since:
            continue
        likes = post.get("likeCount", 0) or 0
        reposts = post.get("repostCount", 0) or 0
        replies = post.get("replyCount", 0) or 0
        engagement = float(likes + reposts * 2 + replies * 0.5)
        author = (post.get("author") or {}).get("handle")
        # Reconstruct a bsky.app URL from the AT-URI
        uri = post.get("uri", "")  # at://did:plc:.../app.bsky.feed.post/<rkey>
        url = ""
        if uri.startswith("at://") and author:
            rkey = uri.rsplit("/", 1)[-1]
            url = f"https://bsky.app/profile/{author}/post/{rkey}"
        items.append(
            Item(
                source=f"bluesky:{query}",
                source_family="bluesky",
                url=url or uri,
                title=text[:200],
                body=text[:2000],
                author=author,
                timestamp=ts,
                engagement=engagement,
                vendors=[v for v in vendors if v.lower() in text.lower()],
                raw={"query": query, "likes": likes, "reposts": reposts, "replies": replies},
            )
        )
    return items


async def collect(config: dict) -> list[Item]:
    bsky = config.get("bluesky", {})
    queries = bsky.get("queries", [])
    limit = int(bsky.get("limit_per_query", 50))
    lookback_hours = config.get("lookback_hours", 24)
    vendors = config.get("vendors", [])
    since = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)

    async with httpx.AsyncClient(headers={"User-Agent": "security-summary/0.1"}) as client:
        results = await asyncio.gather(
            *[_search(client, q, since, limit, vendors) for q in queries]
        )
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
