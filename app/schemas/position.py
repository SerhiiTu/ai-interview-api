from pydantic import BaseModel, ConfigDict


class PositionCreate(BaseModel):
    name: str
    description: str


class PositionUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class PositionResponse(BaseModel):
    id: int
    name: str
    description: str

    model_config = ConfigDict(from_attributes=True)