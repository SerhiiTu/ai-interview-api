from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings


# Базовый класс для всех моделей
class Base(DeclarativeBase):
    pass


# Создаем подключение к PostgreSQL
engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
)


# Фабрика асинхронных сессий
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# Dependency для FastAPI
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session