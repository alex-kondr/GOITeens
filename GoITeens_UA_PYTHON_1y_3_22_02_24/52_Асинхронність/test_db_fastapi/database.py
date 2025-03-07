from typing import Optional

from sqlalchemy import String, create_engine, Table, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from databases import Database


DATABASE_URL = "sqlite:///test.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
database = Database(DATABASE_URL)


# class User(Base):
#     __tablename__ = "users"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String())
#     age: Mapped[Optional[int]] = mapped_column(default=None, nullable=True)


users = Table(
    "users",
    Base.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("name", String),
    Column("age", Integer, nullable=True, default=None)
)


def create_db():
    Base.metadata.create_all(bind=engine)

