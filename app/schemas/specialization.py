from pydantic import BaseModel, ConfigDict


class SpecializationCreate(BaseModel):
    name: str
    description: str | None = None


class SpecializationUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class SpecializationResponse(BaseModel):
    id: int
    name: str
    description: str | None

    model_config = ConfigDict(from_attributes=True)
