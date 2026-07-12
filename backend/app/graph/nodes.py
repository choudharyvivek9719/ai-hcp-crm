# backend/app/graph/nodes.py

import json

from app.graph.prompts import (
    INTENT_PROMPT,
    EXTRACTION_PROMPT,
    MISSING_FIELD_PROMPT,
)

from app.services.groq_service import llm

from app.graph.tools import (
    log_interaction,
    edit_interaction,
    search_hcp,
    schedule_followup,
    summarize_interaction,
)


# --------------------------------------------------
# Utility
# --------------------------------------------------

def _safe_json(content: str):
    """
    Parse JSON returned by the LLM.
    """

    try:
        return json.loads(content)
    except Exception:
        return {}


# --------------------------------------------------
# Node 1
# Detect Intent
# --------------------------------------------------

def detect_intent(state):

    prompt = INTENT_PROMPT.format(
        user_input=state["user_input"]
    )

    response = llm.invoke(prompt)

    state["intent"] = response.content.strip().lower()

    return state


# --------------------------------------------------
# Node 2
# Extract Information
# --------------------------------------------------

def extract_information(state):

    prompt = EXTRACTION_PROMPT.format(
        user_input=state["user_input"]
    )

    response = llm.invoke(prompt)

    extracted = _safe_json(response.content)

    state["representative"] = extracted.get(
        "representative",
        ""
    )

    state["hcp_name"] = extracted.get(
        "hcp_name",
        ""
    )

    state["speciality"] = extracted.get(
        "speciality",
        ""
    )

    state["hospital"] = extracted.get(
        "hospital",
        ""
    )

    state["topic"] = extracted.get(
        "topic",
        ""
    )

    state["interaction_date"] = extracted.get(
        "interaction_date",
        ""
    )

    state["interaction_time"] = extracted.get(
        "interaction_time",
        ""
    )

    state["attendees"] = extracted.get(
        "attendees",
        0
    )

    state["summary"] = extracted.get(
        "summary",
        ""
    )

    state["followup"] = extracted.get(
        "followup",
        ""
    )

    return state


# --------------------------------------------------
# Node 3
# Validate Fields
# --------------------------------------------------

def validate(state):

    missing = []

    required = [
        "representative",
        "hcp_name",
        "topic",
        "interaction_date",
        "interaction_time",
        "summary",
    ]

    for field in required:

        value = state.get(field)

        if value is None or value == "" or value == 0:

            missing.append(field)

    state["missing_fields"] = missing

    return state


# --------------------------------------------------
# Node 4
# Ask Missing Information
# --------------------------------------------------

def ask_missing_information(state):

    prompt = MISSING_FIELD_PROMPT.format(
        missing_fields=", ".join(state["missing_fields"])
    )

    response = llm.invoke(prompt)

    state["response"] = response.content

    return state


# --------------------------------------------------
# Node 5
# Execute Tool
# --------------------------------------------------

def execute_tool(state):

    intent = state["intent"]

    # --------------------------------------
    # LOG INTERACTION
    # --------------------------------------

    if intent == "log_interaction":

        result = log_interaction.invoke({

            "representative": state["representative"],

            "hcp_name": state["hcp_name"],

            "speciality": state["speciality"],

            "hospital": state["hospital"],

            "topic": state["topic"],

            "interaction_date": state["interaction_date"],

            "interaction_time": state["interaction_time"],

            "attendees": state["attendees"],

            "summary": state["summary"],

            "followup": state["followup"]

        })

    # --------------------------------------
    # EDIT INTERACTION
    # --------------------------------------

    elif intent == "edit_interaction":

        result = edit_interaction.invoke({

            "interaction_id": 1,

            "field": "summary",

            "value": state["summary"]

        })

    # --------------------------------------
    # SEARCH HCP
    # --------------------------------------

    elif intent == "search_hcp":

        result = search_hcp.invoke({

            "speciality": state["speciality"],

            "hospital": state["hospital"]

        })

    # --------------------------------------
    # FOLLOW-UP
    # --------------------------------------

    elif intent == "schedule_followup":

        result = schedule_followup.invoke({

            "interaction_id": 1,

            "followup_date": state["followup"]

        })

    # --------------------------------------
    # SUMMARY
    # --------------------------------------

    elif intent == "summarize":

        result = summarize_interaction.invoke({

            "interaction_text": state["summary"]

        })

    else:

        result = {

            "status": "error",

            "message": "Unknown intent"

        }

    state["tool_result"] = result

    state["response"] = result

    return state


# --------------------------------------------------
# Node 6
# Finish Workflow
# --------------------------------------------------

def finish(state):

    state["completed"] = True

    return state


# --------------------------------------------------
# Conditional Edge
# --------------------------------------------------

def should_continue(state):

    if len(state["missing_fields"]) == 0:

        return "execute"

    return "ask"
