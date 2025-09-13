# mlops_pipeline_project/serve_model.py

import mlflow
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# --- 1. Load the Preprocessor and the Best Model from MLflow ---

# Define the MLflow tracking server URI
mlflow.set_tracking_uri("http://localhost:5000")

# Define the name of the experiment and the model
EXPERIMENT_NAME = "Online Shopper Prediction"
MODEL_NAME = "logistic_regression_model"

print("Loading the preprocessor...")
# The preprocessor is always the same, so we can load it directly
preprocessor_path = "./processed_data/preprocessor.joblib"
preprocessor = joblib.load(preprocessor_path)
print("Preprocessor loaded successfully.")

print("Searching for the best model in MLflow...")
# Search for the run with the highest F1-score to get the "best" model
best_run = mlflow.search_runs(
    experiment_names=[EXPERIMENT_NAME],
    order_by=["metrics.f1_score DESC"],
    max_results=1
).iloc[0]

# Get the run ID of the best run
best_run_id = best_run.run_id
print(f"Found best model in run: {best_run_id} with F1-score: {best_run['metrics.f1_score']:.4f}")

# Load the model from that specific run
logged_model_uri = f"runs:/{best_run_id}/{MODEL_NAME}"
model = mlflow.sklearn.load_model(logged_model_uri)
print("Best model loaded successfully from MLflow.")


# --- 2. Define the Input Data Schema using Pydantic ---
# This tells FastAPI what kind of data to expect in a prediction request.
# The names and types MUST match the columns used for training.
class ShopperData(BaseModel):
    Month: str
    VisitorType: str
    Administrative: int
    Administrative_Duration: float
    Informational: int
    Informational_Duration: float
    ProductRelated: int
    ProductRelated_Duration: float
    BounceRates: float
    ExitRates: float
    PageValues: float
    SpecialDay: float

# --- 3. Create the FastAPI Application ---
app = FastAPI(
    title="Online Shopper Prediction API",
    description="An API to predict if an online shopper will generate revenue.",
    version="1.0.0"
)

# --- 4. Define the Prediction Endpoint ---
@app.post("/predict")
def predict_revenue(data: ShopperData):
    """
    Takes shopper data as input and returns a revenue prediction.
    """
    try:
        # Convert the input data to a pandas DataFrame
        # The model expects a DataFrame, so we create one from the input JSON
        input_df = pd.DataFrame([data.dict()])

        # Preprocess the input data using the SAME preprocessor from training
        processed_input = preprocessor.transform(input_df)

        # Make a prediction using the loaded model
        prediction = model.predict(processed_input)
        probability = model.predict_proba(processed_input)

        # Convert the prediction to a human-readable format
        prediction_label = "Will Generate Revenue" if prediction[0] == 1 else "Will Not Generate Revenue"
        
        return {
            "prediction": prediction_label,
            "prediction_value": int(prediction[0]),
            "probability_no_revenue": f"{probability[0][0]:.4f}",
            "probability_revenue": f"{probability[0][1]:.4f}"
        }

    except Exception as e:
        return {"error": str(e)}

# Optional: Define a root endpoint for health checks
@app.get("/")
def read_root():
    return {"status": "API is live and running!"}