from typing import List, Union, Optional
import os

from sqlalchemy import String, create_engine
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from databases import Database
from dotenv import load_dotenv


load_dotenv()
SQLALCHEMY_URI = os.getenv("SQLALCHEMY_URI")
engine = create_engine(SQLALCHEMY_URI, echo=True)
database = Database(SQLALCHEMY_URI)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, default=None)
    email: Mapped[str] = mapped_column(String(250), unique=True)


# Base.metadata.create_all(bind=engine)
