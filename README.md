# Titanic Survival Prediction API

A Dockerized FastAPI machine learning service for Titanic passenger survival prediction.

The project uses a trained Random Forest model to predict whether a passenger would survive based on passenger attributes such as age, fare, sex, passenger class, embarkation port, family size and solo-travel status.

The application includes:

- REST API for model inference
- Web frontend for manual prediction
- Docker setup
- Cloud deployment support
- Clean backend structure with routers and services

---

## Project Overview

This project demonstrates a complete machine learning application workflow:

```text
dataset → preprocessing → trained model → API → frontend → Docker → cloud deployment
```

The main goal is not only to train a model, but to show how a machine learning model can be served as a usable web application.

The project is suitable as a portfolio example for:

- AI Engineer Intern
- ML Engineer Intern
- Junior AI Developer
- Junior Python Backend Developer with ML/AI focus

---

## Live Demo

Web app:

```text
https://titanic-api-eqep.onrender.com/
```

API documentation:

```text
https://titanic-api-eqep.onrender.com/docs
```

Health check:

```text
https://titanic-api-eqep.onrender.com/health
```

> Note: if the service is running on a free cloud instance, it may need time to wake up after inactivity.

---

## Tech Stack

| Area | Tools |
|---|---|
| Language | Python |
| Backend | FastAPI |
| Validation | Pydantic |
| Machine Learning | scikit-learn |
| Data Processing | pandas |
| Model Storage | joblib / pickle |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Docker, Render |
| API Docs | Swagger / OpenAPI |

---

## Features

- Predict Titanic passenger survival
- Clean REST API endpoint
- Interactive frontend form
- Input validation with Pydantic
- Health check endpoint
- Request statistics endpoint
- Dockerized application
- Cloud-ready configuration
- Swagger API documentation
- Separate backend and frontend structure

---

## Prediction Inputs

The model accepts the following passenger features:

| Feature | Type | Example | Description |
|---|---:|---|---|
| `Age` | number | `25` | Passenger age |
| `Fare` | number | `20.5` | Ticket fare |
| `Embarked` | string | `"S"` | Embarkation port |
| `Sex` | string | `"male"` | Passenger sex |
| `Pclass` | integer | `3` | Passenger class |
| `FamilySize` | integer | `1` | Number of family members |
| `IsAlone` | boolean | `true` | Whether passenger travelled alone |

Allowed values for `Embarked`:

```text
S - Southampton
C - Cherbourg
Q - Queenstown
```

Allowed values for `Sex`:

```text
male
female
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Web frontend |
| `GET` | `/health` | Health check |
| `GET` | `/stats` | Request counter |
| `POST` | `/predict_model` | Run survival prediction |
| `GET` | `/docs` | Swagger API documentation |

---

## Example API Request

```json
{
  "Age": 25,
  "Fare": 20,
  "Embarked": "S",
  "Sex": "male",
  "Pclass": 3,
  "FamilySize": 1,
  "IsAlone": true
}
```

---

## Example API Response

```json
{
  "Prediction": "Not survived",
  "request_count": 1
}
```

---

## Application Architecture

```text
User
│
├── Web frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── FastAPI backend
│   ├── main.py
│   ├── routers/
│   │   └── predict.py
│   └── services/
│       └── prediction_service.py
│
├── ML model
│   └── random_forest_titanic.pkl
│
└── Data
    └── titanic.csv
