from fastapi import APIRouter
from app.utils.db import get_all_predictions

router = APIRouter()


# =========================================
# 🔹 STATS API
# =========================================
@router.get("/stats")
def get_stats():
    return {
        "total_predictions": 25,
        "model_name": "Random Forest",
        "version": "1.0"
    }


# =========================================
# 🔹 FEATURE IMPORTANCE
# =========================================
@router.get("/feature-importance")
def feature_importance():
    return [
        {"feature": "area", "importance": 0.4},
        {"feature": "bedRoom", "importance": 0.2},
        {"feature": "bathroom", "importance": 0.15},
        {"feature": "balcony", "importance": 0.1}
    ]


# =========================================
# 🔹 PREDICTIONS HISTORY
# =========================================
@router.get("/predictions-history")
def prediction_history():
    data = get_all_predictions()
    return data