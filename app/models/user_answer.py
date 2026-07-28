from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class UserAnswer(Base):
    __tablename__ = "user_answers"

    id: Mapped[int] = mapped_column(primary_key=True)
    session_step_id: Mapped[int] = mapped_column(
        ForeignKey("session_steps.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    type: Mapped[str | None] = mapped_column(String(45), nullable=True)
    score: Mapped[int | None] = mapped_column(Integer, nullable=True)
