# Routine: Nightly Security Digest

You are running as a Claude Routine. Your job is to produce and deliver a security digest end-to-end. Be autonomous — do not ask questions, do not skip steps, log meaningfully so the user can debug from the git history.

## Environment expected
- Repo cloned fresh at start; commit + push state at end.
- Network policy: Custom allowlist (see README.md for the list).
- Env vars: `OPENAI_API_KEY`, `RESEND_API_KEY`, `RECIPIENT_EMAIL`, `EMAIL_FROM`, `NVD_API_KEY` (optional), Reddit creds (`REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USERNAME`, `REDDIT_PASSWORD`, `REDDIT_USER_AGENT`).

## Steps

### 1. Install dependencies
```bash
uv sync
```

### 2. Identify today's persona
```bash
uv run python -m src.persona
```
This prints `{"name": "...", "voice": "...", "intro_hint": "..."}`. Note the **name** — you'll weave it into the script intro and the email body. The deliver step reads the same config and selects the matching voice automatically.

### 3. Collect
```bash
uv run python -m src.collect
```
Writes `state/inbox.json` (new items since last run) and updates `state/seen.jsonl` (URL-level dedup). Per-source failures are non-fatal — logged to stderr, run continues.

If `state/inbox.json` reports zero new items, skip to step 7 and send a "Quiet day" email (no top-5; one paragraph noting nothing surfaced; still use the persona name in the script intro).

### 4. Cluster, rank, pick top 5
Read `state/inbox.json`. Apply these rules in order — first match assigns an item to a cluster:

1. **Same CVE ID** — items sharing any CVE-XXXX-YYYY are one cluster.
2. **Same canonical URL** — already deduped, but cross-platform reposts cluster here.
3. **Fuzzy title match** — `rapidfuzz.fuzz.token_set_ratio(title_a, title_b) >= 85` within a 48-hour window.
4. **≥ 2 shared vendor tokens AND timestamps within 24 h** — clusters when discussing the same incident at the same vendor.

Score each cluster (weights from `config/ranking.yaml`):
```
score =   w_diversity  * log(1 + distinct_source_families)
        + w_recency    * exp(-hours_since_newest / 24)
        + w_engagement * z(sum(engagement))    # z-score within source_family
        + w_severity   * severity_boost        # +1.0 CVSS>=9, +0.5 KEV, +0.5 "actively exploited"/"in the wild"/"0-day"
        - w_novelty    * cluster_seen_in_last_7d   # check seen.jsonl
```

Greedy top-N selection with diversity: skip a cluster that shares ≥ 2 vendor tokens AND any CVE with an already-picked cluster.

### 5. Cross-day deduplication (NEW)
You produce a digest *every* day, so the same story can keep cropping up. The goal: avoid hearing the same "breaking" news two days in a row, but DO follow stories as they develop.

Load the last 7 days of featured stories:
```bash
uv run python -m src.featured load 7
```

For each candidate cluster (after step 4 ranking, before final selection), classify it. The easy path is to call the helper:
```bash
echo '{"title": "...", "cves": ["CVE-..."], "vendors": ["Cisco"], "source_families": ["news","reddit"]}' \
  | uv run python -m src.featured classify
```

