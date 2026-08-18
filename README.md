# Titanic Survival Prediction API

A small machine learning project that predicts whether a Titanic passenger would survive based on passenger information.

The project includes:

* a trained **Random Forest** classification model;
* a **FastAPI** backend for model inference;
* a simple **Streamlit** web interface;
* Docker support;
* a structured project architecture separating API routes, schemas, and prediction logic.

## Project Structure

```text
titanic_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── predict.py
│   │
│   └── services/
│       ├── __init__.py
│       └── prediction_service.py
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
├── streamlit_app.py
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

## Tech Stack

* Python
* FastAPI
* Streamlit
* Scikit-learn
* Pandas
* Joblib
* Uvicorn
* Docker

## How It Works

The application follows this flow:

```text
User
 ↓
Streamlit Web App
 ↓
FastAPI
 ↓
Prediction Service
 ↓
Random Forest Model
 ↓
Prediction
 ↓
API Response
 ↓
Streamlit Result
```

The trained model is stored in:

```text
models/random_forest_titanic.pkl
```

The API loads the model and uses it to make predictions from passenger data sent by the client.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd titanic_api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run FastAPI

Start the backend from the project root:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 5000
```

The API will be available at:

```text
http://127.0.0.1:5000
```

Swagger documentation:

```text
http://127.0.0.1:5000/docs
```

## API Endpoints

### Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "ok"
}
```

### Prediction

```http
POST /predict_model
```

Sends passenger information to the trained model and returns a survival prediction.

### Statistics

```http
GET /stats
```

Returns basic API usage statistics.

## Run Streamlit

Keep the FastAPI server running and open another terminal.

Run:

```bash
streamlit run streamlit_app.py
```

The web interface will usually be available at:

```text
http://localhost:8501
```

The Streamlit application sends requests to the FastAPI backend and displays the model prediction.

## Run with Docker

Build the Docker image:

```bash
docker build -t titanic-service .
```

Run the container:

```bash
docker run -p 5000:5000 titanic-service
```

Then open:

```text
http://localhost:5000/docs
```

## Machine Learning

The model was trained on the Titanic dataset as a binary classification task.

Target:

```text
Survived
```

The model predicts one of two classes:

```text
0 → Did not survive
1 → Survived
```

The training and experimentation process can be found in:

```text
notebooks/tests_&_train.ipynb
```

## Project Purpose

This is an educational project created to practice the complete ML application workflow:

```text
Dataset
→ Data preprocessing
→ Model training
→ Model evaluation
→ Model serialization
→ FastAPI inference service
→ Web interface
→ Docker containerization
```

The main goal is to demonstrate how a trained machine learning model can be integrated into a structured API service and exposed through a simple user interface.
