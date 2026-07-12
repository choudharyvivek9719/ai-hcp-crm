// src/services/followupService.js

import api from "./api";

export const getFollowups = async () => {
    const response = await api.get("/followup");
    return response.data;
};

export const createFollowup = async (data) => {
    const response = await api.post("/followup", data);
    return response.data;
};

export const updateFollowup = async (id, data) => {
    const response = await api.put(`/followup/${id}`, data);
    return response.data;
};

export const deleteFollowup = async (id) => {
    const response = await api.delete(`/followup/${id}`);
    return response.data;
};
