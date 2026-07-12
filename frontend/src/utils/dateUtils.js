export const formatDate = (date) => {
  if (!date) return "";

  return new Date(date).toLocaleDateString("en-IN", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
};

export const formatTime = (time) => {
  if (!time) return "";

  return time;
};

export const getTodayDate = () => {
  return new Date().toISOString().split("T")[0];
};

export const getCurrentTime = () => {
  return new Date().toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit",
  });
};
