import { useState } from "react";
import axios from "axios";

const API_URL = "http://localhost:8000/chat";

export default function useChat() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async (message) => {
    if (!message.trim()) return;

    const userMessage = {
      sender: "user",
      text: message,
      timestamp: new Date().toLocaleTimeString(),
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {
      const response = await axios.post(API_URL, {
        message: message,
      });

      const aiMessage = {
        sender: "assistant",
        text: response.data.response,
        timestamp: new Date().toLocaleTimeString(),
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      const errorMessage = {
        sender: "assistant",
        text: "Unable to connect to AI Assistant.",
        timestamp: new Date().toLocaleTimeString(),
      };

      setMessages((prev) => [...prev, errorMessage]);

      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const clearChat = () => {
    setMessages([]);
  };

  return {
    messages,
    loading,
    sendMessage,
    clearChat,
  };
}
