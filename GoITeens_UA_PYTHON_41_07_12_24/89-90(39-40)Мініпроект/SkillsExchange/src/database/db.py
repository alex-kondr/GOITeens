from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from src.config import settings


Base = declarative_base()
engine = create_async_engine(settings.sqlalchemy_uri, echo=True)
Session = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


async def get_db():
    async with Session() as  session:
        yield session
