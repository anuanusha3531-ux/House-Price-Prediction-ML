import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Prediction from "./pages/Prediction";
import Dashboard from "./pages/Dashboard";
function Home() {
  return <h1>🏠 Home Page Working</h1>;
}

function App() {
  return (
    <BrowserRouter>
      <div style={{ display: "flex", minHeight: "100vh" }}>

        {/* Sidebar */}
        <div style={{ width: "200px", padding: "20px", borderRight: "1px solid #ccc" }}>
          <h2>🏠 ML App</h2>

          <nav style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
            <Link to="/">Home</Link>
            <Link to="/predict">Prediction</Link>
            <Link to="/dashboard">Dashboard</Link>
          </nav>
        </div>

        {/* Page */}
        <div style={{ padding: "20px" }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/predict" element={<Prediction />} />
            <Route path="/dashboard" element={<Dashboard />} />
          </Routes>
        </div>

      </div>
    </BrowserRouter>
  );
}

export default App;