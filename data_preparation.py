# ===============================
# HOUSE PRICE PREDICTION - DATA PREPARATION
# ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# ===============================
# 1. LOAD DATASET
# ===============================
try:
    df = pd.read_csv("house_data.csv")  # change filename if needed
    print("Dataset loaded successfully!")
except Exception as e:
    print("Error loading dataset:", e)
    exit()

# ===============================
# 2. CREATE OUTPUT FOLDER
# ===============================
os.makedirs("outputs", exist_ok=True)

# ===============================
# 3. EXPLORATORY DATA ANALYSIS
# ===============================

print("\n--- BASIC INFO ---")
print("Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nData Types:\n", df.dtypes)

# Save basic info
with open("outputs/data_preprocessing_report.txt", "w") as f:
    f.write(f"Shape: {df.shape}\n\n")
    f.write(f"Columns:\n{df.columns}\n\n")
    f.write(f"Data Types:\n{df.dtypes}\n\n")

# Head
print("\nFirst 5 rows:\n", df.head())

# Statistical summary
print("\nSummary:\n", df.describe())

# Missing values
missing = df.isnull().sum()
print("\nMissing values:\n", missing)

# Duplicates
duplicates = df.duplicated().sum()
print("\nDuplicate rows:", duplicates)

# Identify column types
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

print("\nNumerical columns:", num_cols)
print("\nCategorical columns:", cat_cols)

# ===============================
# 4. VISUALIZATION
# ===============================

# Distribution plots
for col in num_cols:
    plt.figure()
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.savefig(f"outputs/{col}_distribution.png")
    plt.close()

# Box plots (Outliers)
for col in num_cols:
    plt.figure()
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.savefig(f"outputs/{col}_boxplot.png")
    plt.close()

# Correlation heatmap
plt.figure(figsize=(10, 8))
corr = df[num_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("outputs/correlation_heatmap.png")
plt.close()

# ===============================
# 5. DATA PREPROCESSING
# ===============================

# ---- Handle Missing Values ----
for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# ---- Remove Duplicates ----
df.drop_duplicates(inplace=True)

# ---- Encode Categorical Variables ----
le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# ---- Handle Outliers (IQR Method) ----
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df[col] = np.clip(df[col], lower, upper)

# ---- Feature Scaling ----
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

# ===============================
# 6. SPLIT DATA
# ===============================

# Change target column name if needed
# ===============================
# CREATE TARGET VARIABLE (CLASSIFICATION)
# ===============================

# Convert price into categories (Low, Medium, High)
df['price_category'] = pd.qcut(
    df['price'],
    q=3,
    labels=[0, 1, 2],
    duplicates='drop'   # 🔥 IMPORTANT FIX
)
df = df.dropna(subset=['price_category'])
# Drop original price column
df.drop('price', axis=1, inplace=True)

# Now use new target
target_column = 'price_category'  # <-- update if different

if target_column not in df.columns:
    print(f"ERROR: '{target_column}' column not found!")
    exit()

X = df.drop(target_column, axis=1)
y = df[target_column]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# 7. SAVE FILES
# ===============================

df.to_csv("outputs/processed_data.csv", index=False)
X_train.to_csv("outputs/X_train.csv", index=False)
X_test.to_csv("outputs/X_test.csv", index=False)
y_train.to_csv("outputs/y_train.csv", index=False)
y_test.to_csv("outputs/y_test.csv", index=False)

print("\nAll files saved in 'outputs' folder!")

# ===============================
# 8. DATA DICTIONARY
# ===============================

with open("outputs/data_preprocessing_report.txt", "a") as f:
    f.write("\n\n--- DATA PREPROCESSING STEPS ---\n")
    f.write("1. Missing values handled (median for numerical, mode for categorical)\n")
    f.write("2. Duplicates removed\n")
    f.write("3. Label Encoding applied to categorical variables\n")
    f.write("4. Outliers handled using IQR clipping\n")
    f.write("5. Feature scaling using StandardScaler\n")
    f.write("6. Train-test split (80-20)\n")

print("Report saved successfully!")