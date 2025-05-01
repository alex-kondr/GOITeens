import token
from typing import List, Optional, Union
import os

from sqlalchemy import create_engine, String
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, Session
from databases import Database
from dotenv import load_dotenv


load_dotenv()

SQLALCHEMY_URI = os.getenv("SQLALCHEMY_URI")
Base = declarative_base()
database = Database(SQLALCHEMY_URI)
engine = create_engine(SQLALCHEMY_URI, echo=True)
# session = Session(bind=engine)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, default=None)
    password: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(500), unique=True)
    token: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, default=None)



# Base.metadata.create_all(engine)

async def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()