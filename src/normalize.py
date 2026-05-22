from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}", re.IGNORECASE)

_TRACKING_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "ref", "ref_src", "ref_url", "mc_cid", "mc_eid", "fbclid", "gclid",
    "_hsenc", "_hsmi", "hsCtaTracking",
}


def canonical_url(url: str) -> str:
    try:
        parts = urlsplit(url.strip())
    except ValueError:
        return url
    query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=False) if k.lower() not in _TRACKING_PARAMS]
    path = parts.path.rstrip("/") or "/"
    cleaned = parts._replace(query=urlencode(query), fragment="", path=path, netloc=parts.netloc.lower())
    return urlunsplit(cleaned)


def extract_cves(text: str) -> list[str]:
    return sorted({m.group(0).upper() for m in CVE_RE.finditer(text or "")})


def match_vendors(text: str, vendor_list: list[str]) -> list[str]:
    if not text:
        return []
    lo = text.lower()
    return sorted({v for v in vendor_list if v.lower() in lo})


def hash_url(url: str) -> str:
    return hashlib.sha256(canonical_url(url).encode("utf-8")).hexdigest()[:16]


def hash_content(title: str, body: str) -> str:
    blob = f"{title.strip().lower()}\n{(body or '')[:500].strip().lower()}"
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


@dataclass
class Item:
    source: str
    source_family: str
    url: str
    title: str
    body: str = ""
    author: str | None = None
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    engagement: float = 0.0
    cves: list[str] = field(default_factory=list)
    vendors: list[str] = field(default_factory=list)
    raw: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.url = canonical_url(self.url)
        if self.timestamp.tzinfo is None:
            self.timestamp = self.timestamp.replace(tzinfo=timezone.utc)
        if not self.cves:
            self.cves = extract_cves(f"{self.title}\n{self.body}")

    @property
    def url_hash(self) -> str:
        return hash_url(self.url)

    @property
    def content_hash(self) -> str:
        return hash_content(self.title, self.body)

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["timestamp"] = self.timestamp.isoformat()
        d["url_hash"] = self.url_hash
        d["content_hash"] = self.content_hash
        return d
