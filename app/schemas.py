from typing import Literal

from pydantic import BaseModel


class PredictInput(BaseModel):
    Age: float
    Fare: float
    Embarked: Literal["S", "C", "Q"]
    Sex: Literal["male", "female"]
    Pclass: Literal[1, 2, 3]
    FamilySize: int
    IsAlone: bool


class PredictionResponse(BaseModel):
    Prediction: str
    request_count: int


class StatsResponse(BaseModel):
    request_count: int
