// frontend/src/pages/Dashboard.jsx

import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  FaUserMd,
  FaComments,
  FaCalendarCheck,
  FaClipboardList,
} from "react-icons/fa";
import { fetchInteractions } from "../redux/interactionSlice";
import { fetchHCPs } from "../redux/hcpSlice";

const Dashboard = () => {
  const dispatch = useDispatch();

  const { interactions } = useSelector((state) => state.interaction);
  const { hcps } = useSelector((state) => state.hcp);

  useEffect(() => {
    dispatch(fetchInteractions());
    dispatch(fetchHCPs());
  }, [dispatch]);

  const totalInteractions = interactions?.length || 0;
  const totalHCPs = hcps?.length || 0;

  const today = new Date().toLocaleDateString();

  return (
    <div
      style={{
        fontFamily: "'Inter', sans-serif",
        background: "#f5f7fb",
        minHeight: "100vh",
        padding: "30px",
      }}
    >
      <h1
        style={{
          fontSize: "32px",
          fontWeight: "700",
          marginBottom: "10px",
        }}
      >
        AI-First Healthcare CRM
      </h1>

      <p
        style={{
          color: "#666",
          marginBottom: "35px",
        }}
      >
        Welcome to your Healthcare Professional Interaction Dashboard
      </p>

      {/* Cards */}

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit,minmax(250px,1fr))",
          gap: "20px",
          marginBottom: "35px",
        }}
      >
        {/* HCP */}

        <div className="dashboard-card">
          <FaUserMd size={35} color="#2563eb" />

          <h2>{totalHCPs}</h2>

          <p>Total HCPs</p>
        </div>

        {/* Interactions */}

        <div className="dashboard-card">
          <FaClipboardList size={35} color="#16a34a" />

          <h2>{totalInteractions}</h2>

          <p>Total Interactions</p>
        </div>

        {/* AI */}

        <div className="dashboard-card">
          <FaComments size={35} color="#9333ea" />

          <h2>AI Ready</h2>

          <p>LangGraph Assistant</p>
        </div>

        {/* Date */}

        <div className="dashboard-card">
          <FaCalendarCheck size={35} color="#ea580c" />

          <h2>{today}</h2>

          <p>Today's Date</p>
        </div>
      </div>

      {/* Recent Interactions */}

      <div
        style={{
          background: "white",
          borderRadius: "12px",
          padding: "20px",
          boxShadow: "0 2px 10px rgba(0,0,0,.08)",
        }}
      >
        <h2
          style={{
            marginBottom: "20px",
          }}
        >
          Recent HCP Interactions
        </h2>

        {interactions?.length === 0 ? (
          <p>No interactions found.</p>
        ) : (
          <table
            style={{
              width: "100%",
              borderCollapse: "collapse",
            }}
          >
            <thead>
              <tr
                style={{
                  background: "#eef3ff",
                }}
              >
                <th style={thStyle}>HCP</th>
                <th style={thStyle}>Topic</th>
                <th style={thStyle}>Date</th>
                <th style={thStyle}>Attendees</th>
              </tr>
            </thead>

            <tbody>
              {interactions.map((interaction) => (
                <tr key={interaction.id}>
                  <td style={tdStyle}>
                    {interaction.hcp_name || "N/A"}
                  </td>

                  <td style={tdStyle}>
                    {interaction.topic}
                  </td>

                  <td style={tdStyle}>
                    {interaction.interaction_date}
                  </td>

                  <td style={tdStyle}>
                    {interaction.attendees}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
};

const thStyle = {
  padding: "12px",
  textAlign: "left",
  borderBottom: "2px solid #ddd",
};

const tdStyle = {
  padding: "12px",
  borderBottom: "1px solid #eee",
};

export default Dashboard;
