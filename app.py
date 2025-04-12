from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize the FastAPI app
app = FastAPI()

# Load the trained model
model = joblib.load("model/logistic_regression_model.pkl")

# Define the expected input format
class ChurnRequest(BaseModel):
    data: list  # 2D list: [[feature1, feature2, ..., featureN]]

@app.get("/")
def read_root():
    return {"message": "Telco Customer Churn Prediction API is running 🚀"}

@app.post("/predict")
def predict_churn(request: ChurnRequest):
    input_data = np.array(request.data)
    prediction = model.predict(input_data).tolist()
    probability = model.predict_proba(input_data)[:, 1].tolist()

    return {
        "prediction": prediction,
        "churn_probability": probability
    }
