// src/services/interactionService.js

import api from "./api";

export const getInteractions = async () => {
    const response = await api.get("/interaction");
    return response.data;
};

export const getInteractionById = async (id) => {
    const response = await api.get(`/interaction/${id}`);
    return response.data;
};

export const createInteraction = async (data) => {
    const response = await api.post("/interaction", data);
    return response.data;
};

export const updateInteraction = async (id, data) => {
    const response = await api.put(`/interaction/${id}`, data);
    return response.data;
};

export const deleteInteraction = async (id) => {
    const response = await api.delete(`/interaction/${id}`);
    return response.data;
};
