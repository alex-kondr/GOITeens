from typing import List

from sqlalchemy import String, ForeignKey, Table, Column, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin

from data.base import db, Base


class Tour(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = "tours"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(100))
    departure: Mapped[str] = mapped_column(String(50))
    picture: Mapped[str] = mapped_column(String(500))
    price: Mapped[int] = mapped_column()
    stars: Mapped[str] = mapped_column(String(10))
    country: Mapped[str] = mapped_column(String(50))
    nights: Mapped[str] = mapped_column(String(10))
    date: Mapped[str] = mapped_column(String(50))


tour_user_assoc = Table(
    "tour_user_assoc",
    Base.metadata,
    Column("tour_id", ForeignKey("tours.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    extend_existing=True
)


class User(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    email: Mapped[str] = mapped_column(String(500), unique=True)
    email_isvalid: Mapped[bool] = mapped_column(Boolean(), default=False, server_default='true')
    email_pass_validator: Mapped[str] = mapped_column(String(500), nullable=True, default=None)
    password: Mapped[str] = mapped_column(String(500))
    tours: Mapped[List[Tour]] = relationship(secondary=tour_user_assoc)
