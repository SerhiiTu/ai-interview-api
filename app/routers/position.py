from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas import PositionCreate, PositionResponse, PositionUpdate
from app.services import PositionService


router = APIRouter(
    prefix="/positions",
    tags=["Positions"],
)


@router.get("/", response_model=list[PositionResponse])
async def get_positions(db: AsyncSession = Depends(get_db)):
    service = PositionService(db)

    return await service.get_all()


@router.get("/{position_id}", response_model=PositionResponse)
async def get_position(position_id: int, db: AsyncSession = Depends(get_db)):
    service = PositionService(db)

    position = await service.get_by_id(position_id)

    if position is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Position not found",
        )

    return position


@router.post("/", response_model=PositionResponse, status_code=status.HTTP_201_CREATED)
async def create_position(position_data: PositionCreate, db: AsyncSession = Depends(get_db)):
    service = PositionService(db)

    return await service.create(position_data)


@router.patch("/{position_id}", response_model=PositionResponse)
async def update_position(position_id: int, position_data: PositionUpdate, db: AsyncSession = Depends(get_db)):
    service = PositionService(db)

    position = await service.update(
        position_id,
        position_data,
    )

    if position is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Position not found",
        )

    return position


@router.delete("/{position_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_position(position_id: int, db: AsyncSession = Depends(get_db)):
    service = PositionService(db)

    deleted = await service.delete(position_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Position not found",
        )