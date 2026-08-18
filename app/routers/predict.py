from fastapi import APIRouter

from app.schemas import PredictInput, PredictionResponse, StatsResponse
from app.services.prediction_service import get_request_count, predict_passenger


router = APIRouter(tags=["prediction"])


@router.get("/stats", response_model=StatsResponse)
def stats():
    return {"request_count": get_request_count()}


@router.post("/predict_model", response_model=PredictionResponse)
def predict_model(input_data: PredictInput):
    return predict_passenger(input_data)
