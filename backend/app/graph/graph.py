from langgraph.graph import StateGraph, END

from app.graph.state import InteractionState
from app.graph.nodes import (
    detect_intent,
    extract_information,
    validate_information,
    ask_missing_information,
    update_state,
    execute_tool,
    finish_interaction
)


def validation_router(state: InteractionState):
    """
    Decide the next step after validation.

    If required fields are missing,
    ask the user for more information.

    Otherwise,
    execute the detected tool.
    """

    if len(state["missing_fields"]) > 0:
        return "ask_missing"

    return "execute_tool"


builder = StateGraph(InteractionState)

# ----------------------------------------------------
# Nodes
# ----------------------------------------------------

builder.add_node("detect_intent", detect_intent)

builder.add_node("extract_information", extract_information)

builder.add_node("validate_information", validate_information)

builder.add_node("ask_missing", ask_missing_information)

builder.add_node("update_state", update_state)

builder.add_node("execute_tool", execute_tool)

builder.add_node("finish", finish_interaction)

# ----------------------------------------------------
# Entry Point
# ----------------------------------------------------

builder.set_entry_point("detect_intent")

# ----------------------------------------------------
# Edges
# ----------------------------------------------------

builder.add_edge(
    "detect_intent",
    "extract_information"
)

builder.add_edge(
    "extract_information",
    "validate_information"
)

builder.add_conditional_edges(
    "validate_information",
    validation_router,
    {
        "ask_missing": "ask_missing",
        "execute_tool": "execute_tool"
    }
)

builder.add_edge(
    "ask_missing",
    "update_state"
)

builder.add_edge(
    "update_state",
    "validate_information"
)

builder.add_edge(
    "execute_tool",
    "finish"
)

builder.add_edge(
    "finish",
    END
)

# ----------------------------------------------------
# Compile Graph
# ----------------------------------------------------

graph = builder.compile()
