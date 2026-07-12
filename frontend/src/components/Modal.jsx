// frontend/src/components/Modal.jsx

import React from "react";
import "./Modal.css";

const Modal = ({
  isOpen,
  title,
  children,
  onClose,
  onConfirm,
  confirmText = "Save",
  cancelText = "Cancel",
  showFooter = true,
  loading = false,
}) => {
  if (!isOpen) return null;

  const handleOverlayClick = (e) => {
    if (e.target.className === "modal-overlay") {
      onClose();
    }
  };

  return (
    <div className="modal-overlay" onClick={handleOverlayClick}>
      <div className="modal-container">

        {/* Header */}
        <div className="modal-header">
          <h2>{title}</h2>

          <button
            className="modal-close-btn"
            onClick={onClose}
          >
            ×
          </button>
        </div>

        {/* Body */}
        <div className="modal-body">
          {children}
        </div>

        {/* Footer */}
        {showFooter && (
          <div className="modal-footer">

            <button
              className="cancel-btn"
              onClick={onClose}
              disabled={loading}
            >
              {cancelText}
            </button>

            <button
              className="confirm-btn"
              onClick={onConfirm}
              disabled={loading}
            >
              {loading ? "Please wait..." : confirmText}
            </button>

          </div>
        )}

      </div>
    </div>
  );
};

export default Modal;
