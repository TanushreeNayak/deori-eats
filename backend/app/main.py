from fastapi import FastAPI
from app.routers import auth

app = FastAPI(
    title="Deori Eats API",
    version="1.0.0"
)

app.include_router(auth.router)

@app.get("/")
def home():
    return {"app": "Deori Eats", "status": "running"}