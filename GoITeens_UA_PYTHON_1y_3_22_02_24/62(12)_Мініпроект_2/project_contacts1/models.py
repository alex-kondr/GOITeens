import os
from typing import List, Optional
import asyncio
from uuid import uuid4

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from dotenv import load_dotenv


load_dotenv()
SQLALCHEMY_URI = os.getenv("SQLALCHEMY_URI")
engine = create_async_engine(SQLALCHEMY_URI, echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    address: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    phone_number: Mapped[str] = mapped_column(String(50))
    account_id: Mapped[Optional[str]] = mapped_column(Text(), nullable=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid4().hex


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(50))
    token: Mapped[Optional[str]] = mapped_column(String(100), nullable=True, default=None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid4().hex


# Base.metadata.create_all(bind=engine)


async def create_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def get_db():
    async with async_session() as session:
        yield session


if __name__ == "__main__":
    asyncio.run(create_db())
