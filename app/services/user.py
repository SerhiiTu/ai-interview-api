from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import UserRepository
from app.schemas import UserCreate, UserUpdate


class UserService:
    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)

    async def get_all(self):
        return await self.repository.get_all()

    async def get_by_id(self, user_id: int):
        return await self.repository.get_by_id(user_id)

    async def create(self, user_data: UserCreate):
        existing_user = await self.repository.get_by_email(
            user_data.email
        )

        if existing_user is not None:
            return None # потом поменять на норм ошибку

        return await self.repository.create(user_data)

    async def update(self, user_id: int, user_data: UserUpdate):
        user = await self.repository.get_by_id(user_id)

        if user is None:
            return None

        return await self.repository.update(
            user,
            user_data,
        )

    async def delete(self, user_id: int) -> bool:
        user = await self.repository.get_by_id(user_id)

        if user is None:
            return False

        await self.repository.delete(user)

        return True