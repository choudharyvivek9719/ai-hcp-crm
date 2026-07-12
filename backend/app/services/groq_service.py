import json
from typing import Dict, Any

from groq import Groq

from app.core.config import GROQ_API_KEY


class GroqService:
    """
    Wrapper class for communicating with the Groq LLM.
    """

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = "gemma2-9b-it"

    def chat(self, prompt: str) -> str:
        """
        Generic chat completion.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI assistant for a Healthcare CRM. "
                        "Respond clearly and accurately."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content

    def extract_interaction(self, conversation: str) -> Dict[str, Any]:
        """
        Extract structured interaction details from
        natural language.
        """

        prompt = f"""
You are an AI assistant for a Healthcare CRM.

Extract the following fields from the conversation.

Return ONLY valid JSON.

Fields:

representative_name

hcp_name

speciality

hospital

topic

interaction_date

interaction_time

attendees

summary

follow_up_date

Conversation:

{conversation}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0,
        )

        text = response.choices[0].message.content

        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {
                "error": "Failed to parse LLM response",
                "raw_response": text,
            }

    def summarize_interaction(self, text: str) -> str:
        """
        Generate a concise interaction summary.
        """

        prompt = f"""
Summarize the following HCP interaction
in fewer than 100 words.

{text}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.3,
        )

        return response.choices[0].message.content

    def detect_intent(self, user_input: str) -> str:
        """
        Detect which CRM action the user wants.
        """

        prompt = f"""
Classify the user's request into ONE of these intents.

log_interaction

edit_interaction

search_hcp

schedule_followup

interaction_summary

User Input:

{user_input}

Return ONLY the intent name.
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0,
        )

        return response.choices[0].message.content.strip()

    def generate_followup_message(
        self,
        doctor_name: str,
        topic: str,
    ) -> str:
        """
        Generate a professional follow-up message.
        """

        prompt = f"""
Write a professional follow-up message
for Dr. {doctor_name} regarding

{topic}

Keep it under 80 words.
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.5,
        )

        return response.choices[0].message.content


groq_service = GroqService()
