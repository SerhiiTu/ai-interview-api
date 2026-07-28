from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Subsphere(Base):
    __tablename__ = "subspheres"

    id: Mapped[int] = mapped_column(primary_key=True)
    sphere_id: Mapped[int] = mapped_column(
        ForeignKey("spheres.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
