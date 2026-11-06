from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Interview
from app.schemas import InterviewCreate, InterviewUpdate


class InterviewRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> Sequence[Interview]:
        result = await self.db.execute(
            select(Interview)
        )

        return result.scalars().all()

    async def get_by_id(self, interview_id: int) -> Interview | None:
        result = await self.db.execute(
            select(Interview).where(
                Interview.id == interview_id
            )
        )

        return result.scalar_one_or_none()

    async def create(self, interview_data: InterviewCreate) -> Interview:
        interview = Interview(
            position_id=interview_data.position_id,
            user_id=interview_data.user_id,
            specialization_id=interview_data.specialization_id,
            language=interview_data.language,
            difficulty_level=interview_data.difficulty_level,
            time=interview_data.time,
            status=interview_data.status,
            result=interview_data.result,
        )

        self.db.add(interview)
        await self.db.commit()
        await self.db.refresh(interview)

        return interview

    async def update(self, interview: Interview, interview_data: InterviewUpdate) -> Interview:
        update_data = interview_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(interview, field, value)

        await self.db.commit()
        await self.db.refresh(interview)

        return interview

    async def delete(self, interview: Interview) -> None:
        await self.db.delete(interview)
        await self.db.commit()
