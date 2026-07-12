import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";

import Dashboard from "./pages/Dashboard";
import LogInteraction from "./pages/LogInteraction";
import EditInteraction from "./pages/EditInteraction";
import InteractionHistory from "./pages/InteractionHistory";
import HCPDirectory from "./pages/HCPDirectory";
import ChatAssistant from "./components/ChatAssistant";

function App() {
  return (
    <BrowserRouter>
      <div
        style={{
          display: "flex",
          minHeight: "100vh",
          background: "#f4f6f9",
          fontFamily: "Inter, sans-serif",
        }}
      >
        {/* Sidebar */}
        <Sidebar />

        {/* Main Content */}
        <div
          style={{
            flex: 1,
            display: "flex",
            flexDirection: "column",
          }}
        >
          {/* Top Navbar */}
          <Navbar />

          {/* Page Content */}
          <main
            style={{
              flex: 1,
              padding: "25px",
            }}
          >
            <Routes>
              <Route path="/" element={<Dashboard />} />

              <Route
                path="/log-interaction"
                element={<LogInteraction />}
              />

              <Route
                path="/edit-interaction/:id"
                element={<EditInteraction />}
              />

              <Route
                path="/interaction-history"
                element={<InteractionHistory />}
              />

              <Route
                path="/hcp-directory"
                element={<HCPDirectory />}
              />

              <Route
                path="/ai-assistant"
                element={<ChatAssistant />}
              />
            </Routes>
          </main>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
