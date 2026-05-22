import os

import pytest

from src.email_client import _from_field


@pytest.fixture(autouse=True)
def _restore_env():
    saved = os.environ.get("EMAIL_FROM")
    yield
    if saved is None:
        os.environ.pop("EMAIL_FROM", None)
    else:
        os.environ["EMAIL_FROM"] = saved


def test_from_field_wraps_bare_email_with_persona_name():
    os.environ["EMAIL_FROM"] = "onboarding@resend.dev"
    assert _from_field("Allie") == "Allie <onboarding@resend.dev>"


def test_from_field_falls_back_to_default_when_no_persona():
    os.environ["EMAIL_FROM"] = "onboarding@resend.dev"
    assert _from_field(None) == "Security Digest <onboarding@resend.dev>"


def test_from_field_respects_explicit_name_email_override():
    os.environ["EMAIL_FROM"] = "Fixed Sender <fixed@example.com>"
    assert _from_field("Allie") == "Fixed Sender <fixed@example.com>"
