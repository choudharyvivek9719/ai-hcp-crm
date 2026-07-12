import { NavLink } from "react-router-dom";
import {
  FaHome,
  FaUserMd,
  FaComments,
  FaHistory,
  FaEdit,
  FaCalendarAlt,
} from "react-icons/fa";

const menuItems = [
  {
    title: "Dashboard",
    path: "/",
    icon: <FaHome />,
  },
  {
    title: "Log Interaction",
    path: "/log-interaction",
    icon: <FaComments />,
  },
  {
    title: "Interaction History",
    path: "/history",
    icon: <FaHistory />,
  },
  {
    title: "Edit Interaction",
    path: "/edit-interaction",
    icon: <FaEdit />,
  },
  {
    title: "HCP Directory",
    path: "/hcp-directory",
    icon: <FaUserMd />,
  },
  {
    title: "Follow Ups",
    path: "/follow-ups",
    icon: <FaCalendarAlt />,
  },
];

export default function Sidebar() {
  return (
    <aside className="w-64 min-h-screen bg-slate-900 text-white shadow-lg flex flex-col">
      {/* Logo */}
      <div className="px-6 py-6 border-b border-slate-700">
        <h1 className="text-2xl font-bold tracking-wide">
          AI HCP CRM
        </h1>

        <p className="text-sm text-gray-400 mt-1">
          LangGraph AI Assistant
        </p>
      </div>

      {/* Navigation */}
      <nav className="flex-1 mt-4">
        {menuItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) =>
              `flex items-center gap-3 px-6 py-4 transition-all duration-200 ${
                isActive
                  ? "bg-blue-600 text-white"
                  : "text-gray-300 hover:bg-slate-800 hover:text-white"
              }`
            }
          >
            <span className="text-lg">{item.icon}</span>

            <span className="text-sm font-medium">
              {item.title}
            </span>
          </NavLink>
        ))}
      </nav>

      {/* AI Status */}
      <div className="border-t border-slate-700 p-5">
        <div className="rounded-lg bg-slate-800 p-4">
          <div className="flex items-center gap-2">
            <span className="h-3 w-3 rounded-full bg-green-500"></span>

            <p className="text-sm font-semibold">
              AI Agent Online
            </p>
          </div>

          <p className="mt-2 text-xs text-gray-400">
            LangGraph + Groq (Gemma2-9B-IT)
          </p>
        </div>
      </div>
    </aside>
  );
}
