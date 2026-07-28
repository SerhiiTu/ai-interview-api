from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class TheoreticalAnswer(Base):
    __tablename__ = "theoretical_answers"

    id: Mapped[int] = mapped_column(
        ForeignKey("user_answers.id", ondelete="CASCADE"),
        primary_key=True,
        autoincrement=False,
    )
    text: Mapped[str] = mapped_column(Text, nullable=False)
