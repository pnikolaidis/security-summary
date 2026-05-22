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

### 2. Collect
```bash
uv run python -m src.collect
```
This writes `state/inbox.json` (new items since last run) and updates `state/seen.jsonl` (dedup state). Any per-source failures are non-fatal — they're logged to stderr and the run continues.

If `state/inbox.json` reports zero new items, skip to step 5 and send a "Quiet day" email (no top-5; one-paragraph note that nothing new surfaced).

### 3. Cluster, rank, pick top 5
Read `state/inbox.json`. Apply these rules in order — first match assigns an item to a cluster:

1. **Same CVE ID** — items sharing any CVE-XXXX-YYYY are one cluster.
2. **Same canonical URL** — already deduped, but cross-platform reposts (e.g., article on Bleeping + Reddit link to it) cluster here.
3. **Fuzzy title match** — `rapidfuzz.fuzz.token_set_ratio(title_a, title_b) >= 85` within a 48-hour window.
4. **≥ 2 shared vendor tokens AND timestamps within 24h** — clusters when discussing the same incident at the same vendor.

Score each cluster (weights from `config/ranking.yaml`):
```
score =   w_diversity  * log(1 + distinct_source_families)
        + w_recency    * exp(-hours_since_newest / 24)
        + w_engagement * z(sum(engagement))    # z-score within each source_family
        + w_severity   * severity_boost        # +1.0 CVSS>=9, +0.5 KEV, +0.5 "actively exploited"/"in the wild"/"0-day"/"zero-day"
        - w_novelty    * cluster_seen_in_last_7d   # check seen.jsonl
```

Select top 5 greedily, skipping any cluster that shares ≥ 2 vendor tokens AND any CVE with an already-picked cluster (diversity filter).

### 4. Write outputs
Create `state/runs/YYYY-MM-DD/` (use today's UTC date) and write:

**`summary.md`** — the email body:
```markdown
# Security Digest — YYYY-MM-DD

## TL;DR
<3–5 sentences summarizing all 5 picks at a glance>

## 1. <Concise headline>
**Why it matters:** <single sentence — the impact / who's affected>

<2–3 sentence summary of what's happening>

*Covered in: <source 1>, <source 2>, ... — N posts across M sources*
- [<title>](<url>)
- [<title>](<url>)

## 2. ...
(repeat for 3, 4, 5)

## Signal stats
- Total items processed: N
- New (post-dedup): N
- Clusters formed: N
- Top 5 selected from: N candidate clusters
```

**`script.txt`** — the TTS source:
- Spoken-friendly. NO URLs. NO markdown. Plain paragraphs separated by blank lines.
- Open: "Good morning. Here is your security digest for <date>. <one-sentence overall framing>."
- For each story: state the headline conversationally, then 2-3 sentences of context, then "why it matters."
- Pause between stories with a blank line.
- Close: "That's your digest. Stay safe out there."
- Target: 600–900 words. Hard cap 1,400 words (chunking handles up to ~14k chars, but shorter is friendlier).
- Acronyms and CVE IDs: write them normally — the TTS preprocessor handles expansion.

**`claude.log`** — observability:
- For each cluster: members (URLs), score breakdown (diversity, recency, engagement, severity, novelty), why selected/dropped.
- Note any dedup decisions of interest.
- Plain text or JSON, doesn't matter — this is for the user to grep.

### 5. Deliver
```bash
uv run python -m src.deliver
```
This generates `digest.mp3` from `script.txt` and sends the email via Resend with the MP3 attached.

If today is a "quiet day," still call `src.deliver` — it'll send the summary without freaking out on the short script.

### 6. Commit + push
```bash
git add state/
git commit -m "digest: YYYY-MM-DD"
git push -u origin HEAD
```
If a push race occurs (the previous run hasn't fully landed), `git pull --rebase` then retry once.

## Failure handling
- Per-collector failures are non-fatal (handled by `src/collectors/__init__.py`).
- If `src.collect` itself crashes: bail, no email sent, log and exit non-zero so the routine is visibly red.
- If `src.deliver` fails after TTS but before email: the MP3 is already on disk; commit the run dir anyway so it's not lost, then re-raise.
- If Resend returns an error: surface it in the routine log AND keep the run dir committed.
