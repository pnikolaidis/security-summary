from datetime import date

from src.persona import for_date


def test_for_date_is_deterministic():
    d = date(2026, 5, 25)
    assert for_date(d) == for_date(d)


def test_for_date_rotates_through_week():
    # 7 distinct weekdays should give 7 distinct lookups; with 7 personas
    # configured we expect all names distinct (with nova reused on Sun, all
    # *names* are still unique per the default config).
    monday = date(2026, 5, 25)  # weekday() = 0
    names = {for_date(date.fromordinal(monday.toordinal() + i)).name for i in range(7)}
    assert len(names) == 7


def test_for_date_voice_is_known_openai_voice():
    valid = {"alloy", "echo", "fable", "onyx", "nova", "shimmer", "ash", "sage", "coral"}
    for i in range(7):
        d = date.fromordinal(date(2026, 5, 25).toordinal() + i)
        assert for_date(d).voice in valid, f"unknown voice on {d}: {for_date(d).voice}"
