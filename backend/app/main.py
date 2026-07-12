from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router

app = FastAPI(
    title="AI First Healthcare CRM",
    description="AI-powered CRM for Healthcare Professionals using LangGraph and Groq",
    version="1.0.0",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all API routes
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {
        "status": "success",
        "message": "AI First Healthcare CRM Backend Running 🚀"
    }
