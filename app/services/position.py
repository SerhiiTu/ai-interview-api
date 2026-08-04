from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import PositionRepository
from app.schemas import PositionCreate, PositionUpdate


class PositionService:
    def __init__(self, db: AsyncSession):
        self.repository = PositionRepository(db)

    async def get_all(self):
        return await self.repository.get_all()

    async def get_by_id(self, position_id: int):
        return await self.repository.get_by_id(position_id)

    async def create(self, position_data: PositionCreate):
        return await self.repository.create(position_data)

    async def update(self, position_id: int, position_data: PositionUpdate):
        position = await self.repository.get_by_id(position_id)

        if position is None:
            return None

        return await self.repository.update(
            position,
            position_data,
        )

    async def delete(self, position_id: int) -> bool:
        position = await self.repository.get_by_id(position_id)

        if position is None:
            return False

        await self.repository.delete(position)

        return True