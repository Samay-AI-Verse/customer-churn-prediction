import logging
from fastapi import FastAPI, HTTPException
from huggingface_hub import hf_hub_download
import joblib
import pandas as pd
from pydantic import BaseModel, Field, validator

# -----------------------------
# Logging Setup
# -----------------------------
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

# -----------------------------
# App Initialization
# -----------------------------
app = FastAPI(
    title="Customer Retention Prediction API",
    description="AI-powered API to predict customer loyalty and retention risk",
    version="1.0.0",
)

# -----------------------------
# Load Model from HF Hub
# -----------------------------
MODEL_REPO = "Samay-Verse/Customer-Churn-Prediction-Model"
MODEL_FILE = "random_forest.pkl"

try:
    logger.info("Downloading model from Hugging Face Hub...")
    MODEL_PATH = hf_hub_download(repo_id=MODEL_REPO, filename=MODEL_FILE)
    model = joblib.load(MODEL_PATH)
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Model loading failed: {e}")
    raise RuntimeError("Failed to load model. Check HF repo and file name.")


# -----------------------------
# Input Schema
# -----------------------------
class CustomerData(BaseModel):
    Age: int = Field(..., example=35, ge=0, le=120)
    Gender: str = Field(..., example="Male")
    Tenure: int = Field(..., example=24, ge=0)
    Usage_Frequency: int = Field(..., example=15, ge=0)
    Support_Calls: int = Field(..., example=3, ge=0)
    Payment_Delay: int = Field(..., example=10, ge=0)
    Subscription_Type: str = Field(..., example="Premium")
    Contract_Length: str = Field(..., example="Annual")
    Total_Spend: float = Field(..., example=750.0, ge=0)
    Last_Interaction: int = Field(..., example=15, ge=0)

    # -----------------------------
    # Validators
    # -----------------------------
    @validator("Gender")
    def validate_gender(cls, v):
        allowed = ["Male", "Female"]
        if v not in allowed:
            raise ValueError(f"Gender must be one of {allowed}")
        return v

    @validator("Subscription_Type")
    def validate_subscription(cls, v):
        allowed = ["Basic", "Standard", "Premium"]
        if v not in allowed:
            raise ValueError(f"Subscription_Type must be one of {allowed}")
        return v

    @validator("Contract_Length")
    def validate_contract(cls, v):
        allowed = ["Monthly", "Quarterly", "Annual"]
        if v not in allowed:
            raise ValueError(f"Contract_Length must be one of {allowed}")
        return v


# -----------------------------
# Routes
# -----------------------------
@app.get("/")
def home():
    return {
        "project": "Customer Retention Prediction System",
        "status": "running",
        "info": "Predict whether customers will stay or leave using AI",
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: CustomerData):
    try:
        logger.info("Received prediction request")

        # Convert to DataFrame
        df = pd.DataFrame([data.dict()])

        # Match model's expected feature names
        df.columns = df.columns.str.replace("_", " ")

        prediction = model.predict(df)[0]
        probability = None

        # If model supports probability
        if hasattr(model, "predict_proba"):
            probability = float(model.predict_proba(df)[0][1])

        logger.info(f"Prediction result: {prediction}")

        return {"churn_prediction": int(prediction), "churn_probability": probability}

    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed")


# -----------------------------
# Local Run Support
# -----------------------------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
