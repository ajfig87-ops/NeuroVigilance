import pytest
from api.redaction_service import RedactionService

@pytest.fixture
def redactor():
    return RedactionService()

def test_redact_email(redactor):
    text = "My email is example@example.com"
    result = redactor.redact(text)
    assert "[REDACTED_EMAIL]" in result
    assert "example@example.com" not in result

def test_redact_phone(redactor):
    text = "Call me at 123-456-7890"
    result = redactor.redact(text)
    assert "[REDACTED_PHONE]" in result
    assert "123-456-7890" not in result

def test_redact_credit_card(redactor):
    text = "My card number is 4111 1111 1111 1111"
    result = redactor.redact(text)
    assert "[REDACTED_CREDIT_CARD]" in result
    assert "4111 1111 1111 1111" not in result

def test_redact_multiple_types(redactor):
    text = "Email: foo@bar.com, Phone: (555) 555-5555, Card: 1234 5678 9012 3456"
    result = redactor.redact(text)
    assert "[REDACTED_EMAIL]" in result
    assert "[REDACTED_PHONE]" in result
    assert "[REDACTED_CREDIT_CARD]" in result
