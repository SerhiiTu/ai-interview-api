from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/db")
async def check_database(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))

    return {
        "status": "ok",
        "database": result.scalar(),
    }