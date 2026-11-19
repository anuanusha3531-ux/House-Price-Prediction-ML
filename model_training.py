# ============================================
# RANDOM FOREST CLASSIFICATION - TRAINING SCRIPT
# ============================================

import pandas as pd
import numpy as np
import os
import json
import joblib
from datetime import datetime

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report,
    roc_auc_score, roc_curve
)

# ============================================
# CREATE OUTPUT FOLDER
# ============================================
os.makedirs("model_outputs", exist_ok=True)

# ============================================
# 1. TRAIN MODEL
# ============================================
def train_model():
    try:
        print("Loading data...")

        X_train = pd.read_csv("outputs/X_train.csv")
        X_test = pd.read_csv("outputs/X_test.csv")
        y_train = pd.read_csv("outputs/y_train.csv").values.ravel()
        y_test = pd.read_csv("outputs/y_test.csv").values.ravel()

    except Exception as e:
        print("Error loading data:", e)
        return None

    print("Training Random Forest...")

    rf = RandomForestClassifier(random_state=42)

    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [10, 20, 30, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    grid_search = GridSearchCV(
        rf,
        param_grid,
        cv=5,
        n_jobs=-1,
        verbose=2
    )

    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    print("Best Parameters:", grid_search.best_params_)

    return best_model, X_test, y_test, grid_search.best_params_, X_train.columns


# ============================================
# 2. EVALUATE MODEL
# ============================================
def evaluate_model(model, X_test, y_test):

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1] if len(set(y_test)) == 2 else None

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    print("\n--- MODEL PERFORMANCE ---")
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure()
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title("Confusion Matrix")
    plt.savefig("model_outputs/confusion_matrix.png")
    plt.close()

    # ROC Curve (Binary Only)
    roc_auc = None
    if y_prob is not None:
        roc_auc = roc_auc_score(y_test, y_prob)
        fpr, tpr, _ = roc_curve(y_test, y_prob)

        plt.figure()
        plt.plot(fpr, tpr)
        plt.title("ROC Curve")
        plt.savefig("model_outputs/roc_curve.png")
        plt.close()

    # Classification Report
    report = classification_report(y_test, y_pred)

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "roc_auc": roc_auc,
        "classification_report": report
    }, cm


# ============================================
# 3. SAVE MODEL ARTIFACTS
# ============================================
def save_model_artifacts(model, metrics, best_params, feature_names):

    joblib.dump(model, "model_outputs/model.pkl")

    joblib.dump(list(feature_names), "model_outputs/feature_names.pkl")

    # Feature Importance
    importance = model.feature_importances_
    fi_df = pd.DataFrame({
        "feature": feature_names,
        "importance": importance
    }).sort_values(by="importance", ascending=False)

    fi_df.to_csv("model_outputs/feature_importance.csv", index=False)

    # Plot Feature Importance
    plt.figure(figsize=(10, 6))
    sns.barplot(x="importance", y="feature", data=fi_df.head(10))
    plt.title("Top Features")
    plt.savefig("model_outputs/feature_importance.png")
    plt.close()

    # Save metrics
    with open("model_outputs/model_metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    # Model info
    with open("model_outputs/model_info.txt", "w") as f:
        f.write(f"Training Date: {datetime.now()}\n\n")
        f.write(f"Best Parameters: {best_params}\n\n")
        f.write(f"Metrics: {metrics}\n\n")
        f.write(f"Features: {list(feature_names)}\n")


# ============================================
# MAIN EXECUTION
# ============================================
if __name__ == "__main__":

    model, X_test, y_test, best_params, feature_names = train_model()

    if model is not None:
        metrics, cm = evaluate_model(model, X_test, y_test)
        save_model_artifacts(model, metrics, best_params, feature_names)

        print("\nModel training complete!")