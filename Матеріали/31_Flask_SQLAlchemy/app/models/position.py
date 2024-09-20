from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.associates import cabinet_position_assoc_table


class Position(Base):
    __tablename__ = "positions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    cabinets: Mapped[List["Cabinet"]] = relationship(secondary=cabinet_position_assoc_table)

    def __repr__(self):
        return f"Назва посади: {self.name}"

    def __str__(self):
        return self.name
