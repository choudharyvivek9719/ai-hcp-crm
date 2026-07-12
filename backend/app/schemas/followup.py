from pydantic import BaseModel
from datetime import date
from typing import Optional


class FollowUpBase(BaseModel):
    interaction_id: int
    followup_date: date
    status: str


class FollowUpCreate(FollowUpBase):
    pass


class FollowUpUpdate(BaseModel):
    followup_date: Optional[date] = None
    status: Optional[str] = None


class FollowUpResponse(FollowUpBase):
    id: int

    class Config:
        from_attributes = True
