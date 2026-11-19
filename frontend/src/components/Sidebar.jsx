import { Link, useLocation } from "react-router-dom";

export default function Sidebar() {
  const location = useLocation();

  const menu = [
    { name: "Home", path: "/" },
    { name: "Prediction", path: "/predict" },
    { name: "Dashboard", path: "/dashboard" },
    { name: "Data", path: "/data" }
  ];

  return (
    <div className="h-screen w-56 bg-gray-900 text-white p-5">
      <h2 className="text-xl font-bold mb-6">🏠 ML App</h2>

      <nav className="flex flex-col gap-3">
        {menu.map((item) => (
          <Link
            key={item.path}
            to={item.path}
            className={`px-3 py-2 rounded-lg transition ${
              location.pathname === item.path
                ? "bg-green-500 text-white"
                : "hover:bg-gray-700"
            }`}
          >
            {item.name}
          </Link>
        ))}
      </nav>
    </div>
  );
}