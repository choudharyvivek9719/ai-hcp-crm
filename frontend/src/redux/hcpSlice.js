import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../services/api";

/* ===========================
   Fetch All HCPs
=========================== */

export const fetchHCPs = createAsyncThunk(
  "hcp/fetchHCPs",
  async (_, thunkAPI) => {
    try {
      const response = await api.get("/hcp");
      return response.data;
    } catch (error) {
      return thunkAPI.rejectWithValue(
        error.response?.data?.detail || "Failed to fetch HCPs"
      );
    }
  }
);

/* ===========================
   Search HCP
=========================== */

export const searchHCP = createAsyncThunk(
  "hcp/searchHCP",
  async (searchText, thunkAPI) => {
    try {
      const response = await api.get(`/hcp/search?query=${searchText}`);
      return response.data;
    } catch (error) {
      return thunkAPI.rejectWithValue(
        error.response?.data?.detail || "Search failed"
      );
    }
  }
);

/* ===========================
   Create HCP
=========================== */

export const createHCP = createAsyncThunk(
  "hcp/createHCP",
  async (hcpData, thunkAPI) => {
    try {
      const response = await api.post("/hcp", hcpData);
      return response.data;
    } catch (error) {
      return thunkAPI.rejectWithValue(
        error.response?.data?.detail || "Unable to create HCP"
      );
    }
  }
);

/* ===========================
   Update HCP
=========================== */

export const updateHCP = createAsyncThunk(
  "hcp/updateHCP",
  async ({ id, data }, thunkAPI) => {
    try {
      const response = await api.put(`/hcp/${id}`, data);
      return response.data;
    } catch (error) {
      return thunkAPI.rejectWithValue(
        error.response?.data?.detail || "Unable to update HCP"
      );
    }
  }
);

/* ===========================
   Delete HCP
=========================== */

export const deleteHCP = createAsyncThunk(
  "hcp/deleteHCP",
  async (id, thunkAPI) => {
    try {
      await api.delete(`/hcp/${id}`);
      return id;
    } catch (error) {
      return thunkAPI.rejectWithValue(
        error.response?.data?.detail || "Unable to delete HCP"
      );
    }
  }
);

/* ===========================
   Initial State
=========================== */

const initialState = {
  hcps: [],
  selectedHCP: null,
  loading: false,
  success: false,
  error: null,
};

/* ===========================
   Slice
=========================== */

const hcpSlice = createSlice({
  name: "hcp",

  initialState,

  reducers: {
    clearError: (state) => {
      state.error = null;
    },

    clearSuccess: (state) => {
      state.success = false;
    },

    setSelectedHCP: (state, action) => {
      state.selectedHCP = action.payload;
    },

    clearSelectedHCP: (state) => {
      state.selectedHCP = null;
    },
  },

  extraReducers: (builder) => {
    builder

      // Fetch HCPs
      .addCase(fetchHCPs.pending, (state) => {
        state.loading = true;
      })

      .addCase(fetchHCPs.fulfilled, (state, action) => {
        state.loading = false;
        state.hcps = action.payload;
      })

      .addCase(fetchHCPs.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })

      // Search HCP
      .addCase(searchHCP.pending, (state) => {
        state.loading = true;
      })

      .addCase(searchHCP.fulfilled, (state, action) => {
        state.loading = false;
        state.hcps = action.payload;
      })

      .addCase(searchHCP.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })

      // Create
      .addCase(createHCP.pending, (state) => {
        state.loading = true;
      })

      .addCase(createHCP.fulfilled, (state, action) => {
        state.loading = false;
        state.success = true;
        state.hcps.push(action.payload);
      })

      .addCase(createHCP.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })

      // Update
      .addCase(updateHCP.pending, (state) => {
        state.loading = true;
      })

      .addCase(updateHCP.fulfilled, (state, action) => {
        state.loading = false;
        state.success = true;

        const index = state.hcps.findIndex(
          (hcp) => hcp.id === action.payload.id
        );

        if (index !== -1) {
          state.hcps[index] = action.payload;
        }

        if (
          state.selectedHCP &&
          state.selectedHCP.id === action.payload.id
        ) {
          state.selectedHCP = action.payload;
        }
      })

      .addCase(updateHCP.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })

      // Delete
      .addCase(deleteHCP.pending, (state) => {
        state.loading = true;
      })

      .addCase(deleteHCP.fulfilled, (state, action) => {
        state.loading = false;
        state.success = true;

        state.hcps = state.hcps.filter(
          (hcp) => hcp.id !== action.payload
        );
      })

      .addCase(deleteHCP.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export const {
  clearError,
  clearSuccess,
  setSelectedHCP,
  clearSelectedHCP,
} = hcpSlice.actions;

export default hcpSlice.reducer;
