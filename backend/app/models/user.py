from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(120), unique=True, nullable=False)

    territory = Column(String(100), nullable=True)

    interactions = relationship(
        "Interaction",
        back_populates="representative",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.name}>"
