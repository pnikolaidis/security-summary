# security-summary

A nightly OSINT cybersecurity digest. Runs as a [Claude Routine](https://code.claude.com/docs/en/claude-code-on-the-web), collects across RSS / Reddit / Hacker News / Mastodon / Bluesky / CISA KEV / NVD, picks the top 5 stories of the last 24 hours, and emails a text + audio (MP3) summary.

## How it runs

The Routine executes [`ROUTINE_PROMPT.md`](./ROUTINE_PROMPT.md). The pipeline:

1. `python -m src.collect` — async fan-out across all sources → `state/inbox.json`.
2. Claude (in-session) reads the inbox, clusters / ranks / picks the top 5, writes `state/runs/<date>/summary.md` and `script.txt`.
3. `python -m src.deliver` — OpenAI TTS → `digest.mp3`, then Resend → email with MP3 attached.
4. `git commit && git push` — dedup state and the per-run artifacts go back to the repo.

## Setup

### 1. Create a Claude Routine
- Repo: this one.
- Schedule: nightly (e.g. `0 6 * * *` UTC = ~01:00 ET).
- Trigger: also enable "Run now" / API for on-demand.
- Setup script: `uv sync` (or use the default Python+uv image).

### 2. Network policy — `Custom`, allowlist:
```
api.openai.com
api.resend.com
oauth.reddit.com
www.reddit.com
infosec.exchange
public.api.bsky.app
hn.algolia.com
services.nvd.nist.gov
www.cisa.gov
krebsonsecurity.com
www.bleepingcomputer.com
feeds.feedburner.com
www.darkreading.com
www.schneier.com
googleprojectzero.blogspot.com
msrc.microsoft.com
github.com
isc.sans.edu
```
After the first run, check the routine logs for any other domains your RSS feeds redirect through and add them.

### 3. Environment variables
| Var | Required | Purpose |
|---|---|---|
| `OPENAI_API_KEY` | yes | TTS |
| `RESEND_API_KEY` | yes | Email transport |
| `RECIPIENT_EMAIL` | yes | Where to send the digest |
| `EMAIL_FROM` | no (default: `onboarding@resend.dev`) | Sender; verify a domain in Resend for a custom from-address |
| `NVD_API_KEY` | no but recommended | Lifts NVD rate limit from 5→50 req/30s |
| `REDDIT_CLIENT_ID` | no | Reddit script app — collector skipped if missing |
| `REDDIT_CLIENT_SECRET` | no | ditto |
| `REDDIT_USERNAME` | no | ditto |
| `REDDIT_PASSWORD` | no | ditto |
| `REDDIT_USER_AGENT` | no | Defaults to `security-summary/0.1 by u/<username>` — required by Reddit |

### Reddit auth setup (optional but recommended)
1. https://www.reddit.com/prefs/apps → "create app" → choose **script** type.
2. Set redirect URI to `http://localhost:8080` (unused for script apps).
3. Save `client_id` (under the app name) and `client_secret`.
4. Set the four env vars above. PRAW handles auth headlessly.

## Running locally for testing

```bash
uv sync
export OPENAI_API_KEY=...
export RESEND_API_KEY=...
export RECIPIENT_EMAIL=you@example.com
# Optional sources:
export NVD_API_KEY=...
export REDDIT_CLIENT_ID=... # etc

# Smoke test a single collector:
uv run python -m src.collectors.hackernews
uv run python -m src.collectors.cisa
uv run python -m src.collectors.bluesky

# Full pipeline (without using Claude for summarization):
uv run python -m src.collect
# Then hand-write state/runs/<today>/summary.md + script.txt to test delivery:
uv run python -m src.deliver
```

In a real Routine run, the cluster/rank/summarize step is done by Claude reading `state/inbox.json` directly — there is no separate script for it.

## Layout
```
src/
  collect.py             # async fan-out → state/inbox.json
  deliver.py             # TTS + Resend email
  normalize.py           # Item schema, URL canonicalization, CVE/vendor extraction
  dedup.py               # JSONL seen-set, 14-day rolling
  tts.py                 # OpenAI TTS + chunking + CVE/acronym preprocessing
  email_client.py        # Resend client + HTML template
  collectors/{rss,reddit,hackernews,mastodon,bluesky,cisa,nvd}.py
config/
  sources.yaml           # feeds, subreddits, hashtags, vendor list
  ranking.yaml           # weights for top-5 selection
state/                   # git-committed; persistent across runs
  seen.jsonl             # dedup
  inbox.json             # latest run's normalized items
  runs/YYYY-MM-DD/       # per-run summary.md, script.txt, digest.mp3, claude.log
ROUTINE_PROMPT.md        # the prompt the Routine executes (source of truth for the runbook)
```

## Tuning
- Edit `config/sources.yaml` to add/remove feeds, subreddits, hashtags, or vendor tokens.
- Edit `config/ranking.yaml` to reweight `diversity`/`recency`/`engagement`/`severity`/`novelty`. Restart effect is immediate — next run will pick up the change.
- Look at `state/runs/*/claude.log` after a few runs to see why specific items were or weren't selected.
