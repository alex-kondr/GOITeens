from uuid import uuid4
from datetime import timedelta, datetime, timezone
# import asyncio


from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from passlib.context import CryptContext
import jwt
# import bcrypt

from app.config import settings


engine = create_async_engine(settings.sqlalchemy_uri, echo=True)
Session = async_sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# bcrypt.__about__ = bcrypt


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    password_: Mapped[str] = mapped_column(String(100))
    disabled: Mapped[bool] = mapped_column(Boolean(), default=False)
    # token: Mapped[Optional[str]] = mapped_column(String(100), nullable=True, default=None)

    def __init__(self, **kwargs):
        self.id = uuid4().hex
        super().__init__(**kwargs)

    @property
    def password(self):
        return self.password_

    @password.setter
    def password(self, pwd):
        self.password_ = pwd_context.hash(pwd)

    def verify_password(self, pwd):
        return pwd_context.verify(pwd, self.password_)

    def create_access_token(self, expires_delta: timedelta = settings.access_token_expire_min):
        payload = dict(sub=self.username, exp=datetime.now(tz=timezone.utc) + expires_delta)
        return jwt.encode(payload=payload, key=settings.secret_key, algorithm=settings.algorithm)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    async with Session() as session:
        yield session

