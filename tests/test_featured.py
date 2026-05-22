import json
from datetime import date, timedelta

from src.featured import append, classify, load_recent


def test_append_round_trip(tmp_path):
    path = tmp_path / "featured.jsonl"
    append(
        [
            {
                "title": "Cisco ASA RCE actively exploited",
                "cves": ["CVE-2026-12345"],
                "vendors": ["Cisco"],
                "score": 7.2,
                "source_families": ["news", "reddit"],
            }
        ],
        run_date=date.today(),
        path=path,
    )
    recent = load_recent(days=7, path=path)
    assert len(recent) == 1
    assert recent[0]["title"] == "Cisco ASA RCE actively exploited"
    assert recent[0]["cves"] == ["CVE-2026-12345"]
    assert recent[0]["rank"] == 1


def test_load_recent_expires_old_entries(tmp_path):
    path = tmp_path / "featured.jsonl"
    old = {
        "date": (date.today() - timedelta(days=30)).isoformat(),
        "title": "old", "cves": [], "vendors": [], "score": 1.0,
        "source_families": [], "rank": 1, "representative_url": "", "status": "fresh",
    }
    new = {
        "date": date.today().isoformat(),
        "title": "new", "cves": [], "vendors": [], "score": 1.0,
        "source_families": [], "rank": 1, "representative_url": "", "status": "fresh",
    }
    path.write_text(json.dumps(old) + "\n" + json.dumps(new) + "\n")
    assert [r["title"] for r in load_recent(days=7, path=path)] == ["new"]


def _entry(title="x", cves=None, vendors=None, source_families=None, days_ago=1):
    return {
        "date": (date.today() - timedelta(days=days_ago)).isoformat(),
        "title": title,
        "cves": cves or [],
        "vendors": vendors or [],
        "source_families": source_families or [],
        "rank": 1,
        "score": 1.0,
        "representative_url": "",
        "status": "fresh",
    }


def test_classify_same_when_cve_and_vendor_match_and_no_new_sources():
    recent = [_entry(
        title="Cisco ASA RCE actively exploited",
        cves=["CVE-2026-12345"],
        vendors=["Cisco"],
        source_families=["news", "reddit"],
    )]
    cluster = {
        "title": "Cisco ASA RCE actively exploited in the wild",
        "cves": ["CVE-2026-12345"],
        "vendors": ["Cisco"],
        "source_families": ["news", "reddit"],
    }
    assert classify(cluster, recent)["status"] == "same"


def test_classify_developing_when_new_source_appears():
    recent = [_entry(
        title="Cisco ASA RCE",
        cves=["CVE-2026-12345"],
        vendors=["Cisco"],
        source_families=["news"],
    )]
    cluster = {
        "title": "Cisco ASA RCE — patch released",
        "cves": ["CVE-2026-12345"],
        "vendors": ["Cisco"],
        "source_families": ["news", "reddit", "mastodon"],
    }
    assert classify(cluster, recent)["status"] == "developing"


def test_classify_different_when_unrelated():
    recent = [_entry(
        title="Cisco ASA RCE",
        cves=["CVE-2026-12345"],
        vendors=["Cisco"],
        source_families=["news"],
    )]
    cluster = {
        "title": "Fortinet auth bypass disclosed",
        "cves": ["CVE-2026-99999"],
        "vendors": ["Fortinet"],
        "source_families": ["news"],
    }
    assert classify(cluster, recent)["status"] == "different"


def test_classify_returns_different_for_empty_history():
    cluster = {"title": "anything", "cves": ["CVE-2026-1"], "vendors": ["X"], "source_families": ["news"]}
    assert classify(cluster, [])["status"] == "different"
