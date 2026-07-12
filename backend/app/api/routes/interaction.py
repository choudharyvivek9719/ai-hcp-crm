from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.interaction import Interaction
from app.schemas.interaction import (
    InteractionCreate,
    InteractionResponse,
)

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"]
)


@router.post(
    "/",
    response_model=InteractionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_interaction(
    interaction: InteractionCreate,
    db: Session = Depends(get_db),
):
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


@router.get(
    "/",
    response_model=list[InteractionResponse],
)
def get_all_interactions(
    db: Session = Depends(get_db),
):
    """
    Get all interactions.
    """

    interactions = (
        db.query(Interaction)
        .order_by(Interaction.id.desc())
        .all()
    )

    return interactions


@router.get(
    "/{interaction_id}",
    response_model=InteractionResponse,
)
def get_interaction(
    interaction_id: int,
    db: Session = Depends(get_db),
):
    """
    Get interaction by ID.
    """

    interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if interaction is None:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found",
        )

    return interaction


@router.put(
    "/{interaction_id}",
    response_model=InteractionResponse,
)
def update_interaction(
    interaction_id: int,
    interaction: InteractionCreate,
    db: Session = Depends(get_db),
):
    """
    Update an existing interaction.
    """

    db_interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if db_interaction is None:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found",
        )

    db_interaction.representative_id = interaction.representative_id
    db_interaction.hcp_id = interaction.hcp_id
    db_interaction.topic = interaction.topic
    db_interaction.interaction_date = interaction.interaction_date
    db_interaction.interaction_time = interaction.interaction_time
    db_interaction.attendees = interaction.attendees
    db_interaction.summary = interaction.summary
    db_interaction.next_followup = interaction.next_followup

    db.commit()
    db.refresh(db_interaction)

    return db_interaction


@router.delete(
    "/{interaction_id}",
    status_code=status.HTTP_200_OK,
)
def delete_interaction(
    interaction_id: int,
    db: Session = Depends(get_db),
):
    """
    Delete an interaction.
    """

    interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if interaction is None:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found",
        )

    db.delete(interaction)
    db.commit()

    return {
        "message": "Interaction deleted successfully."
    }


@router.get(
    "/hcp/{hcp_id}",
    response_model=list[InteractionResponse],
)
def get_hcp_interactions(
    hcp_id: int,
    db: Session = Depends(get_db),
):
    """
    Get all interactions for a specific HCP.
    """

    interactions = (
        db.query(Interaction)
        .filter(Interaction.hcp_id == hcp_id)
        .order_by(Interaction.interaction_date.desc())
        .all()
    )

    return interactions
