from pathlib import Path

import pytest

from src.podcast_feed import _scan_runs, build_feed, show_notes


@pytest.fixture
def sample_run(tmp_path: Path) -> Path:
    runs = tmp_path / "runs"
    d = runs / "2026-05-22"
    d.mkdir(parents=True)
    (d / "summary.md").write_text(
        "# Security Digest — 2026-05-22\n"
        "*Today's brief by Allie.*\n\n"
        "## TL;DR\n"
        "Cisco patched a critical ASA RCE. Microsoft shipped emergency Outlook updates.\n"
        "Two ransomware operators leaked stolen data overnight.\n\n"
        "## 1. Cisco ASA RCE patched\n"
        "**Why it matters:** affects every internet-facing ASA.\n\n"
        "Cisco released CVE-2026-12345 patches today.\n"
    )
    # Minimal fake MP3 — header bytes recognized by mutagen; duration probe will fall back
    (d / "digest.mp3").write_bytes(b"ID3\x04\x00\x00\x00\x00\x00\x00" + b"\x00" * 1024)
    return runs


def test_scan_runs_finds_complete_runs(sample_run: Path):
    runs = _scan_runs(sample_run)
    assert len(runs) == 1
    assert runs[0]["date"] == "2026-05-22"


def test_scan_runs_skips_incomplete_dirs(tmp_path: Path):
    runs = tmp_path / "runs"
    (runs / "2026-05-22").mkdir(parents=True)  # no files at all
    (runs / "2026-05-23").mkdir(parents=True)
    (runs / "2026-05-23" / "summary.md").write_text("# x")  # missing mp3
    assert _scan_runs(runs) == []


def test_scan_runs_orders_newest_first(tmp_path: Path):
    runs = tmp_path / "runs"
    for d in ("2026-05-22", "2026-05-23", "2026-05-21"):
        run_dir = runs / d
        run_dir.mkdir(parents=True)
        (run_dir / "summary.md").write_text("# x")
        (run_dir / "digest.mp3").write_bytes(b"\x00" * 100)
    dates = [r["date"] for r in _scan_runs(runs)]
    assert dates == ["2026-05-23", "2026-05-22", "2026-05-21"]


def test_show_notes_extracts_tldr_plaintext():
    md = "# Title\n## TL;DR\nFirst sentence. Second sentence.\n\n## 1. Story\nDetail."
    html, plain = show_notes(md)
    assert "First sentence" in plain
    assert "Second sentence" in plain
    assert "Detail" not in plain  # stops at next H2


def test_show_notes_strips_h1_from_html():
    md = "# Episode title\n\nSome body."
    html, _ = show_notes(md)
    assert "Episode title" not in html
    assert "Some body" in html


def test_show_notes_falls_back_when_no_tldr():
    md = "# Title\n\nJust a body paragraph.\n"
    _, plain = show_notes(md)
    assert plain  # non-empty fallback


def test_build_feed_emits_valid_xml_structure(sample_run: Path):
    cfg = {
        "title": "Security Summary",
        "description": "Test feed",
        "category": "Technology",
        "language": "en-us",
        "github": {"owner": "pnikolaidis", "repo": "security-summary", "branch": "main"},
        "episodes_in_feed": 60,
    }
    feed = build_feed(cfg, runs_dir=sample_run)
    assert feed.startswith('<?xml version="1.0"')
    assert "<channel>" in feed and "</channel>" in feed
    assert "<item>" in feed and "</item>" in feed
    assert "security-summary-2026-05-22" in feed  # guid
    assert "raw.githubusercontent.com/pnikolaidis/security-summary/main" in feed
    assert "Cisco ASA RCE patched" in feed  # show notes
    # iTunes namespace declared and used
    assert 'xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"' in feed
    assert "<itunes:author>" in feed


def test_build_feed_handles_empty_runs(tmp_path: Path):
    cfg = {
        "title": "Security Summary",
        "description": "Empty",
        "category": "Technology",
        "language": "en-us",
        "github": {"owner": "pnikolaidis", "repo": "security-summary", "branch": "main"},
        "episodes_in_feed": 60,
    }
    feed = build_feed(cfg, runs_dir=tmp_path / "nonexistent")
    assert "<channel>" in feed
    assert "<item>" not in feed
