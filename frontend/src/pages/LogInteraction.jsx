import React, { useState } from "react";
import axios from "axios";

const API_URL = "http://localhost:8000";

const LogInteraction = () => {
  const [mode, setMode] = useState("form");

  const [loading, setLoading] = useState(false);

  const [chatInput, setChatInput] = useState("");

  const [chatHistory, setChatHistory] = useState([]);

  const [formData, setFormData] = useState({
    representative: "",
    hcp_name: "",
    speciality: "",
    hospital: "",
    topic: "",
    interaction_date: "",
    interaction_time: "",
    attendees: "",
    summary: "",
    followup: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const saveInteraction = async () => {
    try {
      setLoading(true);

      await axios.post(`${API_URL}/interaction`, formData);

      alert("Interaction Saved Successfully");

      setFormData({
        representative: "",
        hcp_name: "",
        speciality: "",
        hospital: "",
        topic: "",
        interaction_date: "",
        interaction_time: "",
        attendees: "",
        summary: "",
        followup: "",
      });
    } catch (err) {
      alert("Unable to save interaction.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const sendChat = async () => {
    if (!chatInput.trim()) return;

    const userMessage = {
      sender: "user",
      message: chatInput,
    };

    setChatHistory((prev) => [...prev, userMessage]);

    try {
      setLoading(true);

      const response = await axios.post(`${API_URL}/chat`, {
        message: chatInput,
      });

      const ai = response.data;

      const aiMessage = {
        sender: "ai",
        message: ai.response,
      };

      setChatHistory((prev) => [...prev, aiMessage]);

      if (ai.data) {
        setFormData({
          representative: ai.data.representative || "",
          hcp_name: ai.data.hcp_name || "",
          speciality: ai.data.speciality || "",
          hospital: ai.data.hospital || "",
          topic: ai.data.topic || "",
          interaction_date: ai.data.interaction_date || "",
          interaction_time: ai.data.interaction_time || "",
          attendees: ai.data.attendees || "",
          summary: ai.data.summary || "",
          followup: ai.data.followup || "",
        });
      }

      setChatInput("");
    } catch (error) {
      console.error(error);

      alert("AI service unavailable.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        fontFamily: "Inter",
        padding: "30px",
      }}
    >
      <h2>AI Healthcare CRM</h2>

      <h3>Log HCP Interaction</h3>

      <div
        style={{
          marginTop: 20,
          marginBottom: 20,
        }}
      >
        <button onClick={() => setMode("form")}>
          Structured Form
        </button>

        <button
          style={{ marginLeft: 10 }}
          onClick={() => setMode("chat")}
        >
          AI Assistant
        </button>
      </div>

      {mode === "form" && (
        <div
          style={{
            maxWidth: 700,
          }}
        >
          <input
            name="representative"
            placeholder="Representative Name"
            value={formData.representative}
            onChange={handleChange}
          />

          <br />
          <br />

          <input
            name="hcp_name"
            placeholder="Doctor Name"
            value={formData.hcp_name}
            onChange={handleChange}
          />

          <br />
          <br />

          <input
            name="speciality"
            placeholder="Speciality"
            value={formData.speciality}
            onChange={handleChange}
          />

          <br />
          <br />

          <input
            name="hospital"
            placeholder="Hospital"
            value={formData.hospital}
            onChange={handleChange}
          />

          <br />
          <br />

          <input
            name="topic"
            placeholder="Interaction Topic"
            value={formData.topic}
            onChange={handleChange}
          />

          <br />
          <br />

          <input
            type="date"
            name="interaction_date"
            value={formData.interaction_date}
            onChange={handleChange}
          />

          <br />
          <br />

          <input
            type="time"
            name="interaction_time"
            value={formData.interaction_time}
            onChange={handleChange}
          />

          <br />
          <br />

          <input
            type="number"
            name="attendees"
            placeholder="Attendees"
            value={formData.attendees}
            onChange={handleChange}
          />

          <br />
          <br />

          <textarea
            rows={5}
            name="summary"
            placeholder="Discussion Summary"
            value={formData.summary}
            onChange={handleChange}
          />

          <br />
          <br />

          <input
            type="date"
            name="followup"
            value={formData.followup}
            onChange={handleChange}
          />

          <br />
          <br />

          <button onClick={saveInteraction}>
            {loading ? "Saving..." : "Save Interaction"}
          </button>
        </div>
      )}

      {mode === "chat" && (
        <div
          style={{
            width: "700px",
          }}
        >
          <div
            style={{
              border: "1px solid gray",
              padding: 15,
              height: 400,
              overflowY: "auto",
            }}
          >
            {chatHistory.map((chat, index) => (
              <div
                key={index}
                style={{
                  textAlign:
                    chat.sender === "user"
                      ? "right"
                      : "left",
                  marginBottom: 15,
                }}
              >
                <strong>
                  {chat.sender === "user"
                    ? "You"
                    : "AI Assistant"}
                </strong>

                <div>{chat.message}</div>
              </div>
            ))}
          </div>

          <br />

          <textarea
            rows={3}
            style={{ width: "100%" }}
            placeholder="Describe your interaction..."
            value={chatInput}
            onChange={(e) =>
              setChatInput(e.target.value)
            }
          />

          <br />
          <br />

          <button onClick={sendChat}>
            {loading ? "Thinking..." : "Send"}
          </button>

          <hr />

          <h3>Extracted Information</h3>

          <pre>
            {JSON.stringify(formData, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
};

export default LogInteraction;
