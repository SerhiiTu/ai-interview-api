from sqlalchemy import ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Interview(Base):
    __tablename__ = "interviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    position_id: Mapped[int] = mapped_column(
        ForeignKey("positions.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    specialization_id: Mapped[int] = mapped_column(
        ForeignKey("specializations.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    language: Mapped[int] = mapped_column(Integer, nullable=False)
    difficulty_level: Mapped[int] = mapped_column(Integer, nullable=False)
    time: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[int] = mapped_column(Integer, nullable=False)
    result: Mapped[int | None] = mapped_column(SmallInteger, nullable=True)
