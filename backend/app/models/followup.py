from sqlalchemy import (
    Column,
    Integer,
    Date,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class FollowUp(Base):
    __tablename__ = "followups"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    interaction_id = Column(
        Integer,
        ForeignKey("interactions.id"),
        nullable=False
    )

    followup_date = Column(
        Date,
        nullable=False
    )

    status = Column(
        String(30),
        default="Pending"
    )

    notes = Column(
        String(500),
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    interaction = relationship(
        "Interaction",
        back_populates="followups"
    )

    def __repr__(self):
        return f"<FollowUp {self.id}>"
