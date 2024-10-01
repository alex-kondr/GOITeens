from models.base import Base

from sqlalchemy import Column, Table, ForeignKey


pizza_ingred_assoc_table = Table(
    "pizza_ingred_assoc_table",
    Base.metadata,
    Column("pizza_id", ForeignKey("pizzas.id"), primary_key=True),
    Column("ingredient_id", ForeignKey("ingredients.id"), primary_key=True)
)
