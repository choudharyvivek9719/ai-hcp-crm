import React from "react";
import "./Navbar.css";

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <div className="logo">
          🏥 <span>AI HCP CRM</span>
        </div>
      </div>

      <div className="navbar-center">
        <input
          type="text"
          placeholder="Search HCP, Hospital, Interaction..."
          className="search-box"
        />
      </div>

      <div className="navbar-right">
        <button className="notification-btn">
          🔔
        </button>

        <div className="user-profile">
          <div className="avatar">
            VC
          </div>

          <div className="user-info">
            <span className="user-name">
              Vivek Choudhary
            </span>

            <span className="user-role">
              Sales Representative
            </span>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
