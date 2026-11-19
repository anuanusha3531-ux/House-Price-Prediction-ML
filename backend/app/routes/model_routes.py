from fastapi import APIRouter
from app.services.model_service import predict_price
from app.utils.db import save_prediction   # 🔥 ADD THIS

router = APIRouter()

@router.post("/predict")
def predict(data: dict):
    result = predict_price(data)

    save_prediction(data, result)   # 🔥 ADD THIS

    return {"prediction": result}