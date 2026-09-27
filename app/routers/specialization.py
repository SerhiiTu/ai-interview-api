from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas import (
    SpecializationCreate,
    SpecializationResponse,
    SpecializationUpdate,
)
from app.services import SpecializationService


router = APIRouter(
    prefix="/specializations",
    tags=["Specializations"],
)


@router.get("/", response_model=list[SpecializationResponse])
async def get_specializations(db: AsyncSession = Depends(get_db)):
    service = SpecializationService(db)

    return await service.get_all()


@router.get("/{specialization_id}", response_model=SpecializationResponse)
async def get_specialization(
    specialization_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = SpecializationService(db)

    specialization = await service.get_by_id(specialization_id)

    if specialization is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Specialization not found",
        )

    return specialization


@router.post(
    "/",
    response_model=SpecializationResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_specialization(
    specialization_data: SpecializationCreate,
    db: AsyncSession = Depends(get_db),
):
    service = SpecializationService(db)

    return await service.create(specialization_data)


@router.patch("/{specialization_id}", response_model=SpecializationResponse)
async def update_specialization(
    specialization_id: int,
    specialization_data: SpecializationUpdate,
    db: AsyncSession = Depends(get_db),
):
    service = SpecializationService(db)

    specialization = await service.update(
        specialization_id,
        specialization_data,
    )

    if specialization is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Specialization not found",
        )

    return specialization


@router.delete("/{specialization_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_specialization(
    specialization_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = SpecializationService(db)

    deleted = await service.delete(specialization_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Specialization not found",
        )
