from __future__ import annotations

import json
import logging
from collections.abc import Iterable
from datetime import datetime, timedelta, timezone
from pathlib import Path

from src.normalize import Item

log = logging.getLogger(__name__)

DEFAULT_HORIZON_DAYS = 14


def load_seen(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    seen: dict[str, dict] = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        key = rec.get("url_hash") or rec.get("content_hash")
        if key:
            seen[key] = rec
    return seen


def save_seen(path: Path, seen: dict[str, dict], horizon_days: int = DEFAULT_HORIZON_DAYS) -> None:
    cutoff = datetime.now(timezone.utc) - timedelta(days=horizon_days)
    path.parent.mkdir(parents=True, exist_ok=True)
    out_lines: list[str] = []
    for rec in seen.values():
        try:
            last = datetime.fromisoformat(rec.get("last_seen", ""))
        except ValueError:
            continue
        if last >= cutoff:
            out_lines.append(json.dumps(rec, sort_keys=True))
    out_lines.sort()
    path.write_text("\n".join(out_lines) + ("\n" if out_lines else ""))


def filter_new(items: Iterable[Item], seen: dict[str, dict]) -> tuple[list[Item], list[Item]]:
    """Returns (new_items, repeat_items). Updates `seen` in place."""
    now_iso = datetime.now(timezone.utc).isoformat()
    new_items: list[Item] = []
    repeat_items: list[Item] = []
    for it in items:
        key = it.url_hash
        if key in seen:
            seen[key]["last_seen"] = now_iso
            seen[key]["count"] = int(seen[key].get("count", 1)) + 1
            repeat_items.append(it)
        else:
            seen[key] = {
                "url_hash": key,
                "content_hash": it.content_hash,
                "url": it.url,
                "title": it.title[:200],
                "source_family": it.source_family,
                "cves": it.cves,
                "first_seen": now_iso,
                "last_seen": now_iso,
                "count": 1,
            }
            new_items.append(it)
    return new_items, repeat_items
