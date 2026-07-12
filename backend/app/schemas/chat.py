from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str
    extracted_data: Optional[dict] = None
    missing_fields: Optional[list[str]] = None
