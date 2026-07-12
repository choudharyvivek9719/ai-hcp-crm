import React from "react";

const InteractionCard = ({
  interaction,
  onEdit,
  onDelete,
  onSummary,
  onView,
}) => {
  if (!interaction) return null;

  return (
    <div
      style={{
        background: "#ffffff",
        borderRadius: "12px",
        padding: "20px",
        marginBottom: "20px",
        boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
        border: "1px solid #e5e7eb",
      }}
    >
      {/* Header */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          marginBottom: "15px",
        }}
      >
        <div>
          <h2
            style={{
              margin: 0,
              fontSize: "20px",
              color: "#111827",
            }}
          >
            {interaction.hcp_name}
          </h2>

          <p
            style={{
              margin: "5px 0",
              color: "#6b7280",
            }}
          >
            {interaction.speciality}
          </p>
        </div>

        <div>
          <span
            style={{
              background: "#2563eb",
              color: "#fff",
              padding: "6px 12px",
              borderRadius: "20px",
              fontSize: "13px",
            }}
          >
            {interaction.interaction_date}
          </span>
        </div>
      </div>

      {/* Details */}

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "12px",
        }}
      >
        <div>
          <strong>Hospital</strong>

          <p>{interaction.hospital}</p>
        </div>

        <div>
          <strong>Representative</strong>

          <p>{interaction.representative}</p>
        </div>

        <div>
          <strong>Topic</strong>

          <p>{interaction.topic}</p>
        </div>

        <div>
          <strong>Time</strong>

          <p>{interaction.interaction_time}</p>
        </div>

        <div>
          <strong>Attendees</strong>

          <p>{interaction.attendees}</p>
        </div>

        <div>
          <strong>Follow-up</strong>

          <p>{interaction.followup}</p>
        </div>
      </div>

      {/* Summary */}

      <div
        style={{
          marginTop: "15px",
        }}
      >
        <strong>Discussion Summary</strong>

        <p
          style={{
            marginTop: "8px",
            lineHeight: "1.6",
            color: "#374151",
          }}
        >
          {interaction.summary}
        </p>
      </div>

      {/* Footer */}

      <div
        style={{
          display: "flex",
          justifyContent: "flex-end",
          gap: "10px",
          marginTop: "20px",
        }}
      >
        <button
          onClick={() => onView(interaction)}
          style={buttonStyle("#0f766e")}
        >
          View
        </button>

        <button
          onClick={() => onSummary(interaction)}
          style={buttonStyle("#7c3aed")}
        >
          AI Summary
        </button>

        <button
          onClick={() => onEdit(interaction)}
          style={buttonStyle("#2563eb")}
        >
          Edit
        </button>

        <button
          onClick={() => onDelete(interaction.id)}
          style={buttonStyle("#dc2626")}
        >
          Delete
        </button>
      </div>
    </div>
  );
};

const buttonStyle = (background) => ({
  background,
  color: "#fff",
  border: "none",
  borderRadius: "8px",
  padding: "10px 16px",
  cursor: "pointer",
  fontWeight: "600",
});

export default InteractionCard;
