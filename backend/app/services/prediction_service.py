import pandas as pd
from app.services.model_service import load_model

def predict(input_data: dict):
    model, features = load_model()

    df = pd.DataFrame([input_data])

    # 🔥 Fill missing columns with default value (0)
    for col in features:
        if col not in df.columns:
            df[col] = 0

    # Ensure correct order
    df = df[features]

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0].tolist()

    return prediction, probability