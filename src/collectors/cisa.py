from __future__ import annotations

import asyncio
import logging
from datetime import datetime, timedelta, timezone

import feedparser
import httpx

from src.normalize import Item

log = logging.getLogger(__name__)


async def _kev(client: httpx.AsyncClient, url: str, since: datetime) -> list[Item]:
    try:
        r = await client.get(url, timeout=20.0)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        log.warning("cisa.kev_fail error=%s", e)
        return []

    items: list[Item] = []
    for v in data.get("vulnerabilities", []):
        date_added = v.get("dateAdded")
        if not date_added:
            continue
        try:
            ts = datetime.fromisoformat(date_added).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
        if ts < since:
            continue
        cve = v.get("cveID", "")
        title = f"CISA KEV: {cve} — {v.get('vulnerabilityName', '')}"
        body = (
            f"{v.get('shortDescription', '')}\n\n"
            f"Vendor: {v.get('vendorProject', '')}\n"
            f"Product: {v.get('product', '')}\n"
            f"Required action: {v.get('requiredAction', '')}\n"
            f"Due date: {v.get('dueDate', '')}\n"
            f"Known ransomware use: {v.get('knownRansomwareCampaignUse', 'Unknown')}"
        )
        items.append(
            Item(
                source="cisa_kev",
                source_family="cisa",
                url=f"https://nvd.nist.gov/vuln/detail/{cve}",
                title=title,
                body=body,
                timestamp=ts,
                engagement=10.0,  # KEV items are inherently high-signal
                cves=[cve] if cve else [],
                vendors=[v.get("vendorProject", "")] if v.get("vendorProject") else [],
                raw=v,
            )
        )
    return items


async def _advisories(client: httpx.AsyncClient, url: str, since: datetime, vendors: list[str]) -> list[Item]:
    try:
        r = await client.get(url, timeout=15.0, follow_redirects=True)
        r.raise_for_status()
    except Exception as e:
        log.warning("cisa.advisories_fail error=%s", e)
        return []

    parsed = feedparser.parse(r.content)
    items: list[Item] = []
    for entry in parsed.entries:
        t = getattr(entry, "published_parsed", None) or getattr(entry, "updated_parsed", None)
        ts = datetime(*t[:6], tzinfo=timezone.utc) if t else datetime.now(timezone.utc)
        if ts < since:
            continue
        title = (entry.get("title") or "").strip()
        body = (entry.get("summary") or "")[:2000]
        items.append(
            Item(
                source="cisa_advisories",
                source_family="cisa",
                url=entry.get("link") or "",
                title=title,
                body=body,
                timestamp=ts,
                engagement=5.0,
                vendors=[v for v in vendors if v.lower() in (title + " " + body).lower()],
                raw={"source": "cisa_advisories"},
            )
        )
    return items


async def collect(config: dict) -> list[Item]:
    cisa = config.get("cisa", {})
    lookback_hours = config.get("lookback_hours", 24)
    vendors = config.get("vendors", [])
    since = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)

    async with httpx.AsyncClient(headers={"User-Agent": "security-summary/0.1"}) as client:
        kev, adv = await asyncio.gather(
            _kev(client, cisa.get("kev_url", ""), since),
            _advisories(client, cisa.get("advisories_rss", ""), since, vendors),
        )
    return kev + adv


if __name__ == "__main__":
    import json
    from pathlib import Path

    import yaml

    cfg = yaml.safe_load(Path("config/sources.yaml").read_text())
    items = asyncio.run(collect(cfg))
    print(json.dumps([i.to_dict() for i in items[:5]], indent=2, default=str))
    print(f"\nTotal: {len(items)}")
