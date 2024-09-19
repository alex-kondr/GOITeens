from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.position import Position
from app.models.associates import cabinet_position_assoc_table


class Cabinet(Base):
    __tablename__ = "cabinets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    positions: Mapped[List[Position]] = relationship(secondary=cabinet_position_assoc_table)

    def __repr__(self) -> str:
        return f"Назва кабінету: {self.name}"

    def __str__(self) -> str:
        return self.name.capitalize()
