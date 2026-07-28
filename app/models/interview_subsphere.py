from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class InterviewSubsphere(Base):
    __tablename__ = "interview_subspheres"

    interview_id: Mapped[int] = mapped_column(
        ForeignKey("interviews.id", ondelete="CASCADE"),
        primary_key=True,
    )
    subsphere_id: Mapped[int] = mapped_column(
        ForeignKey("subspheres.id", ondelete="CASCADE"),
        primary_key=True,
        index=True,
    )
