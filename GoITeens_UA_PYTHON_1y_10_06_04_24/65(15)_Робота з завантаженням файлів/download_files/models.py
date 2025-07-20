import asyncio

from sqlalchemy import String
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import Mapped, mapped_column, declarative_base


engine = create_async_engine("sqlite+aiosqlite:///files.db", echo=True)
Session = async_sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()


class DownloadFile(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    original_name: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    async with Session() as session:
        yield session


if __name__ == "__main__":
    asyncio.run(create_db())
