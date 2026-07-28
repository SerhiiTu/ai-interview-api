from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class InterviewSphere(Base):
    __tablename__ = "interview_spheres"

    interview_id: Mapped[int] = mapped_column(
        ForeignKey("interviews.id", ondelete="CASCADE"),
        primary_key=True,
    )
    sphere_id: Mapped[int] = mapped_column(
        ForeignKey("spheres.id", ondelete="CASCADE"),
        primary_key=True,
        index=True,
    )
