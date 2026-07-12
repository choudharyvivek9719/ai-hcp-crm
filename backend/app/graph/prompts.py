"""
Prompt templates used by the LangGraph AI Agent.

These prompts are responsible for:
1. Intent Detection
2. Interaction Information Extraction
3. Missing Field Questions
4. AI Interaction Summary
5. Edit Interaction Instructions
"""

# ==========================================================
# Intent Detection Prompt
# ==========================================================

INTENT_PROMPT = """
You are an AI assistant for a Healthcare CRM.

Your job is to identify the user's intent.

Possible intents:

1. log_interaction
2. edit_interaction
3. search_hcp
4. schedule_followup
5. summarize_interaction

Return ONLY one intent.

Examples:

User:
I met Dr. Sharma today regarding Diabetes medicine.

Answer:
log_interaction

--------------------------

User:
Change attendees from 5 to 8.

Answer:
edit_interaction

--------------------------

User:
Show all Cardiologists in Delhi.

Answer:
search_hcp

--------------------------

User:
Schedule follow-up next Monday.

Answer:
schedule_followup

--------------------------

User:
Summarize yesterday's meeting.

Answer:
summarize_interaction
"""


# ==========================================================
# Information Extraction Prompt
# ==========================================================

EXTRACTION_PROMPT = """
You are an AI Healthcare CRM Assistant.

Extract the following fields from the user's message.

Fields:

representative_name
hcp_name
speciality
hospital
city
interaction_topic
interaction_date
interaction_time
attendees
discussion_summary
followup_date

Rules:

1. Return ONLY valid JSON.
2. Do NOT explain anything.
3. Missing fields should be null.
4. Date should be YYYY-MM-DD if possible.
5. Time should be HH:MM format if possible.
6. attendees must be an integer.

Example:

User:

I met Dr. Sharma at Apollo Hospital today at 2 PM.
We discussed our new diabetes medicine.
Six doctors attended.
Follow-up next Monday.

Return:

{
  "representative_name": null,
  "hcp_name":"Dr. Sharma",
  "speciality":null,
  "hospital":"Apollo Hospital",
  "city":null,
  "interaction_topic":"Diabetes Medicine",
  "interaction_date":"2026-07-12",
  "interaction_time":"14:00",
  "attendees":6,
  "discussion_summary":"Discussion regarding Diabetes Medicine.",
  "followup_date":"2026-07-20"
}
"""


# ==========================================================
# Validation Prompt
# ==========================================================

VALIDATION_PROMPT = """
Check whether all required CRM fields are available.

Required fields:

representative_name
hcp_name
interaction_topic
interaction_date
interaction_time

Return JSON only.

Example:

{
    "missing_fields":[
        "representative_name",
        "interaction_time"
    ]
}
"""


# ==========================================================
# Missing Information Prompt
# ==========================================================

MISSING_FIELDS_PROMPT = """
You are an AI CRM assistant.

Some required information is missing.

Missing Fields:

{missing_fields}

Ask ONLY for the missing fields.

Rules:

1. Be polite.
2. Ask only one combined question.
3. Keep it short.

Example:

Could you please tell me the meeting time and your representative name?
"""


# ==========================================================
# Interaction Summary Prompt
# ==========================================================

SUMMARY_PROMPT = """
You are a Pharmaceutical CRM Assistant.

Summarize the following interaction.

Requirements:

• Maximum 60 words
• Professional language
• Mention product discussed
• Mention doctor's interest
• Mention follow-up if available

Interaction:

{interaction}
"""


# ==========================================================
# Edit Interaction Prompt
# ==========================================================

EDIT_PROMPT = """
You are an AI CRM assistant.

The user wants to modify an existing interaction.

Determine:

1. Which field should be updated?
2. What is the new value?

Return JSON only.

Example:

User:

Change attendees from 5 to 8.

Return:

{
    "field":"attendees",
    "value":8
}

--------------------------

User:

Update meeting time to 4 PM.

Return:

{
    "field":"interaction_time",
    "value":"16:00"
}
"""


# ==========================================================
# Search HCP Prompt
# ==========================================================

SEARCH_HCP_PROMPT = """
Extract HCP search filters.

Possible filters:

doctor_name
speciality
hospital
city

Return JSON only.

Example:

User:

Show Cardiologists in Mumbai.

Return:

{
    "doctor_name": null,
    "speciality":"Cardiologist",
    "hospital": null,
    "city":"Mumbai"
}
"""


# ==========================================================
# Follow-up Scheduling Prompt
# ==========================================================

FOLLOWUP_PROMPT = """
The user wants to schedule a follow-up.

Extract:

interaction_id
followup_date

Return JSON only.

Example:

User:

Schedule follow-up for interaction 12 on next Friday.

Return:

{
    "interaction_id":12,
    "followup_date":"2026-07-17"
}
"""


# ==========================================================
# Final Confirmation Prompt
# ==========================================================

CONFIRMATION_PROMPT = """
Generate a confirmation message after successfully completing the CRM action.

Examples:

Interaction logged successfully.

Interaction updated successfully.

Follow-up scheduled successfully.

HCP search completed.

Summary generated successfully.
"""
