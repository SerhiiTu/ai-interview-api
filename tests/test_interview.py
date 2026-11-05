import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.enums.interview import InterviewStatus
from app.exceptions.interview import InterviewNotFoundError
from app.exceptions.position import PositionNotFoundError
from app.exceptions.specialization import SpecializationNotFoundError
from app.exceptions.user import UserNotFoundError
from app.models import Interview
from app.schemas import InterviewCreate, InterviewUpdate
from app.services import InterviewService


@pytest.fixture
def interview_data():
    return {
        "position_id": 1,
        "user_id": 1,
        "specialization_id": 1,
        "language": 1,
        "difficulty_level": 2,
        "time": 30,
    }


@pytest.fixture
def service():
    service = InterviewService(MagicMock(spec=AsyncSession))
    service.repository = AsyncMock()
    service.repository.get_by_id.return_value = Interview(id=1)
    service.user_repository = AsyncMock()
    service.position_repository = AsyncMock()
    service.specialization_repository = AsyncMock()

    return service


def test_create_requires_user_id(interview_data):
    del interview_data["user_id"]

    with pytest.raises(ValidationError):
        InterviewCreate(**interview_data)


def test_new_interview_has_initial_status_and_no_result(interview_data):
    interview = InterviewCreate(**interview_data)

    assert interview.status == InterviewStatus.CREATED
    assert interview.result is None


@pytest.mark.parametrize(
    "field",
    ["position_id", "user_id", "specialization_id", "language", "difficulty_level", "time", "status"],
)
def test_update_rejects_null_for_required_fields(field):
    with pytest.raises(ValidationError):
        InterviewUpdate(**{field: None})


def test_update_distinguishes_omitted_result_from_explicit_null():
    assert InterviewUpdate(time=45).model_dump(exclude_unset=True) == {"time": 45}
    assert InterviewUpdate(result=None).model_dump(exclude_unset=True) == {"result": None}
    assert InterviewUpdate().model_dump(exclude_unset=True) == {}


@pytest.mark.parametrize("method", ["get_by_id", "update", "delete"])
def test_missing_interview_raises_not_found(service, method):
    service.repository.get_by_id.return_value = None
    args = (999, InterviewUpdate(time=45)) if method == "update" else (999,)

    with pytest.raises(InterviewNotFoundError, match="Interview not found"):
        asyncio.run(getattr(service, method)(*args))

    service.repository.update.assert_not_awaited()
    service.repository.delete.assert_not_awaited()


@pytest.mark.parametrize("method", ["create", "update"])
@pytest.mark.parametrize(
    "field, repository, error",
    [
        ("user_id", "user_repository", UserNotFoundError),
        ("position_id", "position_repository", PositionNotFoundError),
        ("specialization_id", "specialization_repository", SpecializationNotFoundError),
    ],
)
def test_missing_reference_prevents_write(service, interview_data, method, field, repository, error):
    getattr(service, repository).get_by_id.return_value = None

    if method == "create":
        interview_data[field] = 999
        operation = service.create(InterviewCreate(**interview_data))
    else:
        operation = service.update(1, InterviewUpdate(**{field: 999}))

    with pytest.raises(error):
        asyncio.run(operation)

    service.repository.create.assert_not_awaited()
    service.repository.update.assert_not_awaited()
