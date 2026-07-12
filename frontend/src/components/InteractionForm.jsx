import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { saveInteraction } from "../redux/interactionSlice";

const InteractionForm = () => {
  const dispatch = useDispatch();

  const [formData, setFormData] = useState({
    representative: "",
    hcpName: "",
    speciality: "",
    hospital: "",
    topic: "",
    interactionDate: "",
    interactionTime: "",
    attendees: "",
    summary: "",
    followup: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    dispatch(saveInteraction(formData));

    alert("Interaction Saved Successfully!");

    setFormData({
      representative: "",
      hcpName: "",
      speciality: "",
      hospital: "",
      topic: "",
      interactionDate: "",
      interactionTime: "",
      attendees: "",
      summary: "",
      followup: "",
    });
  };

  return (
    <div
      style={{
        background: "#ffffff",
        borderRadius: "10px",
        padding: "25px",
        boxShadow: "0 2px 10px rgba(0,0,0,.1)",
        fontFamily: "Inter, sans-serif",
      }}
    >
      <h2 style={{ marginBottom: "20px" }}>
        Log HCP Interaction
      </h2>

      <form onSubmit={handleSubmit}>
        <div className="form-grid">

          <div className="form-group">
            <label>Representative Name</label>

            <input
              type="text"
              name="representative"
              value={formData.representative}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>HCP Name</label>

            <input
              type="text"
              name="hcpName"
              value={formData.hcpName}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Speciality</label>

            <input
              type="text"
              name="speciality"
              value={formData.speciality}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Hospital</label>

            <input
              type="text"
              name="hospital"
              value={formData.hospital}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Interaction Topic</label>

            <input
              type="text"
              name="topic"
              value={formData.topic}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Date</label>

            <input
              type="date"
              name="interactionDate"
              value={formData.interactionDate}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Time</label>

            <input
              type="time"
              name="interactionTime"
              value={formData.interactionTime}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Attendees</label>

            <input
              type="number"
              name="attendees"
              value={formData.attendees}
              onChange={handleChange}
            />
          </div>

          <div
            className="form-group"
            style={{ gridColumn: "1 / span 2" }}
          >
            <label>Discussion Summary</label>

            <textarea
              rows="4"
              name="summary"
              value={formData.summary}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Follow-up Date</label>

            <input
              type="date"
              name="followup"
              value={formData.followup}
              onChange={handleChange}
            />
          </div>

        </div>

        <div style={{ marginTop: "20px" }}>
          <button
            type="submit"
            style={{
              padding: "12px 25px",
              border: "none",
              borderRadius: "8px",
              background: "#2563eb",
              color: "#fff",
              cursor: "pointer",
              fontWeight: "600",
            }}
          >
            Save Interaction
          </button>
        </div>
      </form>

      <style>{`
        .form-grid{
          display:grid;
          grid-template-columns:1fr 1fr;
          gap:18px;
        }

        .form-group{
          display:flex;
          flex-direction:column;
        }

        label{
          margin-bottom:8px;
          font-weight:600;
        }

        input,
        textarea{
          padding:12px;
          border:1px solid #d1d5db;
          border-radius:8px;
          outline:none;
          font-size:15px;
        }

        input:focus,
        textarea:focus{
          border-color:#2563eb;
        }

        @media(max-width:768px){
          .form-grid{
            grid-template-columns:1fr;
          }
        }
      `}</style>
    </div>
  );
};

export default InteractionForm;
