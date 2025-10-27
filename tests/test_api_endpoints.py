from fastapi.testclient import TestClient
from api.endpoint_router import app

client = TestClient(app)

def test_redact_endpoint_with_email():
    response = client.post("/redact", json={"text": "Contact me at test@example.com"})
    assert response.status_code == 200
    assert "[REDACTED_EMAIL]" in response.json()["redacted_text"]
    assert "test@example.com" not in response.json()["redacted_text"]

def test_redact_endpoint_with_phone():
    response = client.post("/redact", json={"text": "My number is 123-456-7890"})
    assert response.status_code == 200
    assert "[REDACTED_PHONE]" in response.json()["redacted_text"]
    assert "123-456-7890" not in response.json()["redacted_text"]

def test_redact_endpoint_with_credit_card():
    response = client.post("/redact", json={"text": "Card: 4111 1111 1111 1111"})
    assert response.status_code == 200
    assert "[REDACTED_CREDIT_CARD]" in response.json()["redacted_text"]
    assert "4111 1111 1111 1111" not in response.json()["redacted_text"]

def test_redact_endpoint_multiple_patterns():
    text = "Email: test@foo.com, Phone: 555-555-5555, Card: 1234 5678 9012 3456"
    response = client.post("/redact", json={"text": text})
    result = response.json()["redacted_text"]

    assert "[REDACTED_EMAIL]" in result
    assert "[REDACTED_PHONE]" in result
    assert "[REDACTED_CREDIT_CARD]" in result
