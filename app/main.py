from fastapi import FastAPI
from app.routers import health
from app.routers import position

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

app.include_router(health.router)
app.include_router(position.router)