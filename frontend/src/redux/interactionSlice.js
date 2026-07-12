import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

// ==========================
// Async Thunks
// ==========================

// Get all interactions
export const fetchInteractions = createAsyncThunk(
  "interaction/fetchInteractions",
  async (_, thunkAPI) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/interaction`);
      return response.data;
    } catch (error) {
      return thunkAPI.rejectWithValue(
        error.response?.data?.detail || "Unable to fetch interactions."
      );
    }
  }
);

// Create interaction
export const createInteraction = createAsyncThunk(
  "interaction/createInteraction",
  async (interactionData, thunkAPI) => {
    try {
      const response = await axios.post(
        `${API_BASE_URL}/interaction`,
        interactionData
      );
      return response.data;
    } catch (error) {
      return thunkAPI.rejectWithValue(
        error.response?.data?.detail || "Unable to create interaction."
      );
    }
  }
);

// Update interaction
export const updateInteraction = createAsyncThunk(
  "interaction/updateInteraction",
  async ({ id, interactionData }, thunkAPI) => {
    try {
      const response = await axios.put(
        `${API_BASE_URL}/interaction/${id}`,
        interactionData
      );
      return response.data;
    } catch (error) {
      return thunkAPI.rejectWithValue(
        error.response?.data?.detail || "Unable to update interaction."
      );
    }
  }
);

// Delete interaction
export const deleteInteraction = createAsyncThunk(
  "interaction/deleteInteraction",
  async (id, thunkAPI) => {
    try {
      await axios.delete(`${API_BASE_URL}/interaction/${id}`);
      return id;
    } catch (error) {
      return thunkAPI.rejectWithValue(
        error.response?.data?.detail || "Unable to delete interaction."
      );
    }
  }
);

// ==========================
// Initial State
// ==========================

const initialState = {
  interactions: [],
  selectedInteraction: null,
  loading: false,
  success: false,
  error: null,
};

// ==========================
// Slice
// ==========================

const interactionSlice = createSlice({
  name: "interaction",

  initialState,

  reducers: {
    clearInteractionError: (state) => {
      state.error = null;
    },

    clearInteractionSuccess: (state) => {
      state.success = false;
    },

    selectInteraction: (state, action) => {
      state.selectedInteraction = action.payload;
    },

    clearSelectedInteraction: (state) => {
      state.selectedInteraction = null;
    },
  },

  extraReducers: (builder) => {
    builder

      // ==========================
      // Fetch
      // ==========================

      .addCase(fetchInteractions.pending, (state) => {
        state.loading = true;
        state.error = null;
      })

      .addCase(fetchInteractions.fulfilled, (state, action) => {
        state.loading = false;
        state.interactions = action.payload;
      })

      .addCase(fetchInteractions.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })

      // ==========================
      // Create
      // ==========================

      .addCase(createInteraction.pending, (state) => {
        state.loading = true;
        state.error = null;
      })

      .addCase(createInteraction.fulfilled, (state, action) => {
        state.loading = false;
        state.success = true;
        state.interactions.unshift(action.payload);
      })

      .addCase(createInteraction.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })

      // ==========================
      // Update
      // ==========================

      .addCase(updateInteraction.pending, (state) => {
        state.loading = true;
      })

      .addCase(updateInteraction.fulfilled, (state, action) => {
        state.loading = false;
        state.success = true;

        const index = state.interactions.findIndex(
          (item) => item.id === action.payload.id
        );

        if (index !== -1) {
          state.interactions[index] = action.payload;
        }

        state.selectedInteraction = action.payload;
      })

      .addCase(updateInteraction.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })

      // ==========================
      // Delete
      // ==========================

      .addCase(deleteInteraction.pending, (state) => {
        state.loading = true;
      })

      .addCase(deleteInteraction.fulfilled, (state, action) => {
        state.loading = false;
        state.success = true;

        state.interactions = state.interactions.filter(
          (interaction) => interaction.id !== action.payload
        );
      })

      .addCase(deleteInteraction.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

// ==========================
// Actions
// ==========================

export const {
  clearInteractionError,
  clearInteractionSuccess,
  selectInteraction,
  clearSelectedInteraction,
} = interactionSlice.actions;

// ==========================
// Reducer
// ==========================

export default interactionSlice.reducer;
