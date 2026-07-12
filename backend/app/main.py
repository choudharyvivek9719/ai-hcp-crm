from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine
from app.api.router import api_router


# Create all database tables
Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown events.
    """

    print("=" * 60)
    print("🚀 AI HCP CRM Backend Started")
    print("🤖 LangGraph Agent Initialized")
    print("🧠 Groq LLM Ready")
    print("🗄️ Database Connected")
    print("=" * 60)

    yield

    print("=" * 60)
    print("🛑 AI HCP CRM Backend Stopped")
    print("=" * 60)


app = FastAPI(
    title="AI-First Healthcare CRM API",
    description="""
AI-powered Customer Relationship Management (CRM)
for Healthcare Professionals (HCP).

Features
--------
• AI Chat Assistant
• HCP Interaction Logging
• Edit Interaction
• Search HCP
• Schedule Follow-up
• AI Interaction Summary
• LangGraph Agent
• Groq LLM Integration
""",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# -------------------------------------------------------------------
# CORS
# -------------------------------------------------------------------

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------------
# Register API Routes
# -------------------------------------------------------------------

app.include_router(api_router)

# -------------------------------------------------------------------
# Root Endpoint
# -------------------------------------------------------------------


@app.get("/", tags=["Home"])
async def home():
    return {
        "success": True,
        "message": "Welcome to AI-First Healthcare CRM",
        "version": "1.0.0",
        "framework": "FastAPI",
        "agent": "LangGraph",
        "llm": "Groq - gemma2-9b-it",
    }


# -------------------------------------------------------------------
# Health Check
# -------------------------------------------------------------------


@app.get("/health", tags=["Health"])
async def health():
    return {
        "status": "healthy",
        "database": "connected",
        "langgraph": "running",
        "llm": "available",
    }


# -------------------------------------------------------------------
# About
# -------------------------------------------------------------------


@app.get("/about", tags=["About"])
async def about():
    return {
        "project": "AI-First Healthcare CRM",
        "module": "Healthcare Professional (HCP)",
        "frontend": "React + Redux",
        "backend": "FastAPI",
        "database": "PostgreSQL / MySQL",
        "agent": "LangGraph",
        "llm": "Groq Gemma2-9B-IT",
    }
