
import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import Prediction from "./pages/Prediction";
import Dashboard from "./pages/Dashboard";
import "./App.css";

function Home() {
  return (
    <div className="home-page">
      <div className="welcome-banner">
        <div>
          <span className="eyebrow">PROPERTY INTELLIGENCE PLATFORM</span>
          <h1>Find the value of your next home.</h1>
          <p>
            Make smarter property decisions with machine learning-powered
            house price predictions and real estate insights.
          </p>
          <NavLink to="/predict" className="primary-link">
            Predict Property Price <span>→</span>
          </NavLink>
        </div>
        <div className="hero-house">🏡</div>
      </div>

      <div className="section-heading">
        <div>
          <span className="eyebrow">YOUR WORKSPACE</span>
          <h2>Explore your tools</h2>
        </div>
      </div>

      <div className="feature-grid">
        <NavLink to="/predict" className="feature-card">
          <div className="feature-icon">⌂</div>
          <h3>Price Prediction</h3>
          <p>Estimate property prices using property details and machine learning.</p>
          <span className="card-link">Start predicting →</span>
        </NavLink>

        <NavLink to="/dashboard" className="feature-card">
          <div className="feature-icon">▥</div>
          <h3>Analytics Dashboard</h3>
          <p>Explore prediction activity and property analytics.</p>
          <span className="card-link">View dashboard →</span>
        </NavLink>
      </div>

      <div className="info-strip">
        <span>✦</span>
        <div>
          <strong>Data-driven property insights</strong>
          <p>Powered by Python, FastAPI and Random Forest Regression.</p>
        </div>
      </div>
    </div>
  );
}

function AppLayout() {
  return (
    <div className="app-layout">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-icon">⌂</div>
          <div>
            <strong>EstateIQ</strong>
            <span>PROPERTY ANALYTICS</span>
          </div>
        </div>

        <div className="nav-label">WORKSPACE</div>

        <nav className="navigation">
          <NavLink to="/" end className="nav-item">
            <span>⌂</span> Home
          </NavLink>
          <NavLink to="/predict" className="nav-item">
            <span>⌕</span> Prediction
          </NavLink>
          <NavLink to="/dashboard" className="nav-item">
            <span>▥</span> Dashboard
          </NavLink>
        </nav>

        <div className="sidebar-bottom">
          <div className="sidebar-note">
            <span>✦</span>
            <strong>Smart Property Insights</strong>
            <p>Make informed decisions with intelligent price estimates.</p>
          </div>
          <div className="profile">
            <div className="avatar">A</div>
            <div>
              <strong>Administrator</strong>
              <span>Property Analyst</span>
            </div>
          </div>
        </div>
      </aside>

      <main className="main-area">
        <header className="topbar">
          <div>
            <span className="topbar-label">REAL ESTATE INTELLIGENCE</span>
            <h2>Property Insights</h2>
          </div>
          <div className="topbar-status">
            <span className="status-dot"></span>
            ML System Active
          </div>
        </header>

        <div className="page-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/predict" element={<Prediction />} />
            <Route path="/dashboard" element={<Dashboard />} />
          </Routes>
        </div>

        <footer className="footer">
          © 2026 EstateIQ · House Price Prediction ML
        </footer>
      </main>
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>
      <AppLayout />
    </BrowserRouter>
  );
}

export default App;
