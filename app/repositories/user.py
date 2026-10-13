from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.schemas import UserCreate, UserUpdate


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> Sequence[User]:
        result = await self.db.execute(
            select(User)
        )

        return result.scalars().all()

    async def get_by_id(self, user_id: int) -> User | None:
        result = await self.db.execute(
            select(User).where(
                User.id == user_id
            )
        )

        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> User | None:
        result = await self.db.execute(
            select(User).where(
                User.email == email
            )
        )

        return result.scalar_one_or_none()

    async def create(self, user_data: UserCreate) -> User:
        user = User(
            email=user_data.email,
            password_hash=user_data.password_hash,
            role=user_data.role,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            birth_date=user_data.birth_date,
            phone=user_data.phone,
            email_verified_at=user_data.email_verified_at,
        )

        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)

        return user

    async def update(self, user: User, user_data: UserUpdate) -> User:
        update_data = user_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(user, field, value)

        await self.db.commit()
        await self.db.refresh(user)

        return user

    async def delete(self, user: User) -> None:
        await self.db.delete(user)
        await self.db.commit()