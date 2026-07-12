from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)

    doctor_name = Column(String(150), nullable=False)

    speciality = Column(String(100), nullable=False)

    hospital = Column(String(150), nullable=False)

    city = Column(String(100), nullable=True)

    phone = Column(String(25), nullable=True)

    email = Column(String(120), nullable=True)

    interactions = relationship(
        "Interaction",
        back_populates="hcp",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<HCP {self.doctor_name}>"
