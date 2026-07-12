from datetime import date
from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.followup import FollowUp


def create_followup(
    db: Session,
    interaction_id: int,
    followup_date: date,
    status: str = "Scheduled",
) -> FollowUp:
    """
    Create a new follow-up record.
    """

    followup = FollowUp(
        interaction_id=interaction_id,
        followup_date=followup_date,
        status=status,
    )

    db.add(followup)
    db.commit()
    db.refresh(followup)

    return followup


def get_followup(
    db: Session,
    followup_id: int,
) -> Optional[FollowUp]:
    """
    Get a follow-up by ID.
    """

    return (
        db.query(FollowUp)
        .filter(FollowUp.id == followup_id)
        .first()
    )


def get_all_followups(
    db: Session,
    skip: int = 0,
    limit: int = 100,
) -> List[FollowUp]:
    """
    Get all follow-up records.
    """

    return (
        db.query(FollowUp)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_followups_by_interaction(
    db: Session,
    interaction_id: int,
) -> List[FollowUp]:
    """
    Get all follow-ups for a specific interaction.
    """

    return (
        db.query(FollowUp)
        .filter(FollowUp.interaction_id == interaction_id)
        .all()
    )


def update_followup(
    db: Session,
    followup_id: int,
    followup_date: Optional[date] = None,
    status: Optional[str] = None,
) -> Optional[FollowUp]:
    """
    Update an existing follow-up.
    """

    followup = (
        db.query(FollowUp)
        .filter(FollowUp.id == followup_id)
        .first()
    )

    if not followup:
        return None

    if followup_date is not None:
        followup.followup_date = followup_date

    if status is not None:
        followup.status = status

    db.commit()
    db.refresh(followup)

    return followup


def mark_followup_completed(
    db: Session,
    followup_id: int,
) -> Optional[FollowUp]:
    """
    Mark a follow-up as completed.
    """

    followup = (
        db.query(FollowUp)
        .filter(FollowUp.id == followup_id)
        .first()
    )

    if not followup:
        return None

    followup.status = "Completed"

    db.commit()
    db.refresh(followup)

    return followup


def delete_followup(
    db: Session,
    followup_id: int,
) -> bool:
    """
    Delete a follow-up.
    """

    followup = (
        db.query(FollowUp)
        .filter(FollowUp.id == followup_id)
        .first()
    )

    if not followup:
        return False

    db.delete(followup)
    db.commit()

    return True
