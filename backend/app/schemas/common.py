from pydantic import BaseModel
from datetime import datetime


class APIResponse(BaseModel):
    success: bool = True
    message: str


class ErrorResponse(BaseModel):
    success: bool = False
    message: str


class Pagination(BaseModel):
    page: int = 1
    page_size: int = 10
    total: int = 0


class TimestampMixin(BaseModel):
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
