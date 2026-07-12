from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.graph.graph import graph

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    success: bool
    intent: Optional[str] = None
    response: Optional[str] = None
    data: Optional[dict] = None


@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    AI Chat Endpoint

    Accepts natural language from the sales representative,
    sends it through the LangGraph workflow,
    and returns the AI response.
    """

    try:

        initial_state = {
            "user_input": request.message,
            "representative": "",
            "hcp_name": "",
            "speciality": "",
            "hospital": "",
            "topic": "",
            "interaction_date": "",
            "interaction_time": "",
            "attendees": 0,
            "summary": "",
            "followup": "",
            "missing_fields": [],
            "intent": "",
            "completed": False,
            "response": ""
        }

        result = graph.invoke(initial_state)

        return ChatResponse(
            success=True,
            intent=result.get("intent"),
            response=result.get("response"),
            data=result
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
