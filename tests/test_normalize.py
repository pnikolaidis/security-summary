from src.normalize import Item, canonical_url, extract_cves, match_vendors


def test_canonical_url_strips_tracking_params():
    url = "https://example.com/article/?utm_source=twitter&id=42&utm_campaign=foo"
    out = canonical_url(url)
    assert "utm_source" not in out
    assert "utm_campaign" not in out
    assert "id=42" in out


def test_canonical_url_drops_fragment_and_trailing_slash():
    assert canonical_url("https://EXAMPLE.com/a/b/#section") == "https://example.com/a/b"


def test_canonical_url_keeps_root_slash():
    assert canonical_url("https://example.com/") == "https://example.com/"


def test_extract_cves_finds_and_dedupes():
    text = "Patched CVE-2024-1234 and cve-2024-1234 again, plus CVE-2025-99999."
    assert extract_cves(text) == ["CVE-2024-1234", "CVE-2025-99999"]


def test_match_vendors_case_insensitive():
    assert match_vendors("Critical Microsoft Outlook bug", ["Microsoft", "Cisco"]) == ["Microsoft"]


def test_item_post_init_canonicalizes_url_and_extracts_cves():
    i = Item(
        source="x",
        source_family="news",
        url="https://example.com/post/?utm_source=foo",
        title="CVE-2025-12345 in Acme Widget",
        body="",
    )
    assert "utm_source" not in i.url
    assert "CVE-2025-12345" in i.cves


def test_item_url_and_content_hashes_are_stable():
    a = Item(source="x", source_family="news", url="https://example.com/a", title="t", body="b")
    b = Item(source="y", source_family="hn", url="https://example.com/a/?utm_source=foo", title="t", body="b")
    assert a.url_hash == b.url_hash  # canonicalization collapses tracking params
    assert a.content_hash == b.content_hash
