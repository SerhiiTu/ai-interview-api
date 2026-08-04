from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Position
from app.schemas import PositionCreate, PositionUpdate


class PositionRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> Sequence[Position]:
        result = await self.db.execute(
            select(Position)
        )

        return result.scalars().all()

    async def get_by_id(self, position_id: int) -> Position | None:
        result = await self.db.execute(
            select(Position).where(
                Position.id == position_id
            )
        )

        return result.scalar_one_or_none()

    async def create(self, position_data: PositionCreate) -> Position:
        position = Position(
            name=position_data.name,
            description=position_data.description,
        )

        self.db.add(position)
        await self.db.commit()
        await self.db.refresh(position)

        return position

    async def update(self, position: Position, position_data: PositionUpdate) -> Position:
        update_data = position_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(position, field, value)

        await self.db.commit()
        await self.db.refresh(position)

        return position

    async def delete(self,position: Position) -> None:
        await self.db.delete(position)
        await self.db.commit()