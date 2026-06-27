from fastapi import FastAPI
from app.routers import orders
from app.routers import auth
from app.routers import restaurants
from app.routers import menu

app = FastAPI(
    title="Deori Eats",
    description="Food Delivery API for Deori Eats",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(restaurants.router)
app.include_router(menu.router)
app.include_router(orders.router)

@app.get("/")
def home():
    return {
        "app": "Deori Eats",
        "status": "running"
    }