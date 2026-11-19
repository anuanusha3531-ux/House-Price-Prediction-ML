import { useEffect, useState } from "react";
import api from "../services/api";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";

export default function Dashboard() {
  const [data, setData] = useState([]);
  const [stats, setStats] = useState(null);

  useEffect(() => {
    api.get("/dashboard/feature-importance")
      .then(res => setData(res.data));

    api.get("/dashboard/stats")
      .then(res => setStats(res.data));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">📊 Dashboard</h1>

      {/* Stats */}
      {stats && (
        <div className="grid grid-cols-2 gap-6 mb-6">
          <div className="bg-white shadow rounded-lg p-5 text-center">
            <p className="text-gray-500">Total Predictions</p>
            <h2 className="text-2xl font-bold">{stats.total_predictions}</h2>
          </div>

          <div className="bg-white shadow rounded-lg p-5 text-center">
            <p className="text-gray-500">Model</p>
            <h2 className="text-2xl font-bold">{stats.model_name}</h2>
          </div>
        </div>
      )}

      {/* Chart */}
      <div className="bg-white shadow rounded-lg p-5">
        <h2 className="mb-4 font-semibold">Feature Importance</h2>

        {data.length > 0 ? (
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="feature" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="importance" fill="#22c55e" />
            </BarChart>
          </ResponsiveContainer>
        ) : (
          <p>Loading...</p>
        )}
      </div>
    </div>
  );
}