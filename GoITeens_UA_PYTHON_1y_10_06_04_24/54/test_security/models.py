from typing import Optional
import os
from uuid import uuid4

from sqlalchemy import String, create_engine
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, Session, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from databases import Database
from dotenv import load_dotenv


load_dotenv()
SQLALCHEMY_URI = os.getenv("SQLALCHEMY_URI")
# engine_sync = create_engine(SQLALCHEMY_URI, echo=True)
engine = create_async_engine(SQLALCHEMY_URI, echo=True)
# async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# database = Database(SQLALCHEMY_URI)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, default=None)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(50))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid4().hex


# Base.metadata.create_all(bind=engine_sync)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def get_db():
    with Session(bind=engine) as session:
        yield session


async def get_async_db():
    # async with async_session() as session:
    async with AsyncSession(bind=engine, expire_on_commit=False) as session:
        yield session


if __name__ == "__main__":
    import asyncio
    asyncio.run(init_db())

