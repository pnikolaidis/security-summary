"""TTS rendering for the audio version of the digest."""
from __future__ import annotations

import logging
import os
import re
from pathlib import Path

log = logging.getLogger(__name__)

# Acronyms that should be spelled out (read as individual letters) when first
# encountered in a sentence. CVE IDs handled separately below.
_LETTERED_ACRONYMS = {
    "CISA", "NVD", "KEV", "CVE", "CVSS", "API", "SSH", "TLS", "SSL", "URL",
    "DNS", "OSINT", "MFA", "2FA", "VPN", "RCE", "SQLi", "XSS", "IAM", "SaaS",
    "IoT", "OT", "ICS", "AWS", "GCP", "MSRC",
}

_CVE_RE = re.compile(r"CVE-(\d{4})-(\d{4,7})", re.IGNORECASE)
_URL_RE = re.compile(r"https?://\S+")
_MD_HEADER_RE = re.compile(r"^#+\s*", re.MULTILINE)
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_MD_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
_MD_ITALIC_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")
_MD_LIST_RE = re.compile(r"^[\-\*]\s+", re.MULTILINE)


def _year_to_words(year_str: str) -> str:
    """Convert e.g. '2025' -> 'twenty twenty-five'. Light touch for 19xx/20xx only."""
    if len(year_str) != 4 or not year_str.isdigit():
        return year_str
    n = int(year_str)
    if 2000 <= n <= 2009:
        return f"two thousand {_digit_words(year_str[3])}" if year_str[3] != "0" else "two thousand"
    if 2010 <= n <= 2099:
        first = "twenty"
        second_num = int(year_str[2:])
        second = _below_hundred(second_num)
        return f"{first} {second}".strip()
    if 1900 <= n <= 1999:
        return f"nineteen {_below_hundred(int(year_str[2:]))}".strip()
    return year_str


_BELOW_TWENTY = {
    0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
    7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
    13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
    17: "seventeen", 18: "eighteen", 19: "nineteen",
}
_TENS = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}


def _below_hundred(n: int) -> str:
    if n < 20:
        return _BELOW_TWENTY[n]
    tens, ones = divmod(n, 10)
    return _TENS[tens] + (f"-{_BELOW_TWENTY[ones]}" if ones else "")


def _digit_words(s: str) -> str:
    return " ".join(_BELOW_TWENTY[int(c)] if c.isdigit() else c for c in s).strip()


def _expand_cve(match: re.Match) -> str:
    year, ident = match.group(1), match.group(2)
    return f"C V E {_year_to_words(year)} dash {_digit_words(ident)}"


def preprocess_for_tts(text: str) -> str:
    # Markdown first so we can replace [label](url) with just `label` before
    # the URL-stripper would otherwise leave an orphan `[label]()`.
    text = _MD_HEADER_RE.sub("", text)
    text = _MD_LINK_RE.sub(r"\1", text)
    text = _MD_BOLD_RE.sub(r"\1", text)
    text = _MD_ITALIC_RE.sub(r"\1", text)
    text = _MD_LIST_RE.sub("", text)
    # Then strip any remaining bare URLs — they're noise when read aloud.
    text = _URL_RE.sub("", text)
    # CVE IDs — spell out.
    text = _CVE_RE.sub(_expand_cve, text)
    # Lettered acronyms — space-separate so the model reads them as letters.
    for acr in _LETTERED_ACRONYMS:
        text = re.sub(rf"\b{acr}\b", " ".join(acr), text)
    # Collapse whitespace.
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


_TTS_CHUNK_LIMIT = 3500  # under OpenAI's 4096 hard limit, with safety margin
_MAX_TOTAL_CHARS = 14000  # ~10–12 minutes audio; hard cap for sanity


def _chunk_for_tts(text: str, limit: int = _TTS_CHUNK_LIMIT) -> list[str]:
    """Split on paragraph then sentence boundaries; each chunk <= limit chars."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    buf = ""
    for para in paragraphs:
        candidate = (buf + "\n\n" + para).strip() if buf else para
        if len(candidate) <= limit:
            buf = candidate
            continue
        if buf:
            chunks.append(buf)
            buf = ""
        # Single paragraph too big — split on sentences.
        if len(para) <= limit:
            buf = para
        else:
            sentences = re.split(r"(?<=[.!?])\s+", para)
            for s in sentences:
                if not s:
                    continue
                cand = (buf + " " + s).strip() if buf else s
                if len(cand) <= limit:
                    buf = cand
                else:
                    if buf:
                        chunks.append(buf)
                    buf = s[:limit]
    if buf:
        chunks.append(buf)
    return chunks


def synthesize(script: str, out_path: Path, voice: str = "nova", model: str = "tts-1") -> Path:
    """Synthesize `script` to MP3 via OpenAI TTS. Returns the output path.

    Chunks input on paragraph/sentence boundaries to stay under OpenAI's
    4096-char per-request limit; concatenates MP3 byte streams.
    """
    from openai import OpenAI  # lazy import

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    processed = preprocess_for_tts(script)
    if len(processed) > _MAX_TOTAL_CHARS:
        log.warning("tts.truncated original_len=%d cap=%d", len(processed), _MAX_TOTAL_CHARS)
        processed = processed[:_MAX_TOTAL_CHARS]
    chunks = _chunk_for_tts(processed)
    log.info("tts.synth chunks=%d total_chars=%d", len(chunks), len(processed))

    with open(out_path, "wb") as out:
        for i, chunk in enumerate(chunks):
            with client.audio.speech.with_streaming_response.create(
                model=model, voice=voice, input=chunk, response_format="mp3"
            ) as response:
                for data in response.iter_bytes():
                    out.write(data)
            log.info("tts.chunk_done %d/%d chars=%d", i + 1, len(chunks), len(chunk))
    return out_path
