# mlops_pipeline_project/scripts/train_model.py

import joblib
import os
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# THIS IS THE ONLY CHANGE: Point to the running MLflow server
mlflow.set_tracking_uri("http://localhost:5000")

# Set an experiment name. This helps organize runs in the UI.
mlflow.set_experiment("Online Shopper Prediction")


def train_model():
    """
    Loads data, trains a model, evaluates it, and logs everything to a central MLflow server.
    """
    with mlflow.start_run():
        try:
            # --- 1. Load Data ---
            training_data_dir = os.path.join(os.path.dirname(__file__), '..', 'training_data')
            training_data_path = os.path.join(training_data_dir, 'training_testing_sets.npz')
            
            print("Loading data...")
            data = np.load(training_data_path)
            X_train, X_test, y_train, y_test = data['X_train'], data['X_test'], data['y_train'], data['y_test']

            # --- 2. Define and Log Model Parameters ---
            params = {
                "random_state": 42,
                "class_weight": "balanced",
                "max_iter": 1000
            }
            model = LogisticRegression(**params)
            mlflow.log_params(params)
            print("Model parameters logged to MLflow.")

            # --- 3. Train the Model ---
            print("Training the model...")
            model.fit(X_train, y_train)

            # --- 4. Evaluate and Log Metrics ---
            print("Evaluating the model...")
            y_pred = model.predict(X_test)
            metrics = {
                "accuracy": accuracy_score(y_test, y_pred),
                "precision": precision_score(y_test, y_pred),
                "recall": recall_score(y_test, y_pred),
                "f1_score": f1_score(y_test, y_pred)
            }
            mlflow.log_metrics(metrics)
            print("Model metrics logged to MLflow:")
            print(metrics)

            # --- 5. Log the Model Artifact ---
            print("Logging the model artifact to MLflow...")
            mlflow.sklearn.log_model(model, "logistic_regression_model")

            print("\n--- MLflow run completed successfully! ---")

        except Exception as e:
            print(f"An error occurred during model training: {e}")
            import sys
            sys.exit(1)

if __name__ == "__main__":
    train_model()