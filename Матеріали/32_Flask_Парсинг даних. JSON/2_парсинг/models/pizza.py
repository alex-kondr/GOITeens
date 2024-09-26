from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.ingredient import Ingredient
from models.assoiates import pizza_ingredient_assoc_table


class Pizza(Base):
    __tablename__ = "pizzas"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[float] = mapped_column()
    ingredients: Mapped[List[Ingredient]] = relationship(secondary=pizza_ingredient_assoc_table)
