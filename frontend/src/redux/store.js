import { configureStore } from "@reduxjs/toolkit";

import interactionReducer from "./interactionSlice";
import chatReducer from "./chatSlice";
import hcpReducer from "./hcpSlice";

export const store = configureStore({
  reducer: {
    interaction: interactionReducer,
    chat: chatReducer,
    hcp: hcpReducer,
  },

  devTools: true,
});

export default store;
