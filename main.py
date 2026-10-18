from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from delivery import load_model
from validate import is_valid_order
import pandas as pd

app = FastAPI(title="Delivery Time Prediction API")

model = load_model("model.joblib")


class Order(BaseModel):
    distance_km: float = Field(gt=0)
    prep_time_min: float = Field(ge=0)
    traffic_level: int = Field(ge=1, le=3)
    rain: int = Field(ge=0, le=1)



@app.get("/")
def home():
    return {"message": "Delivery Time Prediction API is running"}


@app.post("/predict")
def predict(order: Order):
    order_data = {
        "distance_km": order.distance_km,
        "prep_time_min": order.prep_time_min,
        "traffic_level": order.traffic_level,
        "rain": order.rain,
    }

    if not is_valid_order(order_data):
        raise HTTPException(
            status_code=400,
            detail="Invalid delivery order"
        )

    features = pd.DataFrame([order_data])
    minutes = model.predict(features)[0]

    return {
        "predicted_delivery_minutes": round(float(minutes), 1)
    }
