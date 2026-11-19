import { useEffect, useState } from "react";
import api from "../services/api";
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid
} from "recharts";

function Dashboard() {
  const [stats, setStats] = useState(null);
  const [features, setFeatures] = useState([]);

  useEffect(() => {
    fetchStats();
    fetchFeatures();
  }, []);

  const fetchStats = async () => {
    try {
      const res = await api.get("/dashboard/stats");
      setStats(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const fetchFeatures = async () => {
    try {
      const res = await api.get("/dashboard/feature-importance");
      setFeatures(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ marginTop: "40px", textAlign: "center" }}>
      <h2>📊 Dashboard</h2>

      {/* 🔹 STATS */}
      {stats && (
        <div style={{ marginBottom: "30px" }}>
          <p><strong>Total Predictions:</strong> {stats.total_predictions}</p>
          <p><strong>Model:</strong> {stats.model_name}</p>
        </div>
      )}

      {/* 🔹 FEATURE IMPORTANCE CHART */}
      <h3>Feature Importance</h3>

      <BarChart width={400} height={300} data={features}>
        <CartesianGrid stroke="#ccc" />
        <XAxis dataKey="feature" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="importance" fill="#4CAF50" />
      </BarChart>
    </div>
  );
}

export default Dashboard;