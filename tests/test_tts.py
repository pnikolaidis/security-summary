from src.tts import _chunk_for_tts, preprocess_for_tts


def test_cve_expansion():
    out = preprocess_for_tts("Patched CVE-2025-12345 today.")
    assert "C V E twenty twenty-five dash one two three four five" in out
    assert "CVE-2025-12345" not in out


def test_strips_urls():
    out = preprocess_for_tts("See https://example.com/foo/bar for details.")
    assert "https://" not in out
    assert "example.com" not in out


def test_acronym_spacing():
    out = preprocess_for_tts("CISA added it to KEV.")
    assert "C I S A" in out
    assert "K E V" in out


def test_strips_markdown():
    md = "# Header\n\n**Bold** and *italic* and [link](https://x.com)."
    out = preprocess_for_tts(md)
    assert "#" not in out
    assert "**" not in out
    assert "[" not in out and "]" not in out
    assert "Bold" in out and "italic" in out and "link" in out


def test_chunk_under_limit_returns_single_chunk():
    text = "Hello world."
    chunks = _chunk_for_tts(text, limit=4000)
    assert chunks == ["Hello world."]


def test_chunk_splits_long_text_on_paragraphs():
    para = "A" * 2000
    text = "\n\n".join([para, para, para])  # ~6000 chars
    chunks = _chunk_for_tts(text, limit=3500)
    assert len(chunks) >= 2
    assert all(len(c) <= 3500 for c in chunks)


def test_chunk_splits_oversized_paragraph_on_sentences():
    long_para = ". ".join(["Sentence number " + str(i) for i in range(500)]) + "."
    chunks = _chunk_for_tts(long_para, limit=200)
    assert all(len(c) <= 200 for c in chunks)
    assert len(chunks) > 1
