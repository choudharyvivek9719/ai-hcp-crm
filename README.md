# 🏥 AI-First Healthcare CRM (HCP Interaction Management)

An AI-powered Customer Relationship Management (CRM) system designed for Healthcare Professionals that enables pharmaceutical field representatives to log interactions using either a structured form or an AI conversational assistant.

The application leverages LangGraph to orchestrate AI workflows and Groq's Gemma2-9B-IT LLM to extract structured information, validate user input, summarise conversations, and execute CRM-related actions.

---

# 📌 Features

- 🤖 AI-powered conversational interaction logging
- 📝 Structured interaction form
- ✏️ Edit previously logged interactions
- 🔍 Search Healthcare Professionals (HCPs)
- 📅 Schedule follow-up meetings
- 📄 AI-generated interaction summaries
- 💬 Multi-turn conversations using LangGraph
- 🗄 PostgreSQL/MySQL database support
- ⚡ FastAPI backend
- ⚛ React + Redux frontend
- 🎨 Google Inter Font

---

# 🏗 Project Architecture

```
                React + Redux
                      │
                      ▼
                FastAPI Backend
                      │
                      ▼
               LangGraph Agent
                      │
        ┌─────────────┼──────────────┐
        ▼             ▼              ▼
 Intent Detection   Validation   Tool Execution
        │             │              │
        └─────────────┼──────────────┘
                      ▼
               PostgreSQL Database
```

---

# 🛠 Technology Stack

## Frontend

- React.js
- Redux Toolkit
- Axios
- Google Inter Font

## Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic

## AI

- LangGraph
- LangChain
- Groq API
- Gemma2-9B-IT
- Llama-3.3-70B-Versatile (Optional)

## Database

- PostgreSQL
- MySQL (Optional)

---

# 📂 Project Structure

```
ai-hcp-crm/

│

├── frontend/

│   ├── src/

│   ├── components/

│   ├── pages/

│   ├── redux/

│   └── services/

│

├── backend/

│   ├── app/

│   │

│   ├── api/

│   ├── graph/

│   ├── crud/

│   ├── models/

│   ├── schemas/

│   ├── database/

│   ├── services/

│   └── main.py

│

├── README.md

├── .env.example

└── requirements.txt
```

---

# 🤖 LangGraph Agent

The LangGraph agent manages the complete AI workflow.

Workflow:

1. Receive user input
2. Detect user intent
3. Extract interaction details
4. Validate extracted fields
5. Ask follow-up questions if required
6. Execute the appropriate CRM tool
7. Save interaction
8. Return response

---

# 🧰 LangGraph Tools

## 1. Log Interaction

Creates a new HCP interaction.

Example:

> "I met Dr Sharma today at Apollo Hospital regarding Diabetes Therapy."

The AI extracts:

- HCP Name
- Topic
- Hospital
- Date
- Time
- Summary
- Attendees

and stores the interaction in the database.

---

## 2. Edit Interaction

Updates previously logged interaction details.

Example:

> "Change attendees from 5 to 8."

---

## 3. Search HCP

Search Healthcare Professionals using filters such as:

- Name
- Hospital
- Specialty
- City

---

## 4. Schedule Follow-up

Schedules the next meeting with the HCP.

---

## 5. Interaction Summary

Uses the LLM to generate concise meeting summaries.

---

# 💬 Example Conversation

User:

```
I met Dr. Sharma today at Apollo Hospital.

We discussed our new diabetes medicine.

There were six attendees.
```

AI:

```
I extracted the following information.

Doctor:
Dr. Sharma

Hospital:
Apollo Hospital

Topic:
Diabetes Medicine

Attendees:
6

One detail is missing.

What time did the meeting occur?
```

---

# 🗄 Database Tables

## Users

- id
- name
- email
- territory

## HCP

- id
- doctor_name
- speciality
- hospital
- city

## Interactions

- id
- representative_id
- hcp_id
- topic
- interaction_date
- interaction_time
- attendees
- summary
- follow_up

## FollowUps

- id
- interaction_id
- followup_date
- status

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/ai-hcp-crm.git

cd ai-hcp-crm
```

---

# Backend Setup

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment

Create `.env`

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/hcpcrm

GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# Start Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

---

# Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /chat | AI Conversation |
| POST | /interaction | Create Interaction |
| GET | /interaction | Get All Interactions |
| PUT | /interaction/{id} | Edit Interaction |
| DELETE | /interaction/{id} | Delete Interaction |
| GET | /hcp | Search HCP |

---

# Future Improvements

- Voice-to-Text interaction logging
- OCR support for visiting cards
- Calendar integration
- Email reminders
- Analytics dashboard
- AI meeting recommendations
- Role-based authentication
- Multi-agent workflows

---

# Author

Vivek Choudhary

AI-First Healthcare CRM using LangGraph, FastAPI, React, Redux, Groq LLM, and PostgreSQL.

---

# License

This project is developed for educational and assessment purposes.
