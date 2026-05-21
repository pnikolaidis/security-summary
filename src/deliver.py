"""TTS + email delivery for the day's digest.

Usage: python -m src.deliver [YYYY-MM-DD]

Reads state/runs/<date>/summary.md and script.txt, produces digest.mp3 in the
same directory, then sends the email via Resend.
"""
from __future__ import annotations

import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

from src import email_client, tts

ROOT = Path(__file__).resolve().parent.parent


def main(date_str: str | None = None) -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        stream=sys.stderr,
    )
    today = date_str or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    run_dir = ROOT / "state" / "runs" / today
    summary_path = run_dir / "summary.md"
    script_path = run_dir / "script.txt"
    mp3_path = run_dir / "digest.mp3"

    if not summary_path.exists():
        print(f"deliver.error missing={summary_path}", file=sys.stderr)
        return 1
    if not script_path.exists():
        print(f"deliver.error missing={script_path}", file=sys.stderr)
        return 1

    summary_md = summary_path.read_text()
    script_text = script_path.read_text()

    tts.synthesize(script_text, mp3_path)
    subject = f"Security Digest — {today}"
    html = email_client.render_html(summary_md, subject)
    resp = email_client.send(subject, html, mp3_path)
    print(f"deliver.done mp3={mp3_path} email_id={resp.get('id', 'n/a')}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    sys.exit(main(arg))
