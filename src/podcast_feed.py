"""Regenerate the podcast RSS feed from past run artifacts.

The feed lives at `docs/feed.xml` and is published via GitHub Pages
(Settings -> Pages -> source: main /docs). Episode MP3s are referenced
via raw.githubusercontent.com URLs pointing at `state/runs/<date>/digest.mp3`
so we don't duplicate the audio on disk.

CLI: `uv run python -m src.podcast_feed`
"""
from __future__ import annotations

import logging
import sys
from datetime import date as date_t
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from typing import Any
from xml.sax.saxutils import escape

import yaml
from markdown_it import MarkdownIt

from src import persona

ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = ROOT / "state" / "runs"
DOCS_DIR = ROOT / "docs"
CONFIG_PATH = ROOT / "config" / "podcast.yaml"

log = logging.getLogger(__name__)


def _load_config() -> dict[str, Any]:
    return yaml.safe_load(CONFIG_PATH.read_text())


def _raw_mp3_url(cfg: dict, date_str: str) -> str:
    gh = cfg["github"]
    return (
        f"https://raw.githubusercontent.com/{gh['owner']}/{gh['repo']}/"
        f"{gh['branch']}/state/runs/{date_str}/digest.mp3"
    )


def _pages_base_url(cfg: dict) -> str:
    gh = cfg["github"]
    return f"https://{gh['owner']}.github.io/{gh['repo']}/"


def _scan_runs(runs_dir: Path = RUNS_DIR, limit: int = 60) -> list[dict[str, Any]]:
    """Return run dirs with both summary.md and digest.mp3, most recent first."""
    out: list[dict[str, Any]] = []
    if not runs_dir.exists():
        return out
    for run_dir in sorted(runs_dir.iterdir(), reverse=True):
        if not run_dir.is_dir():
            continue
        try:
            d = date_t.fromisoformat(run_dir.name)
        except ValueError:
            continue
        summary = run_dir / "summary.md"
        mp3 = run_dir / "digest.mp3"
        if not summary.exists() or not mp3.exists():
            continue
        out.append({"date": run_dir.name, "date_obj": d, "summary": summary, "mp3": mp3})
        if len(out) >= limit:
            break
    return out


