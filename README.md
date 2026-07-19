# Compound Risk Detection Engine

## Overview

Compound Risk Detection Engine is an AI-powered Industrial Safety Risk Prediction System developed using Machine Learning and FastAPI.

The system predicts multiple industrial safety risks based on environmental and operational parameters.

---

## Features

- Explosion Risk Prediction
- Fire Risk Prediction
- Gas Leakage Risk Prediction
- Electrical Hazard Prediction
- Worker Safety Score Prediction
- Overall Risk Score
- Risk Status
- Reason Generation
- REST API using FastAPI
- Interactive Swagger Documentation

---

## Technologies Used

- Python
- Pandas
- Scikit-Learn
- Joblib
- FastAPI
- Uvicorn
- Jupyter Notebook

---

## Project Structure

```
CompoundRiskDetectionEngine/
│
├── api/
│   ├── main.py
│   ├── predict.py
│   └── schemas.py
│
├── dataset/
│   └── industrial_safety.csv
│
├── notebooks/
│   ├── dataset_generation.ipynb
│   ├── EDA.ipynb
│   └── model_training.ipynb
│
├── saved_models/
│   ├── explosion_risk_model.pkl
│   ├── fire_risk_model.pkl
│   ├── gas_leakage_model.pkl
│   ├── electrical_hazard_model.pkl
│   └── worker_safety_model.pkl
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn api.main:app --reload
```

---

## API Documentation

Open:

```
http://127.0.0.1:8000/docs
```

---

## Sample Input

```json
{
  "Gas_Level": 53.37,
  "Temperature": 72.18,
  "Pressure": 8.41,
  "Humidity": 59,
  "Worker_Count": 18,
  "Maintenance_Status": "Yes",
  "Permit_Type": "Normal",
  "Shift": "Morning"
}
```

---

## Sample Output

```json
{
  "Prediction_Time": "2026-07-19 15:17:21",
  "Explosion_Risk": "Low",
  "Fire_Risk": "Medium",
  "Gas_Leakage_Risk": "Medium",
  "Electrical_Hazard": "High",
  "Worker_Safety_Score": 60,
  "Risk_Score": 49,
  "Status": "Medium",
  "Reason": "High electrical hazard, Maintenance work in progress"
}
```

---

## Future Improvements

- Database Integration
- User Authentication
- Dashboard Visualization
- Cloud Deployment
- Real-time Sensor Integration

---

## Author

Akshitha Dusa