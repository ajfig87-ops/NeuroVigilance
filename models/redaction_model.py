import re

try:
    import spacy
    SPACY_AVAILABLE = True
    nlp = spacy.load("en_core_web_sm")
except ImportError:
    SPACY_AVAILABLE = False


class RedactionModel:
    def __init__(self):
        self.patterns = {
            "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
            "name": re.compile(r"\b([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)\b")
        }
    
    def predict(self, text: str) -> str:
        redacted_text = text

        for label, pattern in self.patterns.items():
            redacted_text = pattern.sub(f"[REDACTED_{label.upper()}]", redacted_text)
        
        if SPACY_AVAILABLE:
            doc = nlp(redacted_text)
            for ent in doc.ents:
                if ent.label_ in ["PERSON", "GPE", "ORG"]:
                    redacted_text = redacted_text.replace(ent.text, f"[REDACTED_{ent.label_}]")
    
        return redacted_text