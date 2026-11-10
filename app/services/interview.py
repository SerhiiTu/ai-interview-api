from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import (
    InterviewRepository,
    PositionRepository,
    SpecializationRepository,
    UserRepository,
)
from app.schemas import InterviewCreate, InterviewUpdate

from app.exceptions.interview import InterviewNotFoundError
from app.exceptions.position import PositionNotFoundError
from app.exceptions.specialization import SpecializationNotFoundError
from app.exceptions.user import UserNotFoundError


class InterviewService:
    def __init__(self, db: AsyncSession):
        self.repository = InterviewRepository(db)
        self.user_repository = UserRepository(db)
        self.position_repository = PositionRepository(db)
        self.specialization_repository = SpecializationRepository(db)

    async def get_all(self):
        return await self.repository.get_all()

    async def get_by_id(self, interview_id: int):
        interview = await self.repository.get_by_id(interview_id)

        if interview is None:
            raise InterviewNotFoundError("Interview not found")

        return interview

    async def create(self, interview_data: InterviewCreate):
        await self._validate_references(
            interview_data.user_id,
            interview_data.position_id,
            interview_data.specialization_id,
        )

        return await self.repository.create(interview_data)

    async def update(self, interview_id: int, interview_data: InterviewUpdate):
        interview = await self.repository.get_by_id(interview_id)

        if interview is None:
            raise InterviewNotFoundError("Interview not found")

        await self._validate_references(
            interview_data.user_id,
            interview_data.position_id,
            interview_data.specialization_id,
        )

        return await self.repository.update(
            interview,
            interview_data,
        )

    async def delete(self, interview_id: int) -> None:
        interview = await self.repository.get_by_id(interview_id)

        if interview is None:
            raise InterviewNotFoundError("Interview not found")

        await self.repository.delete(interview)

    async def _validate_references(
        self,
        user_id: int | None,
        position_id: int | None,
        specialization_id: int | None,
    ) -> None:
        if user_id is not None:
            user = await self.user_repository.get_by_id(user_id)

            if user is None:
                raise UserNotFoundError("User not found")

        if position_id is not None:
            position = await self.position_repository.get_by_id(position_id)

            if position is None:
                raise PositionNotFoundError("Position not found")

        if specialization_id is not None:
            specialization = await self.specialization_repository.get_by_id(specialization_id)

            if specialization is None:
                raise SpecializationNotFoundError("Specialization not found")
