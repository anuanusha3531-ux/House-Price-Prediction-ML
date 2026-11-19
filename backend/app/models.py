from pydantic import BaseModel
from typing import Dict, Any, List

class PredictionInput(BaseModel):
    data: Dict[str, Any]

class PredictionResponse(BaseModel):
    prediction: int
    probabilities: List[float]