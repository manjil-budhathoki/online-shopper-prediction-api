# mlops_pipeline_project/api/serve_model.py

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import os

# --- 1. Load the Preprocessor and the Model from Local Files ---

print("Loading the preprocessor...")
# Load the preprocessor from the path inside the container
preprocessor_path = os.path.join(os.path.dirname(__file__), '..', 'processed_data', 'preprocessor.joblib')
preprocessor = joblib.load(preprocessor_path)
print("Preprocessor loaded successfully.")

print("Loading the trained model...")
# Load the model from the path inside the container
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'logistic_regression_model.joblib')
model = joblib.load(model_path)
print("Model loaded successfully.")


# --- 2. Define the Input Data Schema ---
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
    try:
        input_df = pd.DataFrame([data.dict()])
        processed_input = preprocessor.transform(input_df)
        prediction = model.predict(processed_input)
        probability = model.predict_proba(processed_input)
        prediction_label = "Will Generate Revenue" if prediction[0] == 1 else "Will Not Generate Revenue"
        
        return {
            "prediction": prediction_label,
            "prediction_value": int(prediction[0]),
            "probability_no_revenue": f"{probability[0][0]:.4f}",
            "probability_revenue": f"{probability[0][1]:.4f}"
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def read_root():
    return {"status": "API is live! Version 2.0"}