"""Cross-day dedup: track and check stories previously featured in the digest.

Each featured pick is appended to `state/featured.jsonl` after a run. On the
next run, candidate clusters are classified against entries from the last N days:

  - same:        strong match, no new sources -> drop from consideration
  - developing:  strong match BUT new sources/events present -> keep, tag headline
  - different:   no meaningful match -> normal

CLI usage (called from the Routine prompt):
  uv run python -m src.featured load [DAYS]    # print recent entries as JSON
  uv run python -m src.featured classify       # stdin: cluster JSON; out: classification
  uv run python -m src.featured append         # stdin: JSON array of picks; appends to log
"""
from __future__ import annotations

import json
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from rapidfuzz import fuzz

ROOT = Path(__file__).resolve().parent.parent
FEATURED_PATH = ROOT / "state" / "featured.jsonl"

# Tunables for classification thresholds.
STRONG_MATCH_SCORE = 70
WEAK_MATCH_FLOOR = 40


def load_recent(days: int = 7, path: Path = FEATURED_PATH) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    rows: list[dict[str, Any]] = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get("date", "0000-00-00") >= cutoff:
            rows.append(rec)
    return rows


def _match_score(cluster: dict, entry: dict) -> int:
    cves = set(cluster.get("cves", []))
    vendors = {v.lower() for v in cluster.get("vendors", [])}
    title = (cluster.get("title", "") or "").lower()
    e_cves = set(entry.get("cves", []))
    e_vendors = {v.lower() for v in entry.get("vendors", [])}
    e_title = (entry.get("title", "") or "").lower()

    score = 0
    if cves & e_cves:
        score += 50
    score += 20 * min(len(vendors & e_vendors), 2)
    if title and e_title:
        score += int(fuzz.token_set_ratio(title, e_title) * 0.3)
    return score


def classify(cluster: dict[str, Any], recent: list[dict[str, Any]]) -> dict[str, Any]:
    """Return {'status': 'same'|'developing'|'different', 'match': entry|None, 'reason': str}."""
    sources = set(cluster.get("source_families", []))

    best: dict[str, Any] | None = None
    best_score = 0
    for entry in recent:
        s = _match_score(cluster, entry)
        if s > best_score:
            best_score = s
            best = entry

    if best is None or best_score < WEAK_MATCH_FLOOR:
        return {"status": "different", "match": None, "reason": "no recent match"}

    e_sources = set(best.get("source_families", []))
    new_sources = sources - e_sources

    if best_score >= STRONG_MATCH_SCORE:
        if new_sources:
            return {
                "status": "developing",
                "match": best,
                "reason": (
                    f"strong match to '{best.get('title')}' from {best.get('date')}; "
                    f"new source families since: {sorted(new_sources)}"
                ),
            }
        return {
            "status": "same",
            "match": best,
            "reason": f"strong match to '{best.get('title')}' from {best.get('date')}; suppress",
        }

    # Mid-confidence match (between WEAK_MATCH_FLOOR and STRONG_MATCH_SCORE) — treat as
    # developing so we keep coverage but flag it for Claude to handle in the summary.
    return {
        "status": "developing",
        "match": best,
        "reason": f"partial match (score={best_score}) with '{best.get('title')}' from {best.get('date')}",
    }


def append(picks: list[dict[str, Any]], run_date: date | None = None, path: Path = FEATURED_PATH) -> None:
    d = (run_date or date.today()).isoformat()
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f:
        for i, p in enumerate(picks):
            rec = {
                "date": d,
                "rank": p.get("rank", i + 1),
                "title": p.get("title", ""),
                "cves": sorted(p.get("cves", []) or []),
                "vendors": sorted(p.get("vendors", []) or []),
                "representative_url": p.get("representative_url", ""),
                "score": float(p.get("score", 0.0)),
                "source_families": sorted(p.get("source_families", []) or []),
                "status": p.get("status", "fresh"),
            }
            f.write(json.dumps(rec, sort_keys=True) + "\n")


def _cli() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "load"
    if cmd == "load":
        days = int(sys.argv[2]) if len(sys.argv) > 2 else 7
        print(json.dumps(load_recent(days), indent=2))
        return 0
    if cmd == "classify":
        payload = json.loads(sys.stdin.read())
        if isinstance(payload, dict) and "cluster" in payload:
            cluster = payload["cluster"]
            recent = payload.get("recent") or load_recent(7)
        else:
            cluster = payload
            recent = load_recent(7)
        print(json.dumps(classify(cluster, recent), indent=2))
        return 0
    if cmd == "append":
        picks = json.loads(sys.stdin.read())
        if not isinstance(picks, list):
            print("error: stdin must be a JSON array of picks", file=sys.stderr)
            return 2
        append(picks)
        print(f"appended {len(picks)} picks to {FEATURED_PATH}", file=sys.stderr)
        return 0
    print(f"unknown command: {cmd}", file=sys.stderr)
    print("usage: load [DAYS] | classify (stdin) | append (stdin)", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(_cli())
