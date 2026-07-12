from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.models.interaction import Interaction
from app.schemas.interaction import InteractionCreate


def create_interaction(
    db: Session,
    interaction: InteractionCreate
) -> Interaction:
    """
    Create a new HCP interaction.
    """

    db_interaction = Interaction(
        representative_id=interaction.representative_id,
        hcp_id=interaction.hcp_id,
        topic=interaction.topic,
        interaction_date=interaction.interaction_date,
        interaction_time=interaction.interaction_time,
        attendees=interaction.attendees,
        summary=interaction.summary,
        next_followup=interaction.next_followup,
    )

    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)

    return db_interaction


def get_interaction(
    db: Session,
    interaction_id: int
) -> Optional[Interaction]:
    """
    Get interaction by ID.
    """

    return (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )


def get_all_interactions(
    db: Session,
    skip: int = 0,
    limit: int = 100
) -> List[Interaction]:
    """
    Return all interactions.
    """

    return (
        db.query(Interaction)
        .order_by(desc(Interaction.id))
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_interactions_by_hcp(
    db: Session,
    hcp_id: int
) -> List[Interaction]:
    """
    Get all interactions for a specific HCP.
    """

    return (
        db.query(Interaction)
        .filter(Interaction.hcp_id == hcp_id)
        .order_by(desc(Interaction.interaction_date))
        .all()
    )


def get_interactions_by_representative(
    db: Session,
    representative_id: int
) -> List[Interaction]:
    """
    Get all interactions created by a representative.
    """

    return (
        db.query(Interaction)
        .filter(
            Interaction.representative_id == representative_id
        )
        .order_by(desc(Interaction.interaction_date))
        .all()
    )


def update_interaction(
    db: Session,
    interaction_id: int,
    updated_data: dict
) -> Optional[Interaction]:
    """
    Update an interaction.
    """

    interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if not interaction:
        return None

    for key, value in updated_data.items():
        if hasattr(interaction, key):
            setattr(interaction, key, value)

    db.commit()
    db.refresh(interaction)

    return interaction


def delete_interaction(
    db: Session,
    interaction_id: int
) -> bool:
    """
    Delete an interaction.
    """

    interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if not interaction:
        return False

    db.delete(interaction)
    db.commit()

    return True


def search_interactions(
    db: Session,
    keyword: str
) -> List[Interaction]:
    """
    Search interactions by topic or summary.
    """

    return (
        db.query(Interaction)
        .filter(
            (Interaction.topic.ilike(f"%{keyword}%")) |
            (Interaction.summary.ilike(f"%{keyword}%"))
        )
        .order_by(desc(Interaction.interaction_date))
        .all()
    )


def get_upcoming_followups(
    db: Session
) -> List[Interaction]:
    """
    Return interactions that have follow-up dates.
    """

    return (
        db.query(Interaction)
        .filter(
            Interaction.next_followup.isnot(None)
        )
        .order_by(Interaction.next_followup)
        .all()
    )


def count_interactions(
    db: Session
) -> int:
    """
    Return total interaction count.
    """

    return db.query(Interaction).count()
