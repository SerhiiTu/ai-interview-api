from sqlalchemy import ForeignKey, Integer, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class SessionStep(Base):
    __tablename__ = "session_steps"
    __table_args__ = (
        UniqueConstraint(
            "interview_session_id",
            "number",
            name="uq_session_steps_session_number",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    interview_session_id: Mapped[int] = mapped_column(
        ForeignKey("interview_sessions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    number: Mapped[int] = mapped_column(Integer, nullable=False)
    raw_ai_question: Mapped[str] = mapped_column(Text, nullable=False)
    type: Mapped[int] = mapped_column(Integer, nullable=False)
    importance_level: Mapped[int] = mapped_column(Integer, nullable=False)
    difficulty_level: Mapped[int] = mapped_column(Integer, nullable=False)
