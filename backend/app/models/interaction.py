from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Time,
    ForeignKey,
    Text,
    DateTime
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    representative_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    hcp_id = Column(
        Integer,
        ForeignKey("hcps.id"),
        nullable=False
    )

    topic = Column(
        String(255),
        nullable=False
    )

    interaction_date = Column(
        Date,
        nullable=False
    )

    interaction_time = Column(
        Time,
        nullable=False
    )

    attendees = Column(
        Integer,
        default=1
    )

    summary = Column(
        Text,
        nullable=True
    )

    follow_up_date = Column(
        Date,
        nullable=True
    )

    status = Column(
        String(50),
        default="Completed"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    representative = relationship(
        "User",
        back_populates="interactions"
    )

    hcp = relationship(
        "HCP",
        back_populates="interactions"
    )

    followups = relationship(
        "FollowUp",
        back_populates="interaction",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Interaction {self.id}>"