It returns one of:
- **`same`** — strong match to a recent featured story, no new sources/evidence → **drop** from candidates entirely (unless its score is dramatically higher than when last featured AND there's clear new evidence; in that rare case, treat as `developing`).
- **`developing`** — strong/partial match BUT new source families or a new event (patch released, exploit confirmed, scope expanded, new vendor implicated) → **keep**; prefix the headline with `Developing:` in summary.md and start the audio block with "Following up on…"
- **`different`** — no meaningful match → treat normally.

After final top-5 selection, append to the featured log:
```bash
# picks.json is a JSON array of objects with these keys:
# {title, cves, vendors, source_families, score, status, representative_url}
cat picks.json | uv run python -m src.featured append
```

This makes today's picks visible to tomorrow's run.

### 6. Write outputs
Create `state/runs/YYYY-MM-DD/` (today's UTC date) and write:

**`summary.md`** — the email body:
```markdown
# Security Digest — YYYY-MM-DD
*Today's brief by <persona name>.*

## TL;DR
<3–5 sentences across all 5 picks>

## 1. <Concise headline>            (or "Developing: <headline>" for follow-ups)
**Why it matters:** <single sentence>

<2–3 sentence summary>

*Covered in: <source>, <source>, … — N posts across M sources*
- [<title>](<url>)
- [<title>](<url>)

## 2. …
(repeat for 3, 4, 5)

## Signal stats
- Total items processed: N
- New (post-dedup): N
- Clusters formed: N
- Same-as-recent suppressed: N
- Developing follow-ups: N
- Top 5 selected from: N candidate clusters
```

**`script.txt`** — the TTS source:
- Spoken-friendly. NO URLs. NO markdown. Plain paragraphs.
- Open with the persona's `intro_hint` (or a natural adaptation) so the listener knows who's speaking. Example: "Good morning. I'm Allie with your Monday security briefing for May 22nd."
- For each story: state the headline conversationally, then 2–3 sentences of context, then "why it matters." Developing stories should start "Following up on…"
- Pause between stories with a blank line.
- Close with a brief sign-off that includes the persona's name. Example: "That's your digest. Allie out — stay safe."
- Target: 600–900 words. Hard cap 1,400 words.
- Acronyms and CVE IDs: write them normally — the TTS preprocessor handles expansion.

**`claude.log`** — observability (plain text or JSON, your choice):
- For each candidate cluster: members (URLs), score breakdown, the cross-day classification (same/developing/different) with the reason, selected/dropped.
- Note any dedup decisions of interest so the user can grep for "why did this story not appear today?"

### 7. Deliver
```bash
uv run python -m src.deliver
```
Generates `digest.mp3` from `script.txt` using today's persona's voice, then emails via Resend with the persona name in the From-line + subject.

On a quiet day, still call deliver — short script is fine.

### 8. Rebuild the podcast feed
```bash
uv run python -m src.podcast_feed
```
Regenerates `docs/feed.xml` from `state/runs/*/` (most recent 60 episodes). MP3 enclosure URLs point at raw.githubusercontent.com, so the audio file doesn't get duplicated on disk. Also touches `docs/index.html` and `docs/.nojekyll` so GitHub Pages serves the feed cleanly.

### 9. Commit + push **to `main`** (not a feature branch)
By default Claude Code on the web creates a `claude/`-prefixed feature branch for each session. **This routine does not want that** — the digest pipeline needs every run's artifacts to land on `main` so the podcast feed (`docs/feed.xml`, served via GitHub Pages from `main`) and the cross-day dedup state (`state/featured.jsonl`) persist across runs. If runs go to feature branches, the feed stays empty forever.

Do this exactly:
```bash
git fetch origin main
git checkout main
git pull --rebase origin main
git add state/ docs/
git commit -m "digest: YYYY-MM-DD"
git push origin main
```
If the push is rejected with `host_not_allowed` or a permission error, the routine doesn't have **Allow unrestricted branch pushes** enabled. Stop and surface the error — do not silently fall back to a feature branch (that defeats the whole pipeline).

If a push race occurs (previous run hasn't landed yet), the `pull --rebase` brings it in; rerun the push. If rebase conflicts on `state/seen.jsonl` or `state/featured.jsonl`, resolve by taking the union of both files' JSON-lines and dedup-by-key (`url_hash` and `date+representative_url` respectively).

## Scope discipline
This routine has exactly one job: produce and deliver the day's digest, then commit the artifacts. **Do not** add features, refactor code, add new collectors, change `config/`, modify `pyproject.toml`, or commit anything outside `state/` and `docs/`. If a step in this prompt seems broken or missing, log the gap to `state/runs/<date>/claude.log` and proceed with the deliverable — don't fix it in this session. The user reviews `claude.log` and decides what to change.

## Failure handling
- Per-collector failures are non-fatal (handled by `src/collectors/__init__.py`).
- If `src.collect` crashes: bail, no email sent, exit non-zero so the routine is visibly red.
- If `src.deliver` fails after TTS but before email: the MP3 is already on disk; commit the run dir anyway so it's not lost, then re-raise.
- If Resend returns an error: surface it in the routine log AND keep the run dir committed.
- If `src.featured append` fails: not fatal — the day's MP3 still goes out. Log it and continue. Cross-day dedup will just skip that day.
