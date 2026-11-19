import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# 🔹 Load dataset
df = pd.read_csv("downloads/Housing.csv")  # make sure filename matches

# 🔹 Select features (INPUT)
X = df[["area", "bedrooms", "bathrooms", "parking"]]

# 🔹 Target (OUTPUT)
y = df["price"]

# 🔹 Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🔹 Create model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# 🔹 Train model
model.fit(X_train, y_train)

# 🔹 Create models folder if not exists
os.makedirs("models", exist_ok=True)

# 🔹 Save model
joblib.dump(model, "models/model.pkl")

print("✅ Model trained and saved successfully!")