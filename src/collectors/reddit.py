from __future__ import annotations

import asyncio
import logging
import os
from datetime import datetime, timedelta, timezone

from src.normalize import Item

log = logging.getLogger(__name__)


def _fetch_sync(config: dict) -> list[Item]:
    import praw  # imported lazily so missing creds don't break imports

    reddit_cfg = config.get("reddit", {})
    lookback_hours = config.get("lookback_hours", 24)
    vendors = config.get("vendors", [])
    subs = reddit_cfg.get("subreddits", [])
    limit = int(reddit_cfg.get("limit_per_sub", 50))
    min_score = int(reddit_cfg.get("min_score", 10))
    since = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)

    user_agent = os.environ.get(
        "REDDIT_USER_AGENT",
        f"security-summary/0.1 by u/{os.environ.get('REDDIT_USERNAME', 'unknown')}",
    )
    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        username=os.environ["REDDIT_USERNAME"],
        password=os.environ["REDDIT_PASSWORD"],
        user_agent=user_agent,
    )

    items: list[Item] = []
    for sub_name in subs:
        try:
            sub = reddit.subreddit(sub_name)
            for post in sub.new(limit=limit):
                ts = datetime.fromtimestamp(post.created_utc, tz=timezone.utc)
                if ts < since:
                    continue
                if post.score < min_score:
                    continue
                title = (post.title or "").strip()
                body = (post.selftext or "")[:2000]
                items.append(
                    Item(
                        source=f"reddit:r/{sub_name}",
                        source_family="reddit",
                        url=f"https://reddit.com{post.permalink}",
                        title=title,
                        body=body,
                        author=str(post.author) if post.author else None,
                        timestamp=ts,
                        engagement=float(post.score + post.num_comments * 0.5),
                        vendors=[v for v in vendors if v.lower() in (title + " " + body).lower()],
                        raw={
                            "score": post.score,
                            "num_comments": post.num_comments,
                            "subreddit": sub_name,
                            "external_url": post.url if not post.is_self else None,
                        },
                    )
                )
        except Exception as e:
            log.warning("reddit.sub_fail subreddit=%s error=%s", sub_name, e)
            continue
    return items


async def collect(config: dict) -> list[Item]:
    required = ["REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "REDDIT_USERNAME", "REDDIT_PASSWORD"]
    if any(not os.environ.get(k) for k in required):
        log.info("reddit.skip reason=missing_credentials")
        return []
    return await asyncio.to_thread(_fetch_sync, config)


if __name__ == "__main__":
    import json
    from pathlib import Path

    import yaml

    cfg = yaml.safe_load(Path("config/sources.yaml").read_text())
    items = asyncio.run(collect(cfg))
    print(json.dumps([i.to_dict() for i in items[:5]], indent=2, default=str))
    print(f"\nTotal: {len(items)}")
