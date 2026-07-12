import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

const API_URL = "http://localhost:8000/chat";

/*
 * Send user message to FastAPI
 */
export const sendMessage = createAsyncThunk(
  "chat/sendMessage",
  async (message, { rejectWithValue }) => {
    try {
      const response = await axios.post(API_URL, {
        message: message,
      });

      return {
        userMessage: message,
        aiMessage: response.data.response,
      };
    } catch (error) {
      return rejectWithValue(
        error.response?.data?.detail || "Unable to connect to AI server."
      );
    }
  }
);

const initialState = {
  messages: [],
  loading: false,
  error: null,
};

const chatSlice = createSlice({
  name: "chat",

  initialState,

  reducers: {
    addUserMessage: (state, action) => {
      state.messages.push({
        sender: "user",
        text: action.payload,
        timestamp: new Date().toISOString(),
      });
    },

    addAIMessage: (state, action) => {
      state.messages.push({
        sender: "assistant",
        text: action.payload,
        timestamp: new Date().toISOString(),
      });
    },

    clearChat: (state) => {
      state.messages = [];
      state.loading = false;
      state.error = null;
    },

    removeLastMessage: (state) => {
      state.messages.pop();
    },
  },

  extraReducers: (builder) => {
    builder

      .addCase(sendMessage.pending, (state, action) => {
        state.loading = true;
        state.error = null;

        state.messages.push({
          sender: "user",
          text: action.meta.arg,
          timestamp: new Date().toISOString(),
        });
      })

      .addCase(sendMessage.fulfilled, (state, action) => {
        state.loading = false;

        state.messages.push({
          sender: "assistant",
          text: action.payload.aiMessage,
          timestamp: new Date().toISOString(),
        });
      })

      .addCase(sendMessage.rejected, (state, action) => {
        state.loading = false;

        state.error = action.payload;

        state.messages.push({
          sender: "assistant",
          text:
            action.payload ||
            "Something went wrong while contacting the AI.",
          timestamp: new Date().toISOString(),
        });
      });
  },
});

export const {
  addUserMessage,
  addAIMessage,
  clearChat,
  removeLastMessage,
} = chatSlice.actions;

export default chatSlice.reducer;