```

---

## Project Structure

```text
titanic_api/
│
├── app/
│   ├── frontend/
│   │   ├── index.html
│   │   ├── style.css
│   │   └── script.js
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── predict.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── prediction_service.py
│   │
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
│
├── data/
│   └── titanic.csv
│
├── models/
│   └── random_forest_titanic.pkl
│
├── notebooks/
│   └── tests_&_train.ipynb
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
└── streamlit_app.py
```

---

## Backend Design

The backend is separated into clear layers.

### `app/main.py`

Responsible for:

- creating the FastAPI application
- mounting the frontend
- connecting API routers
- exposing the health check endpoint

### `app/routers/predict.py`

Responsible for:

- `/predict_model` endpoint
- `/stats` endpoint
- request/response handling

### `app/services/prediction_service.py`

Responsible for:

- loading the trained model
- preparing input data
- running inference
- returning prediction results

### `app/schemas.py`

Responsible for:

- request validation
- response structure
- Pydantic models

This structure keeps the project easier to maintain and closer to real backend application design.

---

## Model Inference Flow

```text
User input
↓
Frontend form or API request
↓
FastAPI endpoint
↓
Pydantic validation
↓
Feature preparation
↓
Random Forest model inference
↓
Prediction result
↓
JSON response / frontend output
```

---

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/gimolaps/titanic_api.git
cd titanic_api
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn app.main:app --reload
```

Open the web app:

```text
http://127.0.0.1:8000/
```

Open Swagger docs:

```text
http://127.0.0.1:8000/docs
```

---

## Run with Docker

### 1. Build Docker image

```bash
docker build -t titanic-api .
```

### 2. Run Docker container

```bash
docker run -p 8000:8000 -e PORT=8000 titanic-api
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Docker Configuration

The project includes a Dockerfile for containerized deployment.

The container:

- uses Python 3.11
- installs project dependencies
- copies application files
- exposes the FastAPI service
- supports dynamic cloud port through the `PORT` environment variable

Start command:

```dockerfile
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
```

This makes the project compatible with cloud platforms such as Render, Railway, AWS App Runner and similar services.

---

## Frontend

The project includes a separate frontend interface located in:

```text
app/frontend/
```

The frontend provides:

- passenger input form
- dropdowns for categorical features
- prediction button
- loading state
- prediction result block
- links to API documentation and health check

This makes the project usable without directly calling the API from Swagger or Postman.

---

## Example cURL Request

```bash
curl -X POST "http://127.0.0.1:8000/predict_model" \
  -H "Content-Type: application/json" \
  -d "{\"Age\":25,\"Fare\":20,\"Embarked\":\"S\",\"Sex\":\"male\",\"Pclass\":3,\"FamilySize\":1,\"IsAlone\":true}"
```

---

## Cloud Deployment

This project is prepared for cloud deployment with Docker.

Current deployment target:

```text
Render Web Service
```

General deployment flow:

```text
GitHub repository
↓
Dockerfile
↓
Cloud build
↓
FastAPI app
↓
Public URL
```

The same containerized structure can also be adapted for:

- AWS App Runner
- AWS ECS / Fargate
- Railway
- Google Cloud Run
- Azure Container Apps

---

## Limitations

This project is focused on demonstrating the engineering workflow of serving a machine learning model as an API.

The prediction quality depends on:

- dataset size
- selected features
- preprocessing quality
- model choice
- training strategy
- class imbalance in the original data

Possible improvements:

- improve feature engineering
- add cross-validation reports
- compare multiple models
- add model metrics to README
- add automated tests
- add GitHub Actions CI pipeline
- add PostgreSQL prediction history
- add request logging
- add monitoring basics

---

## Current Status

Implemented:

- FastAPI backend
- Random Forest model inference
- Pydantic request validation
- Web frontend
- Docker setup
- Render deployment
- Health check endpoint
- Request statistics endpoint
- Swagger documentation

Planned improvements:

- Add `pytest` tests
- Add GitHub Actions
- Add model metrics section
- Add screenshots
- Add database for prediction history
- Add logging

---

## Skills Demonstrated

This project demonstrates practical AI engineering and backend development skills:

- serving a trained ML model through an API
- building REST endpoints with FastAPI
- using Pydantic for input validation
- structuring a Python backend application
- separating frontend, routing and service logic
- using Docker for reproducible deployment
- preparing an ML service for cloud deployment
- working with model artifacts
- exposing a usable web interface for inference

---

## Author

**Vladyslav Petrov**

GitHub: [gimolaps](https://github.com/gimolaps)
