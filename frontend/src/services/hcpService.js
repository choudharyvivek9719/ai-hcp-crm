// src/services/hcpService.js

import api from "./api";

export const getAllHCPs = async () => {
    const response = await api.get("/hcp");
    return response.data;
};

export const getHCPById = async (id) => {
    const response = await api.get(`/hcp/${id}`);
    return response.data;
};

export const searchHCP = async (keyword) => {
    const response = await api.get(`/hcp/search?query=${keyword}`);
    return response.data;
};

export const createHCP = async (data) => {
    const response = await api.post("/hcp", data);
    return response.data;
};

export const updateHCP = async (id, data) => {
    const response = await api.put(`/hcp/${id}`, data);
    return response.data;
};

export const deleteHCP = async (id) => {
    const response = await api.delete(`/hcp/${id}`);
    return response.data;
};
