export const capitalize = (text = "") => {
  return text.charAt(0).toUpperCase() + text.slice(1);
};

export const truncateText = (text = "", length = 100) => {
  if (text.length <= length) return text;
  return text.substring(0, length) + "...";
};

export const formatDoctorName = (name = "") => {
  if (!name) return "";

  if (name.startsWith("Dr.")) return name;

  return `Dr. ${name}`;
};

export const generateInteractionTitle = (interaction) => {
  return `${interaction.hcpName} - ${interaction.topic}`;
};

export const formatAttendees = (count) => {
  if (!count) return "0 Attendees";

  return `${count} Attendee${count > 1 ? "s" : ""}`;
};
