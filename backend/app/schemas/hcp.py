from pydantic import BaseModel
from typing import Optional


class HCPBase(BaseModel):
    doctor_name: str
    speciality: str
    hospital: str
    city: str
    phone: Optional[str] = None


class HCPCreate(HCPBase):
    pass


class HCPUpdate(BaseModel):
    doctor_name: Optional[str] = None
    speciality: Optional[str] = None
    hospital: Optional[str] = None
    city: Optional[str] = None
    phone: Optional[str] = None


class HCPResponse(HCPBase):
    id: int

    class Config:
        from_attributes = True
