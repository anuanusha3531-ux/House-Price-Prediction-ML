import { useState } from "react";
import api from "../services/api";

export default function BatchPrediction() {
  const [file, setFile] = useState(null);
  const [downloadLink, setDownloadLink] = useState("");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await api.post("/data/upload", formData);

      alert("Upload successful!");

      // 🔥 Create download URL
      const filePath = res.data.download_file;
      const fullUrl = `http://127.0.0.1:8000/${filePath}`;

      setDownloadLink(fullUrl);

    } catch (err) {
      alert("Error: " + err.message);
    }
  };

  return (
    <div className="mt-10">
      <h2 className="text-lg font-bold mb-3">📁 Batch Prediction</h2>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-3"
      />

      <br />

      <button
        onClick={handleUpload}
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        Upload & Predict
      </button>

      {/* 🔥 DOWNLOAD BUTTON */}
      {downloadLink && (
        <div className="mt-4">
          <a
            href={downloadLink}
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-600 underline"
          >
            Download Result File
          </a>
        </div>
      )}
    </div>
  );
}