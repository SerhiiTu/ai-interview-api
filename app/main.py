from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.common import (
    ObjectNotFoundError,
    ResourceConflictError
)

from app.routers import health
from app.routers import position
from app.routers import specialization
from app.routers import user

app = FastAPI()

@app.exception_handler(ObjectNotFoundError)
async def object_not_found_handler(request: Request, exc: ObjectNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)},
    )

@app.exception_handler(ResourceConflictError)
async def resource_conflict_handler(request: Request, exc: ResourceConflictError):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc)},
    )

@app.get("/")
def root():
    return {"message": "Hello World"}

app.include_router(health.router)
app.include_router(position.router)
app.include_router(specialization.router)
app.include_router(user.router)
