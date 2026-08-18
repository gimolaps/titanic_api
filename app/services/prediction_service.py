from pathlib import Path

import joblib
import pandas as pd

from app.schemas import PredictInput


BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "models" / "random_forest_titanic.pkl"

model = joblib.load(MODEL_PATH)
request_count = 0


def get_request_count() -> int:
    return request_count


def predict_passenger(input_data: PredictInput) -> dict:
    global request_count
    request_count += 1

    new_data = pd.DataFrame({
        "Age": [input_data.Age],
        "Fare": [input_data.Fare],
        "Embarked_C": [input_data.Embarked == "C"],
        "Embarked_Q": [input_data.Embarked == "Q"],
        "Embarked_S": [input_data.Embarked == "S"],
        "Sex_female": [input_data.Sex == "female"],
        "Sex_male": [input_data.Sex == "male"],
        "Pclass_1": [input_data.Pclass == 1],
        "Pclass_2": [input_data.Pclass == 2],
        "Pclass_3": [input_data.Pclass == 3],
        "FamilySize": [input_data.FamilySize],
        "IsAlone": [int(input_data.IsAlone)],
    })

    prediction = model.predict(new_data)
    result = "Survived" if prediction[0] == 1 else "Not survived"

    return {
        "Prediction": result,
        "request_count": request_count,
    }
