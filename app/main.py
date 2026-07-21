from fastapi import FastAPI
from app.routers.health import router as health_router

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

app.include_router(health_router)