// frontend/src/pages/EditInteraction.jsx

import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import axios from "axios";

const API_URL = "http://localhost:8000";

const EditInteraction = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);

  const [formData, setFormData] = useState({
    representative: "",
    hcp_name: "",
    speciality: "",
    hospital: "",
    topic: "",
    interaction_date: "",
    interaction_time: "",
    attendees: "",
    summary: "",
    followup: "",
  });

  useEffect(() => {
    fetchInteraction();
  }, []);

  const fetchInteraction = async () => {
    try {
      const response = await axios.get(
        `${API_URL}/interaction/${id}`
      );

      setFormData(response.data);
    } catch (error) {
      console.error(error);
      alert("Unable to load interaction.");
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const updateInteraction = async (e) => {
    e.preventDefault();

    setSaving(true);

    try {
      await axios.put(
        `${API_URL}/interaction/${id}`,
        formData
      );

      alert("Interaction Updated Successfully");

      navigate("/history");
    } catch (error) {
      console.error(error);

      alert("Update Failed");
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center mt-10">
        Loading Interaction...
      </div>
    );
  }

  return (
    <div className="max-w-5xl mx-auto p-8">

      <h1 className="text-3xl font-bold mb-8">
        Edit Interaction
      </h1>

      <form
        onSubmit={updateInteraction}
        className="grid grid-cols-2 gap-5"
      >

        <div>
          <label className="font-medium">
            Representative
          </label>

          <input
            type="text"
            name="representative"
            value={formData.representative}
            onChange={handleChange}
            className="w-full border rounded p-2 mt-1"
          />
        </div>

        <div>
          <label className="font-medium">
            HCP Name
          </label>

          <input
            type="text"
            name="hcp_name"
            value={formData.hcp_name}
            onChange={handleChange}
            className="w-full border rounded p-2 mt-1"
          />
        </div>

        <div>
          <label className="font-medium">
            Speciality
          </label>

          <input
            type="text"
            name="speciality"
            value={formData.speciality}
            onChange={handleChange}
            className="w-full border rounded p-2 mt-1"
          />
        </div>

        <div>
          <label className="font-medium">
            Hospital
          </label>

          <input
            type="text"
            name="hospital"
            value={formData.hospital}
            onChange={handleChange}
            className="w-full border rounded p-2 mt-1"
          />
        </div>

        <div>
          <label className="font-medium">
            Topic
          </label>

          <input
            type="text"
            name="topic"
            value={formData.topic}
            onChange={handleChange}
            className="w-full border rounded p-2 mt-1"
          />
        </div>

        <div>
          <label className="font-medium">
            Interaction Date
          </label>

          <input
            type="date"
            name="interaction_date"
            value={formData.interaction_date}
            onChange={handleChange}
            className="w-full border rounded p-2 mt-1"
          />
        </div>

        <div>
          <label className="font-medium">
            Interaction Time
          </label>

          <input
            type="time"
            name="interaction_time"
            value={formData.interaction_time}
            onChange={handleChange}
            className="w-full border rounded p-2 mt-1"
          />
        </div>

        <div>
          <label className="font-medium">
            Attendees
          </label>

          <input
            type="number"
            name="attendees"
            value={formData.attendees}
            onChange={handleChange}
            className="w-full border rounded p-2 mt-1"
          />
        </div>

        <div className="col-span-2">
          <label className="font-medium">
            Discussion Summary
          </label>

          <textarea
            rows="5"
            name="summary"
            value={formData.summary}
            onChange={handleChange}
            className="w-full border rounded p-2 mt-1"
          />
        </div>

        <div>
          <label className="font-medium">
            Follow-up Date
          </label>

          <input
            type="date"
            name="followup"
            value={formData.followup}
            onChange={handleChange}
            className="w-full border rounded p-2 mt-1"
          />
        </div>

        <div className="col-span-2 flex gap-4 mt-4">

          <button
            type="submit"
            disabled={saving}
            className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
          >
            {saving ? "Updating..." : "Update Interaction"}
          </button>

          <button
            type="button"
            onClick={() => navigate("/history")}
            className="bg-gray-500 text-white px-6 py-2 rounded hover:bg-gray-600"
          >
            Cancel
          </button>

        </div>

      </form>

    </div>
  );
};

export default EditInteraction;
