from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .position import Position
from .associates import cabinet_position_assoc_table


class Cabinet(Base):
    __tablename__ = "cabinets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    positions: Mapped[List[Position]] = relationship(secondary=cabinet_position_assoc_table)

    def __repr__(self) -> str:
        return f"Назва кабінету: {self.name}"

    def __str__(self) -> str:
        return self.name.capitalize()
