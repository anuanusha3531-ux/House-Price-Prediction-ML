import { useState } from "react";
import api from "../services/api";

export default function Prediction() {
  const [form, setForm] = useState({
    area: "",
    bedRoom: "",
    bathroom: "",
    balcony: "",
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [file, setFile] = useState(null);

  // 🔹 Handle input change
  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  // 🔹 Single Prediction
  const handlePredict = async () => {
    try {
      setLoading(true);

      const res = await api.post("/model/predict", {
        area: Number(form.area),
        bedRoom: Number(form.bedRoom),
        bathroom: Number(form.bathroom),
        balcony: Number(form.balcony),
      });

      setResult(res.data.prediction);
    } catch (err) {
      console.error(err);
      alert("Prediction failed");
    } finally {
      setLoading(false);
    }
  };

  // 🔹 File select
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  // 🔹 Batch Prediction + Download
  const handleBatchPredict = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const res = await api.post("/data/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      alert("File processed successfully!");

      // 🔥 Auto download
      const downloadUrl = `http://127.0.0.1:8000/${res.data.download_file}`;
      window.open(downloadUrl);

    } catch (err) {
      console.error(err);
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex justify-center pt-20">
      <div className="glass w-[420px] text-white">

        <h2 className="text-2xl font-bold text-center mb-6">
          🏠 House Price Prediction
        </h2>

        {/* 🔹 INPUTS */}
        <input
          name="area"
          value={form.area}
          placeholder="Area"
          onChange={handleChange}
          className="input"
        />

        <input
          name="bedRoom"
          value={form.bedRoom}
          placeholder="Bedrooms"
          onChange={handleChange}
          className="input"
        />

        <input
          name="bathroom"
          value={form.bathroom}
          placeholder="Bathrooms"
          onChange={handleChange}
          className="input"
        />

        <input
          name="balcony"
          value={form.balcony}
          placeholder="Parking"
          onChange={handleChange}
          className="input"
        />

        {/* 🔹 SINGLE PREDICT BUTTON */}
        <button
          onClick={handlePredict}
          className="btn mt-3"
          disabled={loading}
        >
          {loading ? "Predicting..." : "Predict"}
        </button>

        {/* 🔹 RESULT */}
        {result !== null && (
          <p className="mt-4 text-center text-green-300 text-lg font-semibold">
            ₹ {Number(result).toLocaleString()}
          </p>
        )}

        {/* 🔥 BATCH PREDICTION */}
        <div className="mt-6 text-center">
          <h3 className="text-lg mb-3">📁 Batch Prediction</h3>

          <input type="file" onChange={handleFileChange} />

          <button
            onClick={handleBatchPredict}
            className="btn mt-3"
          >
            Upload & Predict
          </button>
        </div>

      </div>
    </div>
  );
}