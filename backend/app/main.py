from backend.app.routers import restaurants
from fastapi import FastAPI
from app.routers import auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(restaurants.router)

@app.get("/")
def home():
    return {"app": "Deori Eats", "status": "running"}