from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import SpecializationRepository
from app.schemas import SpecializationCreate, SpecializationUpdate


class SpecializationService:
    def __init__(self, db: AsyncSession):
        self.repository = SpecializationRepository(db)

    async def get_all(self):
        return await self.repository.get_all()

    async def get_by_id(self, specialization_id: int):
        return await self.repository.get_by_id(specialization_id)

    async def create(self, specialization_data: SpecializationCreate):
        return await self.repository.create(specialization_data)

    async def update(
        self,
        specialization_id: int,
        specialization_data: SpecializationUpdate,
    ):
        specialization = await self.repository.get_by_id(specialization_id)

        if specialization is None:
            return None

        return await self.repository.update(
            specialization,
            specialization_data,
        )

    async def delete(self, specialization_id: int) -> bool:
        specialization = await self.repository.get_by_id(specialization_id)

        if specialization is None:
            return False

        await self.repository.delete(specialization)

        return True
