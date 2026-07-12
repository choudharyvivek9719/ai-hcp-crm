"""
File: backend/app/graph/tools.py

LangGraph Tools for AI-First Healthcare CRM

These tools are used by the LangGraph agent to perform CRM actions.

Required Assignment Tools:
1. Log Interaction
2. Edit Interaction

Additional Tools:
3. Search HCP
4. Schedule Follow-up
5. Interaction Summary
"""

from langchain_core.tools import tool
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.interaction import Interaction
from app.models.hcp import HCP
from app.models.followup import FollowUp
from app.services.groq_service import llm


# ---------------------------------------------------------
# Helper Function
# ---------------------------------------------------------

def get_db() -> Session:
    return SessionLocal()


# ---------------------------------------------------------
# Tool 1 : Log Interaction
# ---------------------------------------------------------

@tool
def log_interaction(
    representative: str,
    hcp_name: str,
    speciality: str,
    hospital: str,
    topic: str,
    interaction_date: str,
    interaction_time: str,
    attendees: int,
    summary: str,
    followup: str,
):
    """
    Create a new HCP interaction.
    """

    db = get_db()

    try:

        hcp = (
            db.query(HCP)
            .filter(HCP.doctor_name == hcp_name)
            .first()
        )

        if not hcp:

            hcp = HCP(
                doctor_name=hcp_name,
                speciality=speciality,
                hospital=hospital,
            )

            db.add(hcp)
            db.commit()
            db.refresh(hcp)

        interaction = Interaction(
            representative_id=1,
            hcp_id=hcp.id,
            topic=topic,
            interaction_date=interaction_date,
            interaction_time=interaction_time,
            attendees=attendees,
            summary=summary,
            next_followup=followup,
        )

        db.add(interaction)
        db.commit()
        db.refresh(interaction)

        return {
            "success": True,
            "interaction_id": interaction.id,
            "message": "Interaction logged successfully."
        }

    except Exception as e:

        db.rollback()

        return {
            "success": False,
            "error": str(e)
        }

    finally:

        db.close()


# ---------------------------------------------------------
# Tool 2 : Edit Interaction
# ---------------------------------------------------------

@tool
def edit_interaction(
    interaction_id: int,
    field: str,
    value: str,
):
    """
    Edit an existing interaction.
    """

    db = get_db()

    try:

        interaction = (
            db.query(Interaction)
            .filter(Interaction.id == interaction_id)
            .first()
        )

        if interaction is None:

            return {
                "success": False,
                "message": "Interaction not found."
            }

        if hasattr(interaction, field):

            setattr(interaction, field, value)

            db.commit()

            db.refresh(interaction)

            return {
                "success": True,
                "message": f"{field} updated successfully."
            }

        return {
            "success": False,
            "message": "Invalid field."
        }

    except Exception as e:

        db.rollback()

        return {
            "success": False,
            "error": str(e)
        }

    finally:

        db.close()


# ---------------------------------------------------------
# Tool 3 : Search HCP
# ---------------------------------------------------------

@tool
def search_hcp(
    doctor_name: str = "",
    speciality: str = "",
    hospital: str = "",
):
    """
    Search Healthcare Professionals.
    """

    db = get_db()

    try:

        query = db.query(HCP)

        if doctor_name:

            query = query.filter(
                HCP.doctor_name.ilike(f"%{doctor_name}%")
            )

        if speciality:

            query = query.filter(
                HCP.speciality.ilike(f"%{speciality}%")
            )

        if hospital:

            query = query.filter(
                HCP.hospital.ilike(f"%{hospital}%")
            )

        doctors = query.all()

        result = []

        for doctor in doctors:

            result.append(
                {
                    "id": doctor.id,
                    "doctor_name": doctor.doctor_name,
                    "speciality": doctor.speciality,
                    "hospital": doctor.hospital,
                }
            )

        return result

    finally:

        db.close()


# ---------------------------------------------------------
# Tool 4 : Schedule Follow-up
# ---------------------------------------------------------

@tool
def schedule_followup(
    interaction_id: int,
    followup_date: str,
):
    """
    Schedule a follow-up meeting.
    """

    db = get_db()

    try:

        followup = FollowUp(
            interaction_id=interaction_id,
            followup_date=followup_date,
            status="Pending",
        )

        db.add(followup)

        db.commit()

        db.refresh(followup)

        return {
            "success": True,
            "followup_id": followup.id,
            "message": "Follow-up scheduled."
        }

    except Exception as e:

        db.rollback()

        return {
            "success": False,
            "error": str(e)
        }

    finally:

        db.close()


# ---------------------------------------------------------
# Tool 5 : Interaction Summary
# ---------------------------------------------------------

@tool
def summarize_interaction(
    interaction_text: str,
):
    """
    Generate an AI summary of an HCP interaction.
    """

    prompt = f"""
You are a Pharmaceutical CRM Assistant.

Summarize the following interaction in
less than 100 words.

Interaction:

{interaction_text}

Return only the summary.
"""

    response = llm.invoke(prompt)

    return response.content


# ---------------------------------------------------------
# Tool 6 : Get Interaction History
# ---------------------------------------------------------

@tool
def get_interaction_history(
    hcp_name: str,
):
    """
    Retrieve interaction history for a doctor.
    """

    db = get_db()

    try:

        hcp = (
            db.query(HCP)
            .filter(HCP.doctor_name == hcp_name)
            .first()
        )

        if hcp is None:

            return []

        interactions = (
            db.query(Interaction)
            .filter(Interaction.hcp_id == hcp.id)
            .all()
        )

        history = []

        for interaction in interactions:

            history.append(
                {
                    "topic": interaction.topic,
                    "date": str(interaction.interaction_date),
                    "summary": interaction.summary,
                }
            )

        return history

    finally:

        db.close()


# ---------------------------------------------------------
# Export All Tools
# ---------------------------------------------------------

TOOLS = [
    log_interaction,
    edit_interaction,
    search_hcp,
    schedule_followup,
    summarize_interaction,
    get_interaction_history,
]
