import joblib
import numpy as np

# load model once
model = joblib.load("models/model.pkl")

def predict_price(data):
    try:
        features = np.array([[
            float(data["area"]),
            float(data["bedRoom"]),
            float(data["bathroom"]),
            float(data["balcony"])   # mapped to parking
        ]])

        prediction = model.predict(features)[0]

        return round(prediction, 2)

    except Exception as e:
        raise Exception(f"Prediction error: {str(e)}")