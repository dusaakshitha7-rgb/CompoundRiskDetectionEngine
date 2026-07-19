import joblib
import pandas as pd
from datetime import datetime

# -----------------------------
# Load Trained Models
# -----------------------------
explosion_model = joblib.load("saved_models/explosion_risk_model.pkl")
fire_model = joblib.load("saved_models/fire_risk_model.pkl")
gas_model = joblib.load("saved_models/gas_leakage_model.pkl")
electrical_model = joblib.load("saved_models/electrical_hazard_model.pkl")
worker_model = joblib.load("saved_models/worker_safety_model.pkl")

print("All models loaded successfully!")


# -----------------------------
# Prediction Function
# -----------------------------
def predict_risk(data):

    # Convert Maintenance Status
    maintenance = 1 if data["Maintenance_Status"] == "Yes" else 0

    # Dictionaries
    permit_dict = {
        "Normal": 0,
        "Hot Work": 1,
        "Confined Space": 2
    }

    shift_dict = {
        "Morning": 0,
        "Evening": 1,
        "Night": 2
    }

    # Validate Permit Type
    if data["Permit_Type"] not in permit_dict:
        raise ValueError("Invalid Permit Type")

    # Validate Shift
    if data["Shift"] not in shift_dict:
        raise ValueError("Invalid Shift")

    permit = permit_dict[data["Permit_Type"]]
    shift = shift_dict[data["Shift"]]

    # -----------------------------
    # Create Input DataFrame
    # -----------------------------
    input_data = pd.DataFrame([{
        "Gas_Level": data["Gas_Level"],
        "Temperature": data["Temperature"],
        "Pressure": data["Pressure"],
        "Humidity": data["Humidity"],
        "Worker_Count": data["Worker_Count"],
        "Maintenance_Status": maintenance,
        "Permit_Type": permit,
        "Shift": shift
    }])

    # -----------------------------
    # Predictions
    # -----------------------------
    explosion = int(explosion_model.predict(input_data)[0])
    fire = int(fire_model.predict(input_data)[0])
    gas = int(gas_model.predict(input_data)[0])
    electrical = int(electrical_model.predict(input_data)[0])
    worker_score = int(worker_model.predict(input_data)[0])

    # -----------------------------
    # Convert Predictions to Labels
    # -----------------------------
    label_map = {
        0: "High",
        1: "Low",
        2: "Medium"
    }

    explosion_label = label_map[explosion]
    fire_label = label_map[fire]
    gas_label = label_map[gas]
    electrical_label = label_map[electrical]

    # -----------------------------
    # Risk Score Calculation
    # -----------------------------
    risk_map = {
        "Low": 25,
        "Medium": 60,
        "High": 90
    }

    total = (
        risk_map[explosion_label]
        + risk_map[fire_label]
        + risk_map[gas_label]
        + risk_map[electrical_label]
    ) / 4

    risk_score = int((total + (100 - worker_score)) / 2)

    # -----------------------------
    # Risk Status
    # -----------------------------
    if risk_score <= 25:
        status = "Low"
    elif risk_score <= 50:
        status = "Medium"
    elif risk_score <= 75:
        status = "High"
    else:
        status = "Critical"

    # -----------------------------
    # Generate Reason
    # -----------------------------
    reasons = []

    if explosion_label == "High":
        reasons.append("High explosion risk")

    if fire_label == "High":
        reasons.append("High fire risk")

    if gas_label == "High":
        reasons.append("High gas leakage risk")

    if electrical_label == "High":
        reasons.append("High electrical hazard")

    if maintenance == 1:
        reasons.append("Maintenance work in progress")

    if worker_score < 50:
        reasons.append("Low worker safety score")

    if len(reasons) == 0:
        reason = "Industrial conditions appear safe."
    else:
        reason = ", ".join(reasons)

    # -----------------------------
    # Prediction Time
    # -----------------------------
    prediction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # -----------------------------
    # Return Result
    # -----------------------------
    return {
        "Prediction_Time": prediction_time,
        "Explosion_Risk": explosion_label,
        "Fire_Risk": fire_label,
        "Gas_Leakage_Risk": gas_label,
        "Electrical_Hazard": electrical_label,
        "Worker_Safety_Score": worker_score,
        "Risk_Score": risk_score,
        "Status": status,
        "Reason": reason
    }


# -----------------------------
# Test
# -----------------------------
if __name__ == "__main__":

    sample = {
        "Gas_Level": 53.37,
        "Temperature": 72.18,
        "Pressure": 8.41,
        "Humidity": 59,
        "Worker_Count": 18,
        "Maintenance_Status": "Yes",
        "Permit_Type": "Normal",
        "Shift": "Morning"
    }

    result = predict_risk(sample)

    print("\nPrediction Result\n")
    print(result)