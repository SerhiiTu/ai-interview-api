from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    email: str
    password_hash: str
    role: int
    first_name: str
    last_name: str
    birth_date: date | None = None
    phone: str | None = None
    email_verified_at: datetime | None = None


class UserUpdate(BaseModel):
    email: str | None = None
    password_hash: str | None = None
    role: int | None = None
    first_name: str | None = None
    last_name: str | None = None
    birth_date: date | None = None
    phone: str | None = None
    email_verified_at: datetime | None = None


class UserResponse(BaseModel):
    id: int
    email: str
    role: int
    first_name: str
    last_name: str
    birth_date: date | None
    phone: str | None
    email_verified_at: datetime | None

    model_config = ConfigDict(from_attributes=True)