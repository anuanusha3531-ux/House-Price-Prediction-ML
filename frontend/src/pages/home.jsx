import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-r from-green-100 to-green-50 flex items-center justify-center">
      <div className="text-center max-w-xl p-6">
        
        <h1 className="text-4xl font-bold mb-4 text-gray-800">
          🏠 House Price Prediction
        </h1>

        <p className="text-gray-600 mb-6">
          Predict house prices instantly using Machine Learning. 
          Analyze features like area, bedrooms, bathrooms, and more.
        </p>

        <div className="flex justify-center gap-4">
          <Link
            to="/predict"
            className="bg-green-500 hover:bg-green-600 text-white px-6 py-3 rounded-lg font-semibold"
          >
            Start Prediction
          </Link>

          <Link
            to="/dashboard"
            className="bg-gray-800 hover:bg-gray-900 text-white px-6 py-3 rounded-lg font-semibold"
          >
            View Dashboard
          </Link>
        </div>

      </div>
    </div>
  );
}