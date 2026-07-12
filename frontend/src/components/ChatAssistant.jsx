import React, { useState, useRef, useEffect } from "react";
import axios from "axios";

const API_URL = "http://localhost:8000/chat";

const ChatAssistant = ({ onInteractionExtracted }) => {
  const [messages, setMessages] = useState([
    {
      sender: "assistant",
      text: "Hello! 👋 I'm your AI CRM Assistant.\n\nTell me about your interaction with an HCP, and I'll automatically fill the CRM form.",
    },
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = {
      sender: "user",
      text: input,
    };

    setMessages((prev) => [...prev, userMessage]);

    const question = input;
    setInput("");
    setLoading(true);

    try {
      const response = await axios.post(API_URL, {
        message: question,
      });

      const ai = response.data;

      if (ai.interaction) {
        onInteractionExtracted(ai.interaction);
      }

      setMessages((prev) => [
        ...prev,
        {
          sender: "assistant",
          text: ai.reply || "Interaction processed successfully.",
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          sender: "assistant",
          text: "Something went wrong while contacting the AI backend.",
        },
      ]);
    }

    setLoading(false);
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        height: "700px",
        border: "1px solid #ddd",
        borderRadius: 12,
        overflow: "hidden",
        background: "#fff",
      }}
    >
      <div
        style={{
          padding: 15,
          background: "#2563eb",
          color: "#fff",
          fontWeight: 600,
          fontSize: 18,
        }}
      >
        🤖 AI CRM Assistant
      </div>

      <div
        style={{
          flex: 1,
          overflowY: "auto",
          padding: 20,
          background: "#f7f8fc",
        }}
      >
        {messages.map((msg, index) => (
          <div
            key={index}
            style={{
              display: "flex",
              justifyContent:
                msg.sender === "user" ? "flex-end" : "flex-start",
              marginBottom: 15,
            }}
          >
            <div
              style={{
                maxWidth: "70%",
                padding: "12px 16px",
                borderRadius: 15,
                background:
                  msg.sender === "user" ? "#2563eb" : "#e5e7eb",
                color:
                  msg.sender === "user" ? "#fff" : "#111827",
                whiteSpace: "pre-wrap",
                lineHeight: 1.5,
              }}
            >
              {msg.text}
            </div>
          </div>
        ))}

        {loading && (
          <div
            style={{
              color: "#555",
              marginTop: 10,
            }}
          >
            AI is thinking...
          </div>
        )}

        <div ref={bottomRef}></div>
      </div>

      <div
        style={{
          display: "flex",
          padding: 15,
          borderTop: "1px solid #ddd",
          gap: 10,
        }}
      >
        <input
          type="text"
          placeholder="Describe your interaction..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyPress}
          style={{
            flex: 1,
            padding: 12,
            borderRadius: 8,
            border: "1px solid #ccc",
            outline: "none",
            fontSize: 15,
          }}
        />

        <button
          onClick={sendMessage}
          disabled={loading}
          style={{
            background: "#2563eb",
            color: "#fff",
            border: "none",
            padding: "12px 22px",
            borderRadius: 8,
            cursor: "pointer",
            fontWeight: 600,
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatAssistant;
