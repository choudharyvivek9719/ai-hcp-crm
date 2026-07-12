import os

from dotenv import load_dotenv

from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker

# -----------------------------------------------------
# Load Environment Variables
# -----------------------------------------------------

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in .env")

# -----------------------------------------------------
# SQLAlchemy Engine
# -----------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
)

# -----------------------------------------------------
# Session Factory
# -----------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# -----------------------------------------------------
# Base Class
# -----------------------------------------------------

Base = declarative_base()

# -----------------------------------------------------
# Dependency
# -----------------------------------------------------


def get_db():
    """
    FastAPI dependency for database session.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# -----------------------------------------------------
# Database Initialization
# -----------------------------------------------------


def init_db():
    """
    Create all database tables.
    """

    from app.models.user import User
    from app.models.hcp import HCP
    from app.models.interaction import Interaction
    from app.models.followup import FollowUp

    Base.metadata.create_all(bind=engine)


# -----------------------------------------------------
# Drop Database (Development Only)
# -----------------------------------------------------


def drop_db():
    """
    Drops all tables.
    Use only in development.
    """

    Base.metadata.drop_all(bind=engine)
