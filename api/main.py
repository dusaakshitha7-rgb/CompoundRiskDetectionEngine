from fastapi import FastAPI
from api.schemas import RiskInput, RiskOutput
from api.predict import predict_risk
import logging

# Configure Logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI(
    title="Compound Risk Detection API",
    description="AI-powered Industrial Safety Risk Prediction System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Compound Risk Detection API is Running"
    }


@app.post("/predict-risk", response_model=RiskOutput)
def predict(data: RiskInput):

    try:
        logging.info(f"Received Request: {data}")

        result = predict_risk(data.model_dump())

        logging.info(f"Prediction Result: {result}")

        return result

    except Exception as e:

        logging.error(str(e))

        return {
            "Prediction_Time": "",
            "Explosion_Risk": "",
            "Fire_Risk": "",
            "Gas_Leakage_Risk": "",
            "Electrical_Hazard": "",
            "Worker_Safety_Score": 0,
            "Risk_Score": 0,
            "Status": "Error",
            "Reason": str(e)
        }