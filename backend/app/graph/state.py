from typing import TypedDict, Optional, List


class InteractionState(TypedDict):
    """
    Shared state used by LangGraph.
    Every node in the graph reads and updates this state.
    """

    # ==========================
    # Raw User Input
    # ==========================
    user_input: str

    # ==========================
    # Intent
    # ==========================
    intent: Optional[str]

    # ==========================
    # Representative Details
    # ==========================
    representative: Optional[str]

    # ==========================
    # HCP Details
    # ==========================
    hcp_name: Optional[str]

    speciality: Optional[str]

    hospital: Optional[str]

    city: Optional[str]

    # ==========================
    # Interaction Details
    # ==========================
    topic: Optional[str]

    interaction_date: Optional[str]

    interaction_time: Optional[str]

    attendees: Optional[int]

    summary: Optional[str]

    followup: Optional[str]

    # ==========================
    # Edit Interaction
    # ==========================
    interaction_id: Optional[int]

    edit_field: Optional[str]

    edit_value: Optional[str]

    # ==========================
    # Search Filters
    # ==========================
    search_speciality: Optional[str]

    search_city: Optional[str]

    # ==========================
    # Validation
    # ==========================
    missing_fields: List[str]

    completed: bool

    # ==========================
    # Tool Output
    # ==========================
    tool_name: Optional[str]

    tool_result: Optional[dict]

    response: Optional[str]
