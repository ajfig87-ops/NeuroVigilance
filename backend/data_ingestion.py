import os
from api.redaction_service import RedactionService

class DataIngestion:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.redactor = RedactionService()

    def read_input(self):
        if not os.path.exist(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        with open(self.input_path, 'r', encoding='utf-8') as file:
            file.write(redacted_text)

    def process(self):
        raw_text = self.read_input()
        redacted_text = self.redactor.redact(raw_text)
        self.write_output(redacted_text)
        print(f"Redacted content written to: {self.output_path}")