def _mp3_duration(mp3_path: Path) -> str:
    """HH:MM:SS for the audio. Falls back to a sensible guess on parse failure."""
    try:
        from mutagen.mp3 import MP3  # lazy import
        audio = MP3(mp3_path)
        secs = int(audio.info.length)
    except Exception as e:
        log.warning("mp3.duration_fail path=%s error=%s", mp3_path, e)
        return "00:05:00"
    h, rem = divmod(secs, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def _extract_title(summary_md: str, fallback: str) -> str:
    for line in summary_md.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def show_notes(summary_md: str) -> tuple[str, str]:
    """Return (html, plain_description). HTML strips the H1; plain pulls TL;DR if present."""
    lines = summary_md.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    body_md = "\n".join(lines).strip()
    html = MarkdownIt("commonmark", {"linkify": True}).render(body_md)

    plain_parts: list[str] = []
    in_tldr = False
    for line in body_md.splitlines():
        stripped = line.strip()
        if stripped.lower().startswith("## tl;dr") or stripped.lower().startswith("## tldr"):
            in_tldr = True
            continue
        if in_tldr and stripped.startswith("## "):
            break
        if in_tldr and stripped:
            plain_parts.append(stripped)
    plain = " ".join(plain_parts) or "Daily security digest — top 5 stories from news and social sources."
    return html, plain


def _render_item(cfg: dict, run: dict[str, Any]) -> str:
    date_str = run["date"]
    mp3_size = run["mp3"].stat().st_size
    duration = _mp3_duration(run["mp3"])
    summary_md = run["summary"].read_text()
    title = _extract_title(summary_md, f"Security Digest — {date_str}")
    html, plain = show_notes(summary_md)
    try:
        author = persona.for_date(run["date_obj"]).name
    except Exception:
        author = cfg.get("title", "Security Summary")

    pub_dt = datetime.fromisoformat(date_str + "T12:00:00+00:00")
    pub_str = format_datetime(pub_dt)
    enclosure_url = _raw_mp3_url(cfg, date_str)

    return (
        "    <item>\n"
        f"      <title>{escape(title)}</title>\n"
        f"      <description>{escape(plain)}</description>\n"
        f"      <content:encoded><![CDATA[{html}]]></content:encoded>\n"
        f"      <pubDate>{pub_str}</pubDate>\n"
        f'      <guid isPermaLink="false">security-summary-{date_str}</guid>\n'
        f'      <enclosure url="{escape(enclosure_url)}" length="{mp3_size}" type="audio/mpeg"/>\n'
        f"      <itunes:duration>{duration}</itunes:duration>\n"
        f"      <itunes:author>{escape(author)}</itunes:author>\n"
        "      <itunes:explicit>false</itunes:explicit>\n"
        "    </item>\n"
    )


def build_feed(cfg: dict | None = None, runs_dir: Path = RUNS_DIR) -> str:
    cfg = cfg or _load_config()
    limit = int(cfg.get("episodes_in_feed", 60))
    runs = _scan_runs(runs_dir, limit=limit)
    items = "".join(_render_item(cfg, r) for r in runs)
    pages_base = _pages_base_url(cfg)
    feed_url = pages_base + "feed.xml"
    now_rfc = format_datetime(datetime.now(timezone.utc))
    desc = cfg.get("description", "").strip()
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0"\n'
        '     xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"\n'
        '     xmlns:atom="http://www.w3.org/2005/Atom"\n'
        '     xmlns:content="http://purl.org/rss/1.0/modules/content/">\n'
        "  <channel>\n"
        f"    <title>{escape(cfg.get('title', 'Security Summary'))}</title>\n"
        f"    <link>{escape(pages_base)}</link>\n"
        f'    <atom:link href="{escape(feed_url)}" rel="self" type="application/rss+xml"/>\n'
        f"    <description>{escape(desc)}</description>\n"
        f"    <language>{escape(cfg.get('language', 'en-us'))}</language>\n"
        f"    <lastBuildDate>{now_rfc}</lastBuildDate>\n"
        f"    <itunes:author>{escape(cfg['github']['owner'])}</itunes:author>\n"
        f'    <itunes:category text="{escape(cfg.get("category", "Technology"))}"/>\n'
        "    <itunes:explicit>false</itunes:explicit>\n"
        f"    <itunes:summary>{escape(desc)}</itunes:summary>\n"
        f"{items}"
        "  </channel>\n"
        "</rss>\n"
    )


def _render_index_html(cfg: dict) -> str:
    pages_base = _pages_base_url(cfg)
    feed_url = pages_base + "feed.xml"
    title = escape(cfg.get("title", "Security Summary"))
    desc = escape(cfg.get("description", "").strip())
    return (
        "<!DOCTYPE html>\n"
        '<html lang="en"><head>\n'
        '<meta charset="utf-8">\n'
        f"<title>{title}</title>\n"
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        "<style>\n"
        "  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;\n"
        "         max-width: 640px; margin: 4rem auto; padding: 0 1.5rem;\n"
        "         line-height: 1.6; color: #1a1a1a; }\n"
        "  a { color: #0b5fff; }\n"
        "  code { background: #f3f3f3; padding: 2px 6px; border-radius: 3px;\n"
        "         word-break: break-all; }\n"
        "  .feed { margin-top: 1.5rem; padding: 1rem; background: #f8f8f8;\n"
        "          border-left: 3px solid #0b5fff; border-radius: 3px; }\n"
        "</style></head><body>\n"
        f"<h1>{title}</h1>\n"
        f"<p>{desc}</p>\n"
        '<div class="feed">\n'
        "<strong>Podcast feed:</strong><br>\n"
        f'<a href="feed.xml"><code>{escape(feed_url)}</code></a>\n'
        "</div>\n"
        "<p>Subscribe in Overcast, Apple Podcasts, Pocket Casts, or any podcast app by adding that URL.</p>\n"
        "</body></html>\n"
    )


def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        stream=sys.stderr,
    )
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    (DOCS_DIR / ".nojekyll").touch(exist_ok=True)
    cfg = _load_config()
    feed_xml = build_feed(cfg)
    (DOCS_DIR / "feed.xml").write_text(feed_xml)
    (DOCS_DIR / "index.html").write_text(_render_index_html(cfg))
    runs_included = feed_xml.count("<item>")
    print(f"podcast_feed.done episodes={runs_included} feed={DOCS_DIR / 'feed.xml'}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
