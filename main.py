from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"Docker 안에서 실행되는 Python 웹 서비스입니다.",
        "environment":os.getenv("APP_ENV", "local")
    }

@app.get("/health")
def health():
    return {"status": "ok"}