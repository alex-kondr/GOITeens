import os
from typing import Optional

from dotenv import load_dotenv
from sqlalchemy import create_engine, String
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from databases import Database


load_dotenv()
SQLALCHEMY_URI = os.getenv("SQLALCHEMY_URI")
engine = create_engine(SQLALCHEMY_URI, echo=True)
database = Database(SQLALCHEMY_URI)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    address: Mapped[Optional[str]] = mapped_column(String(255), nullable=True, default=None)


# Base.metadata.create_all(bind=engine)
