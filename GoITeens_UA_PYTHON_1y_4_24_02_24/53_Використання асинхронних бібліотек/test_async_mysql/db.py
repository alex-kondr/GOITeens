import os

from sqlalchemy import String, Integer, Table, create_engine, MetaData, Column
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from dotenv import load_dotenv
from databases import Database


load_dotenv()
SQLALCHEMY_URI = os.getenv("SQLALCHEMY_URI")
engine = create_engine(SQLALCHEMY_URI, echo=True)
database = Database(SQLALCHEMY_URI)
metadata = MetaData()
Base = declarative_base(metadata=metadata)

users = Table(
    "users",
    metadata,
    Column("id", Integer(), primary_key=True, autoincrement=True),
    Column("name", String(50))
)


class People(Base):
    __tablename__ = "people"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    username: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(500))


def create_db():
    metadata.create_all(bind=engine)
