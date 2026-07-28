from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class CodeWritingQuestion(Base):
    __tablename__ = "code_writing_questions"

    id: Mapped[int] = mapped_column(
        ForeignKey("session_steps.id", ondelete="CASCADE"),
        primary_key=True,
        autoincrement=False,
    )
    text: Mapped[str] = mapped_column(Text, nullable=False)
    base_code: Mapped[str] = mapped_column(Text, nullable=False)
