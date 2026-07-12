import React from "react";
import "./Loading.css";

const Loading = ({
  message = "AI Assistant is processing...",
  size = "medium",
}) => {
  const spinnerSize = {
    small: "30px",
    medium: "50px",
    large: "70px",
  };

  return (
    <div className="loading-container">
      <div
        className="loading-spinner"
        style={{
          width: spinnerSize[size],
          height: spinnerSize[size],
        }}
      ></div>

      <p className="loading-message">{message}</p>
    </div>
  );
};

export default Loading;
