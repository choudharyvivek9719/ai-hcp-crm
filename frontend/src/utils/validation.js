export const validateInteraction = (data) => {
  const errors = {};

  if (!data.representative)
    errors.representative = "Representative name is required";

  if (!data.hcpName)
    errors.hcpName = "Doctor name is required";

  if (!data.topic)
    errors.topic = "Meeting topic is required";

  if (!data.interactionDate)
    errors.interactionDate = "Interaction date is required";

  if (!data.interactionTime)
    errors.interactionTime = "Interaction time is required";

  if (!data.summary)
    errors.summary = "Discussion summary is required";

  return errors;
};

export const hasValidationErrors = (errors) => {
  return Object.keys(errors).length > 0;
};
