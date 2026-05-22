"""Fan-out collector entrypoint. Writes state/inbox.json with normalized items.

Usage: python -m src.collect
"""
from __future__ import annotations

import asyncio
import json
import logging
import sys
from pathlib import Path

import yaml

from src.collectors import run_collector
from src.collectors import bluesky, cisa, hackernews, mastodon, nvd, reddit, rss
from src.dedup import filter_new, load_seen, save_seen

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "sources.yaml"
INBOX_PATH = ROOT / "state" / "inbox.json"
SEEN_PATH = ROOT / "state" / "seen.jsonl"

COLLECTORS = {
    "rss": rss.collect,
    "hackernews": hackernews.collect,
    "cisa": cisa.collect,
    "nvd": nvd.collect,
    "reddit": reddit.collect,
    "mastodon": mastodon.collect,
    "bluesky": bluesky.collect,
}


async def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        stream=sys.stderr,
    )
    config = yaml.safe_load(CONFIG_PATH.read_text())

    tasks = [run_collector(name, fn, config) for name, fn in COLLECTORS.items()]
    results = await asyncio.gather(*tasks)
    all_items = [it for batch in results for it in batch]

    seen = load_seen(SEEN_PATH)
    new_items, repeat_items = filter_new(all_items, seen)
    save_seen(SEEN_PATH, seen)

    per_source: dict[str, int] = {}
    for it in all_items:
        per_source[it.source_family] = per_source.get(it.source_family, 0) + 1

    INBOX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INBOX_PATH.write_text(
        json.dumps(
            {
                "stats": {
                    "total_fetched": len(all_items),
                    "new": len(new_items),
                    "repeats": len(repeat_items),
                    "per_source_family": per_source,
                },
                "items": [it.to_dict() for it in new_items],
            },
            indent=2,
            default=str,
        )
    )
    print(
        f"collect.done total={len(all_items)} new={len(new_items)} "
        f"repeats={len(repeat_items)} per_family={per_source}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
