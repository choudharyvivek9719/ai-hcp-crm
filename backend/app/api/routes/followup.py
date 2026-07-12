from datetime import date
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.followup import FollowUp
from app.models.interaction import Interaction

router = APIRouter(
    prefix="/followups",
    tags=["Follow Ups"]
)


@router.get("/")
def get_all_followups(db: Session = Depends(get_db)):
    """
    Get all follow-up records.
    """

    followups = db.query(FollowUp).all()

    return {
        "success": True,
        "count": len(followups),
        "data": followups
    }


@router.get("/{followup_id}")
def get_followup(
    followup_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a follow-up by ID.
    """

    followup = (
        db.query(FollowUp)
        .filter(FollowUp.id == followup_id)
        .first()
    )

    if not followup:
        raise HTTPException(
            status_code=404,
            detail="Follow-up not found."
        )

    return {
        "success": True,
        "data": followup
    }


@router.get("/interaction/{interaction_id}")
def get_followups_by_interaction(
    interaction_id: int,
    db: Session = Depends(get_db)
):
    """
    Get follow-ups for a specific interaction.
    """

    followups = (
        db.query(FollowUp)
        .filter(FollowUp.interaction_id == interaction_id)
        .all()
    )

    return {
        "success": True,
        "count": len(followups),
        "data": followups
    }


@router.post("/")
def create_followup(
    interaction_id: int,
    followup_date: date,
    status: str = "Pending",
    db: Session = Depends(get_db)
):
    """
    Create a new follow-up.
    """

    interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if not interaction:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found."
        )

    followup = FollowUp(
        interaction_id=interaction_id,
        followup_date=followup_date,
        status=status
    )

    db.add(followup)
    db.commit()
    db.refresh(followup)

    return {
        "success": True,
        "message": "Follow-up created successfully.",
        "data": followup
    }


@router.put("/{followup_id}")
def update_followup(
    followup_id: int,
    followup_date: Optional[date] = None,
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Update a follow-up.
    """

    followup = (
        db.query(FollowUp)
        .filter(FollowUp.id == followup_id)
        .first()
    )

    if not followup:
        raise HTTPException(
            status_code=404,
            detail="Follow-up not found."
        )

    if followup_date:
        followup.followup_date = followup_date

    if status:
        followup.status = status

    db.commit()
    db.refresh(followup)

    return {
        "success": True,
        "message": "Follow-up updated successfully.",
        "data": followup
    }


@router.delete("/{followup_id}")
def delete_followup(
    followup_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a follow-up.
    """

    followup = (
        db.query(FollowUp)
        .filter(FollowUp.id == followup_id)
        .first()
    )

    if not followup:
        raise HTTPException(
            status_code=404,
            detail="Follow-up not found."
        )

    db.delete(followup)
    db.commit()

    return {
        "success": True,
        "message": "Follow-up deleted successfully."
    }


@router.get("/pending/list")
def get_pending_followups(
    db: Session = Depends(get_db)
):
    """
    Get all pending follow-ups.
    """

    followups = (
        db.query(FollowUp)
        .filter(FollowUp.status == "Pending")
        .all()
    )

    return {
        "success": True,
        "count": len(followups),
        "data": followups
    }


@router.get("/today/list")
def get_today_followups(
    db: Session = Depends(get_db)
):
    """
    Get today's follow-ups.
    """

    today = date.today()

    followups = (
        db.query(FollowUp)
        .filter(FollowUp.followup_date == today)
        .all()
    )

    return {
        "success": True,
        "count": len(followups),
        "data": followups
    }
