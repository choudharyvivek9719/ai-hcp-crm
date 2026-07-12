from pydantic import BaseModel
from datetime import date, time
from typing import Optional


class InteractionBase(BaseModel):
    representative_id: int
    hcp_id: int
    topic: str
    interaction_date: date
    interaction_time: time
    attendees: int
    summary: str
    next_followup: Optional[date] = None


class InteractionCreate(InteractionBase):
    pass


class InteractionUpdate(BaseModel):
    topic: Optional[str] = None
    interaction_date: Optional[date] = None
    interaction_time: Optional[time] = None
    attendees: Optional[int] = None
    summary: Optional[str] = None
    next_followup: Optional[date] = None


class InteractionResponse(InteractionBase):
    id: int

    class Config:
        from_attributes = True
