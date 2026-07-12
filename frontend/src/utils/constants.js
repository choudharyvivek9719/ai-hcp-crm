// API Configuration
export const API_BASE_URL = "http://localhost:8000";

// Interaction Status
export const INTERACTION_STATUS = {
  PENDING: "Pending",
  COMPLETED: "Completed",
  FOLLOW_UP: "Follow Up",
};

// LangGraph Tool Names
export const TOOL_NAMES = {
  LOG: "log_interaction",
  EDIT: "edit_interaction",
  SEARCH: "search_hcp",
  FOLLOWUP: "schedule_followup",
  SUMMARY: "interaction_summary",
};

// Specialities
export const SPECIALITIES = [
  "Cardiology",
  "Neurology",
  "Orthopedics",
  "Dermatology",
  "Pediatrics",
  "General Medicine",
  "Oncology",
  "Gynecology",
  "ENT",
  "Psychiatry",
];

// Chat Placeholder
export const CHAT_PLACEHOLDER =
  "Describe your meeting with the Healthcare Professional...";

// Default Interaction Form
export const DEFAULT_INTERACTION = {
  representative: "",
  hcpName: "",
  speciality: "",
  hospital: "",
  topic: "",
  interactionDate: "",
  interactionTime: "",
  attendees: "",
  summary: "",
  followupDate: "",
};
