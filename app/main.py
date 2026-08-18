from fastapi import FastAPI

from app.routers.predict import router as predict_router


app = FastAPI(title="Titanic Prediction API")

app.include_router(predict_router)


@app.get("/health")
def health():
    return {"status": "OK"}
