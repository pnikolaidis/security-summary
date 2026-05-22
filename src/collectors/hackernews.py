from __future__ import annotations

import asyncio
import logging
from datetime import datetime, timedelta, timezone

import httpx

from src.normalize import Item

log = logging.getLogger(__name__)

ALGOLIA = "https://hn.algolia.com/api/v1/search_by_date"


async def collect(config: dict) -> list[Item]:
    hn = config.get("hackernews", {})
    lookback_hours = config.get("lookback_hours", 24)
    vendors = config.get("vendors", [])
    min_score = hn.get("min_score", 50)
    keywords = hn.get("keywords", [])
    since = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
    since_ts = int(since.timestamp())

    items: list[Item] = []
    seen: set[str] = set()

    async with httpx.AsyncClient(headers={"User-Agent": "security-summary/0.1"}) as client:
        for kw in keywords:
            params = {
                "query": kw,
                "tags": hn.get("query_tags", "story"),
                "numericFilters": f"created_at_i>{since_ts},points>={min_score}",
                "hitsPerPage": 50,
            }
            try:
                r = await client.get(ALGOLIA, params=params, timeout=15.0)
                r.raise_for_status()
            except Exception as e:
                log.warning("hn.fetch_fail keyword=%s error=%s", kw, e)
                continue

            for hit in r.json().get("hits", []):
                obj_id = hit.get("objectID")
                if not obj_id or obj_id in seen:
                    continue
                seen.add(obj_id)
                url = hit.get("url") or f"https://news.ycombinator.com/item?id={obj_id}"
                title = (hit.get("title") or "").strip()
                if not title:
                    continue
                body = (hit.get("story_text") or "")[:2000]
                ts = datetime.fromtimestamp(hit.get("created_at_i", since_ts), tz=timezone.utc)
                points = hit.get("points") or 0
                comments = hit.get("num_comments") or 0
                items.append(
                    Item(
                        source="hackernews",
                        source_family="hn",
                        url=url,
                        title=title,
                        body=body,
                        author=hit.get("author"),
                        timestamp=ts,
                        engagement=float(points + comments * 0.5),
                        vendors=[v for v in vendors if v.lower() in title.lower()],
                        raw={"points": points, "num_comments": comments, "object_id": obj_id},
                    )
                )
    return items


if __name__ == "__main__":
    import json
    from pathlib import Path

    import yaml

    cfg = yaml.safe_load(Path("config/sources.yaml").read_text())
    items = asyncio.run(collect(cfg))
    print(json.dumps([i.to_dict() for i in items[:5]], indent=2, default=str))
    print(f"\nTotal: {len(items)}")
