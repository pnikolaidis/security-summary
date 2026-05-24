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
news.risky.biz
www.zetter-zeroday.com
srslyriskybiz.substack.com
www.youtube.com
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
  deliver.py             # TTS + Resend email; reads today's persona
  normalize.py           # Item schema, URL canonicalization, CVE/vendor extraction
  dedup.py               # URL-level JSONL seen-set, 14-day rolling
  featured.py            # cross-day topic dedup: same / developing / different
  persona.py             # date → persona (name + voice + intro_hint)
  tts.py                 # OpenAI TTS + chunking + CVE/acronym preprocessing
  email_client.py        # Resend client + HTML template + persona From-name
  collectors/{rss,reddit,hackernews,mastodon,bluesky,cisa,nvd}.py
  podcast_feed.py        # regenerates docs/feed.xml + docs/index.html
config/
  sources.yaml           # feeds, subreddits, hashtags, vendor list
  ranking.yaml           # weights for top-5 selection
  personas.yaml          # weekday → {voice, name, intro_hint}
  podcast.yaml           # feed metadata + GitHub Pages owner/repo/branch
state/                   # git-committed; persistent across runs
  seen.jsonl             # URL-level dedup
  featured.jsonl         # cross-day topic dedup (append-only log of past picks)
  inbox.json             # latest run's normalized items
  runs/YYYY-MM-DD/       # per-run summary.md, script.txt, digest.mp3, claude.log
docs/                    # GitHub Pages site (committed)
  feed.xml               # podcast RSS feed
  index.html             # landing page with the feed URL
  .nojekyll              # tells Pages not to run Jekyll
ROUTINE_PROMPT.md        # the prompt the Routine executes (source of truth for the runbook)
```

## Podcast feed (listen in Overcast / Apple Podcasts / etc.)

Each run regenerates `docs/feed.xml` from the last 60 episodes; GitHub Pages serves it as a real podcast feed.

**One-time setup (after merging the first PR with `docs/`):**
1. GitHub repo → **Settings** → **Pages**.
2. **Source:** Deploy from a branch.
3. **Branch:** `main`, **folder:** `/docs`.
4. Save. Within ~1 min the feed is live at:
   ```
   https://pnikolaidis.github.io/security-summary/feed.xml
   ```
5. In Overcast → **+** → **Add URL** → paste the URL above.

The MP3 enclosures point at `raw.githubusercontent.com/pnikolaidis/security-summary/main/state/runs/<date>/digest.mp3` so the audio isn't duplicated in `docs/`.

If you fork or rename the repo, update `config/podcast.yaml` (`github.owner`, `github.repo`, `github.branch`). The Pages URL and the raw URLs are derived from those values.

## Personas + voice rotation

Each weekday has its own host with a distinct OpenAI TTS voice. The persona drives:
- The email's From-name (`Allie <onboarding@resend.dev>`)
- The email subject (`Security Digest — 2026-05-25 (Allie)`)
- The audio script's opening line and sign-off
- The TTS voice used to generate `digest.mp3`

Defaults (Mon → Sun): Allie, Adam Insight, Ada Iverson, Aiden Iyer, Avery Ito, Aria Inoue, Andi. Edit `config/personas.yaml` to rename, change voices, or shorten the rotation — the list is indexed by `date.weekday() % len(personas)`, so any length works.

Inspect today's pick:
```bash
uv run python -m src.persona              # today
uv run python -m src.persona 2026-05-25   # a specific date
```

## Cross-day deduplication

Items already seen *as URLs* are filtered by `state/seen.jsonl`. Stories already *featured in the digest* are tracked separately in `state/featured.jsonl` so the same "breaking" headline doesn't reappear day after day. Each run classifies its candidate clusters against the last 7 days of features:

| Classification | When | Behavior |
|---|---|---|
| `same` | Strong match (shared CVE + vendor + fuzzy title ≥ 70), no new source families | Dropped from candidates |
| `developing` | Strong match BUT new source families OR new event (patch, exploit confirmed, scope expanded) | Kept; headline prefixed `Developing:` and audio starts "Following up on…" |
| `different` | No meaningful match | Treated normally |

Inspect:
```bash
uv run python -m src.featured load 7      # last 7 days of features as JSON
```

Tune the thresholds in `src/featured.py` (`STRONG_MATCH_SCORE`, `WEAK_MATCH_FLOOR`).

## Tuning
- Edit `config/sources.yaml` to add/remove feeds, subreddits, hashtags, or vendor tokens.
- Edit `config/personas.yaml` to change voices/names/rotation.
- Edit `config/ranking.yaml` to reweight `diversity`/`recency`/`engagement`/`severity`/`novelty`. Next run picks up the change.
- Look at `state/runs/*/claude.log` after a few runs to see why specific items were or weren't selected (and which were suppressed as `same`).
