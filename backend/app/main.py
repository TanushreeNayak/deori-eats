from fastapi import FastAPI

app = FastAPI(
    title="Deori Eats API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "app": "Deori Eats",
        "status": "running"
    }