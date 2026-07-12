import React, { useEffect, useState } from "react";
import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

const HCPDirectory = () => {
  const [hcps, setHcps] = useState([]);
  const [filteredHcps, setFilteredHcps] = useState([]);

  const [loading, setLoading] = useState(true);

  const [search, setSearch] = useState("");

  const [speciality, setSpeciality] = useState("");

  const [city, setCity] = useState("");

  useEffect(() => {
    fetchHCPs();
  }, []);

  useEffect(() => {
    filterHCPs();
  }, [search, speciality, city, hcps]);

  const fetchHCPs = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/hcp`);

      setHcps(response.data);

      setFilteredHcps(response.data);
    } catch (error) {
      console.error(error);

      // Sample data if backend is unavailable
      const sample = [
        {
          id: 1,
          doctor_name: "Dr. Rajesh Sharma",
          speciality: "Cardiology",
          hospital: "Apollo Hospital",
          city: "Delhi",
          phone: "9876543210",
        },
        {
          id: 2,
          doctor_name: "Dr. Neha Mehta",
          speciality: "Diabetology",
          hospital: "Fortis Hospital",
          city: "Delhi",
          phone: "9988776655",
        },
        {
          id: 3,
          doctor_name: "Dr. Amit Verma",
          speciality: "Neurology",
          hospital: "Max Hospital",
          city: "Noida",
          phone: "9991122334",
        },
      ];

      setHcps(sample);
      setFilteredHcps(sample);
    } finally {
      setLoading(false);
    }
  };

  const filterHCPs = () => {
    let data = [...hcps];

    if (search !== "") {
      data = data.filter((item) =>
        item.doctor_name.toLowerCase().includes(search.toLowerCase())
      );
    }

    if (speciality !== "") {
      data = data.filter(
        (item) =>
          item.speciality.toLowerCase() === speciality.toLowerCase()
      );
    }

    if (city !== "") {
      data = data.filter(
        (item) => item.city.toLowerCase() === city.toLowerCase()
      );
    }

    setFilteredHcps(data);
  };

  const startInteraction = (doctor) => {
    alert(`Start Interaction with ${doctor.doctor_name}`);
    // Later:
    // navigate("/log-interaction", {
    //   state: doctor
    // });
  };

  return (
    <div className="container py-4">
      <h2 className="mb-4">Healthcare Professional Directory</h2>

      <div className="row mb-4">

        <div className="col-md-4">
          <input
            className="form-control"
            placeholder="Search Doctor..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </div>

        <div className="col-md-4">
          <select
            className="form-select"
            value={speciality}
            onChange={(e) => setSpeciality(e.target.value)}
          >
            <option value="">All Specialities</option>
            <option>Cardiology</option>
            <option>Diabetology</option>
            <option>Neurology</option>
            <option>Orthopedics</option>
            <option>Dermatology</option>
          </select>
        </div>

        <div className="col-md-4">
          <input
            className="form-control"
            placeholder="Filter by City"
            value={city}
            onChange={(e) => setCity(e.target.value)}
          />
        </div>

      </div>

      {loading ? (
        <div className="text-center mt-5">
          <h5>Loading HCP Directory...</h5>
        </div>
      ) : (
        <div className="row">

          {filteredHcps.length === 0 ? (
            <div className="col-12">
              <div className="alert alert-warning">
                No Healthcare Professionals Found.
              </div>
            </div>
          ) : (
            filteredHcps.map((doctor) => (
              <div className="col-lg-4 mb-4" key={doctor.id}>
                <div className="card shadow-sm h-100">

                  <div className="card-body">

                    <h5 className="card-title">
                      {doctor.doctor_name}
                    </h5>

                    <p>
                      <strong>Speciality:</strong>{" "}
                      {doctor.speciality}
                    </p>

                    <p>
                      <strong>Hospital:</strong>{" "}
                      {doctor.hospital}
                    </p>

                    <p>
                      <strong>City:</strong>{" "}
                      {doctor.city}
                    </p>

                    <p>
                      <strong>Phone:</strong>{" "}
                      {doctor.phone}
                    </p>

                  </div>

                  <div className="card-footer bg-white">

                    <button
                      className="btn btn-primary w-100"
                      onClick={() =>
                        startInteraction(doctor)
                      }
                    >
                      Log Interaction
                    </button>

                  </div>

                </div>
              </div>
            ))
          )}

        </div>
      )}
    </div>
  );
};

export default HCPDirectory;
