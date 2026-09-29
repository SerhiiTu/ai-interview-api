from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Specialization
from app.schemas import SpecializationCreate, SpecializationUpdate


class SpecializationRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> Sequence[Specialization]:
        result = await self.db.execute(
            select(Specialization)
        )

        return result.scalars().all()

    async def get_by_id(self, specialization_id: int) -> Specialization | None:
        result = await self.db.execute(
            select(Specialization).where(
                Specialization.id == specialization_id
            )
        )

        return result.scalar_one_or_none()

    async def create(self, specialization_data: SpecializationCreate) -> Specialization:
        specialization = Specialization(
            name=specialization_data.name,
            description=specialization_data.description,
        )

        self.db.add(specialization)
        await self.db.commit()
        await self.db.refresh(specialization)

        return specialization

    async def update(
        self,
        specialization: Specialization,
        specialization_data: SpecializationUpdate,
    ) -> Specialization:
        update_data = specialization_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(specialization, field, value)

        await self.db.commit()
        await self.db.refresh(specialization)

        return specialization

    async def delete(self, specialization: Specialization) -> None:
        await self.db.delete(specialization)
        await self.db.commit()
