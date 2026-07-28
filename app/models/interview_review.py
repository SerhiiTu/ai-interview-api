from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class InterviewReview(Base):
    __tablename__ = "interview_reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    interview_id: Mapped[int] = mapped_column(
        ForeignKey("interviews.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
        index=True,
    )
    raw_ai_response: Mapped[str] = mapped_column(Text, nullable=False)
    final_score: Mapped[int] = mapped_column(Integer, nullable=False)
    general_feedback: Mapped[str] = mapped_column(Text, nullable=False)
    recommendations: Mapped[str] = mapped_column(Text, nullable=False)
    action_plan: Mapped[str] = mapped_column(Text, nullable=False)
