import re

class RedactionService:
    def __init__(self):
        self.patterns = {
            "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"),
            "phone": re.compile(r"(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})"),
            "credit_card": re.compile(r"\b(?:\d[ -]*?){13,16}\b")
        }


    def redact(self, text):
        redacted_text = text
        for label, pattern in self.patterns.items():
            redacted_text = pattern.sub(f"[REDACTED_{label.upper()}]", redacted_text)
        return redacted_text

