from pydantic import BaseModel


class RiskInput(BaseModel):
    Gas_Level: float
    Temperature: float
    Pressure: float
    Humidity: int
    Worker_Count: int
    Maintenance_Status: str
    Permit_Type: str
    Shift: str

    class Config:
        json_schema_extra = {
            "example": {
                "Gas_Level": 53.37,
                "Temperature": 72.18,
                "Pressure": 8.41,
                "Humidity": 59,
                "Worker_Count": 18,
                "Maintenance_Status": "Yes",
                "Permit_Type": "Normal",
                "Shift": "Morning"
            }
        }


class RiskOutput(BaseModel):
    Prediction_Time: str
    Explosion_Risk: str
    Fire_Risk: str
    Gas_Leakage_Risk: str
    Electrical_Hazard: str
    Worker_Safety_Score: int
    Risk_Score: int
    Status: str
    Reason: str