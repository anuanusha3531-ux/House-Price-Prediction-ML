import joblib
import pandas as pd

def load_model_and_predict(input_data):

    try:
        model = joblib.load("model_outputs/model.pkl")
        feature_names = joblib.load("model_outputs/feature_names.pkl")

    except Exception as e:
        print("Error loading model:", e)
        return

    # Convert input to DataFrame
    df = pd.DataFrame([input_data])

    # Ensure correct column order
    df = df[feature_names]

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0]

    return prediction, probability


def predict_new_data(input_data):
    pred, prob = load_model_and_predict(input_data)

    print("Prediction:", pred)
    print("Probabilities:", prob)


# =========================
# SAMPLE TEST
# =========================
if __name__ == "__main__":

    sample_input = {
        # Replace with your actual features
        "area": 1200,
        "bedrooms": 3,
        "bathrooms": 2
    }

    predict_new_data(sample_input)