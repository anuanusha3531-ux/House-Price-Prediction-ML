from fastapi import APIRouter, UploadFile, File
import pandas as pd
import joblib
import os

router = APIRouter()

model = joblib.load("models/model.pkl")

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save uploaded file
        file_location = f"uploads/{file.filename}"
        os.makedirs("uploads", exist_ok=True)

        with open(file_location, "wb") as f:
            f.write(await file.read())

        # Read CSV
        df = pd.read_csv(file_location)

        # Select features (IMPORTANT)
        X = df[["area", "bedrooms", "bathrooms", "parking"]]

        # Predict
        predictions = model.predict(X)

        df["prediction"] = predictions

        # Save result
        output_path = f"downloads/predictions_{file.filename}"
        df.to_csv(output_path, index=False)

        return {
            "message": "File processed successfully",
            "download_file": output_path
        }

    except Exception as e:
        return {"error": str(e)}