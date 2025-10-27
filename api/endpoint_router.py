from fastapi import FastAPI, Request
from api.redaction_service import RedactionService

app = FastAPI()
redactor = RedactionService()

@app.post("/redact")
async def redact(request: Request):
    data = await request.json()
    original_text = data.get("text", "")
    redacted_output = redactor.redact(original_text)
    return {"redacted_text": redacted_output}