from fastapi import APIRouter

from app.api.routes.chat import router as chat_router
from app.api.routes.interaction import router as interaction_router
from app.api.routes.hcp import router as hcp_router
from app.api.routes.followup import router as followup_router

api_router = APIRouter()

# AI Chat Routes
api_router.include_router(
    chat_router,
    prefix="/chat",
    tags=["AI Chat"]
)

# Interaction Routes
api_router.include_router(
    interaction_router,
    prefix="/interactions",
    tags=["Interactions"]
)

# Healthcare Professional Routes
api_router.include_router(
    hcp_router,
    prefix="/hcps",
    tags=["Healthcare Professionals"]
)

# Follow-up Routes
api_router.include_router(
    followup_router,
    prefix="/followups",
    tags=["Follow Ups"]
)
