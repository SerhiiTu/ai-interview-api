from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import UserRepository
from app.schemas import UserCreate, UserUpdate

from app.exceptions.user import (
    UserNotFoundError,
    EmailAlreadyExistsError
)


class UserService:
    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)

    async def get_all(self):
        return await self.repository.get_all()

    async def get_by_id(self, user_id: int):
        user = await self.repository.get_by_id(user_id)

        if user is None:
            raise UserNotFoundError("User not found")

        return user

    async def create(self, user_data: UserCreate):
        existing_user = await self.repository.get_by_email(
            user_data.email
        )

        if existing_user is not None:
            raise EmailAlreadyExistsError("User with this email already exists")

        return await self.repository.create(user_data)

    async def update(self, user_id: int, user_data: UserUpdate):
        user = await self.repository.get_by_id(user_id)

        if user is None:
            raise UserNotFoundError("User not found")

        return await self.repository.update(
            user,
            user_data,
        )

    async def delete(self, user_id: int) -> None:
        user = await self.repository.get_by_id(user_id)

        if user is None:
            raise UserNotFoundError("User not found")

        await self.repository.delete(user)