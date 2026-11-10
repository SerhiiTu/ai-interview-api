from pydantic import BaseModel, ConfigDict, field_validator

from app.enums.interview import InterviewStatus


class InterviewCreate(BaseModel):
    position_id: int
    user_id: int
    specialization_id: int
    language: int
    difficulty_level: int
    time: int
    status: int = InterviewStatus.CREATED
    result: int | None = None


class InterviewUpdate(BaseModel):
    position_id: int | None = None
    user_id: int | None = None
    specialization_id: int | None = None
    language: int | None = None
    difficulty_level: int | None = None
    time: int | None = None
    status: int | None = None
    result: int | None = None

    @field_validator(
        "position_id",
        "user_id",
        "specialization_id",
        "language",
        "difficulty_level",
        "time",
        "status",
    )
    @classmethod
    def validate_not_null(cls, value: int | None) -> int:
        if value is None:
            raise ValueError("Field cannot be null")

        return value


class InterviewResponse(BaseModel):
    id: int
    position_id: int
    user_id: int
    specialization_id: int
    language: int
    difficulty_level: int
    time: int
    status: int
    result: int | None

    model_config = ConfigDict(from_attributes=True)
