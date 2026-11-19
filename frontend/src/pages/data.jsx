return (
  <div>
    <h1 className="text-3xl font-bold mb-6 text-gray-800">
      📂 Data Management
    </h1>

    {/* Upload Card */}
    <div className="bg-white p-6 rounded-xl shadow mb-6">
      <h2 className="font-semibold mb-3">Upload Dataset</h2>

      <input
        type="file"
        className="border p-2 rounded"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button
        onClick={handleUpload}
        className="ml-3 bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded"
      >
        Upload
      </button>
    </div>

    {/* Preview Card */}
    {preview.length > 0 && (
      <div className="bg-white p-6 rounded-xl shadow mb-6 overflow-auto">
        <h2 className="font-semibold mb-3">Preview</h2>

        <table className="min-w-full border">
          <thead className="bg-gray-100">
            <tr>
              {Object.keys(preview[0]).map((key) => (
                <th key={key} className="p-2 border">{key}</th>
              ))}
            </tr>
          </thead>

          <tbody>
            {preview.map((row, i) => (
              <tr key={i}>
                {Object.values(row).map((val, j) => (
                  <td key={j} className="p-2 border">{val}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    )}

    {/* Preprocess */}
    {file && (
      <button
        onClick={handlePreprocess}
        className="bg-blue-500 hover:bg-blue-600 text-white px-5 py-2 rounded"
      >
        ⚙️ Preprocess Data
      </button>
    )}
  </div>
);