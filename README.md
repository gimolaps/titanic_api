# Titanic Survival Prediction API

FastAPI-сервис для предсказания выживания пассажира Titanic с помощью обученной модели Random Forest.

## Структура

```text
titanic_api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── predict.py
│   └── services/
│       ├── __init__.py
│       └── prediction_service.py
├── models/
│   └── random_forest_titanic.pkl
├── data/
│   └── titanic.csv
├── notebooks/
│   └── tests_&_train.ipynb
├── streamlit_app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## Локальный запуск API

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 5000
```

Swagger:

```text
http://127.0.0.1:5000/docs
```

Endpoints:

- `GET /health`
- `GET /stats`
- `POST /predict_model`

Пример запроса:

```json
{
  "Age": 18,
  "Fare": 50,
  "Embarked": "S",
  "Sex": "male",
  "Pclass": 3,
  "FamilySize": 1,
  "IsAlone": false
}
```

## Streamlit

API должен быть запущен на порту `5000`.

```powershell
streamlit run streamlit_app.py --server.address 127.0.0.1
```

## Docker

```powershell
docker build -t titanic-service .
docker run --rm -p 5000:5000 titanic-service
```
