from fastapi import FastAPI
from app.routers import auth, restaurants, menu

app = FastAPI()

app.include_router(auth.router)
app.include_router(restaurants.router)
app.include_router(menu.router)

@app.get("/")
def home():
    return {
        "app": "Deori Eats",
        "status": "running"
    }