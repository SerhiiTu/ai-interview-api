from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class SubsphereSpecialization(Base):
    __tablename__ = "subsphere_specializations"

    subsphere_id: Mapped[int] = mapped_column(
        ForeignKey("subspheres.id", ondelete="CASCADE"),
        primary_key=True,
    )
    specialization_id: Mapped[int] = mapped_column(
        ForeignKey("specializations.id", ondelete="CASCADE"),
        primary_key=True,
        index=True,
    )
