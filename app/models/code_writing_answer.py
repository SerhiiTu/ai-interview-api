from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class CodeWritingAnswer(Base):
    __tablename__ = "code_writing_answers"

    id: Mapped[int] = mapped_column(
        ForeignKey("user_answers.id", ondelete="CASCADE"),
        primary_key=True,
        autoincrement=False,
    )
    code: Mapped[str] = mapped_column(Text, nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=False)
