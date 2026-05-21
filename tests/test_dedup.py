from datetime import datetime, timedelta, timezone
from pathlib import Path

from src.dedup import filter_new, load_seen, save_seen
from src.normalize import Item


def _item(url: str, title: str = "t") -> Item:
    return Item(source="x", source_family="news", url=url, title=title, body="body")


def test_filter_new_marks_first_seen(tmp_path: Path):
    path = tmp_path / "seen.jsonl"
    seen = load_seen(path)
    new, repeats = filter_new([_item("https://a.example/1"), _item("https://b.example/2")], seen)
    assert len(new) == 2
    assert len(repeats) == 0
    save_seen(path, seen)
    assert path.exists()


def test_filter_new_detects_repeats(tmp_path: Path):
    path = tmp_path / "seen.jsonl"
    seen = load_seen(path)
    filter_new([_item("https://a.example/1")], seen)
    save_seen(path, seen)

    reloaded = load_seen(path)
    new, repeats = filter_new([_item("https://a.example/1"), _item("https://b.example/2")], reloaded)
    assert {it.url for it in new} == {"https://b.example/2"}
    assert {it.url for it in repeats} == {"https://a.example/1"}


def test_save_seen_expires_old_records(tmp_path: Path):
    path = tmp_path / "seen.jsonl"
    seen = {
        "old": {
            "url_hash": "old",
            "url": "https://a.example/old",
            "title": "old",
            "source_family": "news",
            "cves": [],
            "first_seen": (datetime.now(timezone.utc) - timedelta(days=30)).isoformat(),
            "last_seen": (datetime.now(timezone.utc) - timedelta(days=30)).isoformat(),
            "count": 1,
        },
        "new": {
            "url_hash": "new",
            "url": "https://a.example/new",
            "title": "new",
            "source_family": "news",
            "cves": [],
            "first_seen": datetime.now(timezone.utc).isoformat(),
            "last_seen": datetime.now(timezone.utc).isoformat(),
            "count": 1,
        },
    }
    save_seen(path, seen, horizon_days=14)
    reloaded = load_seen(path)
    assert "new" in reloaded
    assert "old" not in reloaded
