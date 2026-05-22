from __future__ import annotations

import asyncio
import logging
import os
from datetime import datetime, timedelta, timezone

import httpx

from src.normalize import Item

log = logging.getLogger(__name__)

NVD_API = "https://services.nvd.nist.gov/rest/json/cves/2.0"


def _iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S.000")


def _best_cvss(metrics: dict) -> tuple[float, str | None]:
    for key in ("cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
        for entry in metrics.get(key, []):
            data = entry.get("cvssData") or {}
            score = data.get("baseScore")
            if isinstance(score, (int, float)):
                return float(score), data.get("baseSeverity") or data.get("severity")
    return 0.0, None


async def collect(config: dict) -> list[Item]:
    nvd = config.get("nvd", {})
    lookback_hours = config.get("lookback_hours", 24)
    min_cvss = float(nvd.get("min_cvss", 7.0))
    vendors = config.get("vendors", [])
    now = datetime.now(timezone.utc)
    since = now - timedelta(hours=lookback_hours)

    params = {
        "pubStartDate": _iso(since),
        "pubEndDate": _iso(now),
        "resultsPerPage": int(nvd.get("results_per_page", 200)),
    }
    headers = {"User-Agent": "security-summary/0.1"}
    api_key = os.environ.get("NVD_API_KEY")
    if api_key:
        headers["apiKey"] = api_key

    items: list[Item] = []
    async with httpx.AsyncClient(headers=headers) as client:
        try:
            r = await client.get(NVD_API, params=params, timeout=20.0)
            r.raise_for_status()
            data = r.json()
        except Exception as e:
            log.warning("nvd.fetch_fail error=%s", e)
            return []

    for v in data.get("vulnerabilities", []):
        cve = v.get("cve", {})
        cve_id = cve.get("id", "")
        if not cve_id:
            continue
        descs = cve.get("descriptions", [])
        desc = next((d["value"] for d in descs if d.get("lang") == "en"), "")
        score, sev = _best_cvss(cve.get("metrics", {}))
        if score < min_cvss:
            continue
        pub = cve.get("published")
        try:
            ts = datetime.fromisoformat(pub.replace("Z", "+00:00")) if pub else now
        except (ValueError, AttributeError):
            ts = now
        title = f"{cve_id} ({sev or 'CVSS ' + str(score)}) — {desc[:140]}"
        items.append(
            Item(
                source="nvd",
                source_family="nvd",
                url=f"https://nvd.nist.gov/vuln/detail/{cve_id}",
                title=title,
                body=desc[:2000],
                timestamp=ts,
                engagement=score,  # use CVSS as engagement signal for NVD
                cves=[cve_id],
                vendors=[vd for vd in vendors if vd.lower() in (desc or "").lower()],
                raw={"cvss": score, "severity": sev},
            )
        )
    return items


if __name__ == "__main__":
    import json
    from pathlib import Path

    import yaml

    cfg = yaml.safe_load(Path("config/sources.yaml").read_text())
    items = asyncio.run(collect(cfg))
    print(json.dumps([i.to_dict() for i in items[:5]], indent=2, default=str))
    print(f"\nTotal: {len(items)}")
