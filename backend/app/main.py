from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# 🔹 Import all route files
from app.routes import model_routes, dashboard_routes, data_routes

app = FastAPI()

# 🔹 CORS (IMPORTANT for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Include routers
app.include_router(model_routes.router, prefix="/api/v1/model")
app.include_router(dashboard_routes.router, prefix="/api/v1/dashboard")
app.include_router(data_routes.router, prefix="/api/v1/data")
app.mount("/downloads", StaticFiles(directory="downloads"), name="downloads")
# 🔹 Root route (optional)
@app.get("/")
def home():
    return {"message": "API is running 🚀"}