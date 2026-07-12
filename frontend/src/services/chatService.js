// src/services/chatService.js

import api from "./api";

export const sendMessage = async (message) => {
    const response = await api.post("/chat", {
        message,
    });

    return response.data;
};

export const summarizeInteraction = async (interactionId) => {
    const response = await api.post("/chat/summary", {
        interaction_id: interactionId,
    });

    return response.data;
};
