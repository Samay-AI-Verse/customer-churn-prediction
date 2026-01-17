from fastapi import FastAPI
from huggingface_hub import hf_hub_download
import joblib
import pandas as pd
from pydantic import BaseModel, Field


app = FastAPI()


MODEL_PATH = hf_hub_download(
    repo_id="Samay-Verse/Customer-Churn-Prediction-Model", filename="random_forest.pkl"
)

model = joblib.load(MODEL_PATH)


class Data(BaseModel):
    Age: int = Field(..., example=35, description="Customer age")
    Gender: str = Field(..., example="Male", description="Gender: Male or Female")
    Tenure: int = Field(..., example=24, description="Months as customer")
    Usage_Frequency: int = Field(
        ..., example=15, description="Usage frequency per month"
    )
    Support_Calls: int = Field(..., example=3, description="Number of support calls")
    Payment_Delay: int = Field(..., example=10, description="Days of payment delay")
    Subscription_Type: str = Field(
        ..., example="Premium", description="Subscription: Basic, Standard, or Premium"
    )
    Contract_Length: str = Field(
        ..., example="Annual", description="Contract: Monthly, Quarterly, or Annual"
    )
    Total_Spend: int = Field(..., example=750, description="Total spend amount")
    Last_Interaction: int = Field(
        ..., example=15, description="Days since last interaction"
    )


@app.get("/")
def home():
    return {"Project": "Customer Churn Prediction System"}


@app.post("/predict")
def predict(data: Data):
    result = pd.DataFrame([data.dict()])
    # Rename columns to match the model's expected format (with spaces)
    result.columns = result.columns.str.replace("_", " ")
    predication = model.predict(result)
    return {"Prediction": int(predication[0])}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
