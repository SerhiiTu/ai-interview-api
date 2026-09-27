from fastapi import FastAPI
from app.routers import health
from app.routers import position
from app.routers import specialization

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

app.include_router(health.router)
app.include_router(position.router)
app.include_router(specialization.router)
