from typing import List, Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.position import Position
from app.models.associates import employee_position_assoc_table


class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[Optional[str]]
    age: Mapped[int] = mapped_column()
    salary: Mapped[int] = mapped_column()
    positions: Mapped[List[Position]] = relationship(secondary=employee_position_assoc_table)

    def __repr__(self):
        positions = [position.name for position in self.positions]
        positions = ", ".join(positions)
        return f"Працівник: {self.last_name} {self.first_name}\n"\
               f"Вік: {self.age}\n"\
               f"Обов'язки: {positions}\n"\
               f"Зарплатня: {self.salary}"
