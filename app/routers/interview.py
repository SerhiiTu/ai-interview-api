from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas import InterviewCreate, InterviewResponse, InterviewUpdate
from app.services import InterviewService


router = APIRouter(
    prefix="/interviews",
    tags=["Interviews"],
)


@router.get("/", response_model=list[InterviewResponse])
async def get_interviews(db: AsyncSession = Depends(get_db)):
    service = InterviewService(db)

    return await service.get_all()


@router.get("/{interview_id}", response_model=InterviewResponse)
async def get_interview(interview_id: int, db: AsyncSession = Depends(get_db)):
    service = InterviewService(db)

    return await service.get_by_id(interview_id)


@router.post("/", response_model=InterviewResponse, status_code=status.HTTP_201_CREATED)
async def create_interview(interview_data: InterviewCreate, db: AsyncSession = Depends(get_db)):
    service = InterviewService(db)

    return await service.create(interview_data)


@router.patch("/{interview_id}", response_model=InterviewResponse)
async def update_interview(interview_id: int, interview_data: InterviewUpdate, db: AsyncSession = Depends(get_db)):
    service = InterviewService(db)

    return await service.update(
        interview_id,
        interview_data,
    )


@router.delete("/{interview_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_interview(interview_id: int, db: AsyncSession = Depends(get_db)):
    service = InterviewService(db)

    await service.delete(interview_id)
