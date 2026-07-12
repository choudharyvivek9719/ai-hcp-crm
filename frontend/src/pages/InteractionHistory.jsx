import { useEffect, useState } from "react";
import axios from "axios";

const API_URL = "http://localhost:8000";

const InteractionHistory = () => {
  const [interactions, setInteractions] = useState([]);
  const [filteredInteractions, setFilteredInteractions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [searchText, setSearchText] = useState("");

  useEffect(() => {
    fetchInteractions();
  }, []);

  useEffect(() => {
    handleSearch(searchText);
  }, [searchText, interactions]);

  const fetchInteractions = async () => {
    try {
      setLoading(true);

      const response = await axios.get(
        `${API_URL}/interaction`
      );

      setInteractions(response.data);
      setFilteredInteractions(response.data);
    } catch (error) {
      console.error("Failed to load interactions", error);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = (text) => {
    setSearchText(text);

    if (!text.trim()) {
      setFilteredInteractions(interactions);
      return;
    }

    const filtered = interactions.filter((item) =>
      item.hcp_name?.toLowerCase().includes(text.toLowerCase()) ||
      item.topic?.toLowerCase().includes(text.toLowerCase()) ||
      item.hospital?.toLowerCase().includes(text.toLowerCase())
    );

    setFilteredInteractions(filtered);
  };

  const deleteInteraction = async (id) => {
    const confirmDelete = window.confirm(
      "Delete this interaction?"
    );

    if (!confirmDelete) return;

    try {
      await axios.delete(
        `${API_URL}/interaction/${id}`
      );

      fetchInteractions();
    } catch (error) {
      console.error(error);
      alert("Unable to delete interaction.");
    }
  };

  const editInteraction = (id) => {
    window.location.href = `/edit/${id}`;
  };

  return (
    <div className="container mt-4">

      <div className="d-flex justify-content-between align-items-center mb-4">

        <h2>Interaction History</h2>

        <input
          className="form-control w-25"
          placeholder="Search..."
          value={searchText}
          onChange={(e) => handleSearch(e.target.value)}
        />

      </div>

      {loading ? (
        <div className="text-center">
          <h5>Loading...</h5>
        </div>
      ) : (

        <table className="table table-bordered table-striped">

          <thead className="table-dark">

            <tr>

              <th>ID</th>

              <th>Representative</th>

              <th>HCP</th>

              <th>Hospital</th>

              <th>Topic</th>

              <th>Date</th>

              <th>Time</th>

              <th>Attendees</th>

              <th>Summary</th>

              <th>Actions</th>

            </tr>

          </thead>

          <tbody>

            {filteredInteractions.length === 0 ? (

              <tr>

                <td colSpan="10" className="text-center">

                  No interactions found.

                </td>

              </tr>

            ) : (

              filteredInteractions.map((interaction) => (

                <tr key={interaction.id}>

                  <td>{interaction.id}</td>

                  <td>{interaction.representative}</td>

                  <td>{interaction.hcp_name}</td>

                  <td>{interaction.hospital}</td>

                  <td>{interaction.topic}</td>

                  <td>{interaction.interaction_date}</td>

                  <td>{interaction.interaction_time}</td>

                  <td>{interaction.attendees}</td>

                  <td style={{ maxWidth: "250px" }}>
                    {interaction.summary}
                  </td>

                  <td>

                    <button
                      className="btn btn-warning btn-sm me-2"
                      onClick={() =>
                        editInteraction(interaction.id)
                      }
                    >
                      Edit
                    </button>

                    <button
                      className="btn btn-danger btn-sm"
                      onClick={() =>
                        deleteInteraction(interaction.id)
                      }
                    >
                      Delete
                    </button>

                  </td>

                </tr>

              ))

            )}

          </tbody>

        </table>

      )}

    </div>
  );
};

export default InteractionHistory;
