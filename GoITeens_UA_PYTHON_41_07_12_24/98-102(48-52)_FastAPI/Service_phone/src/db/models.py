from typing import Optional, List
from datetime import datetime, timedelta, timezone

from sqlalchemy import String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.sql import func
import bcrypt
import jwt

from src.config import settings

engine = create_async_engine(settings.db, echo=True)
Session = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(20))
    last_name: Mapped[str] = mapped_column(String(20))
    password_: Mapped[str] = mapped_column(String(100))
    username: Mapped[str] = mapped_column(String(20))
    email: Mapped[Optional[str]] = mapped_column(String(100), nullable=True, default=None)
    create_at: Mapped[datetime] = mapped_column(DateTime(), server_default=func.now())

    problems_user: Mapped[List["Problem"]] = relationship(back_populates="user", lazy="selectin")
    problems_worker: Mapped[List["Problem"]] = relationship(back_populates="worker", lazy="selectin")

    messages: Mapped[List["Message"]] = relationship(back_populates="user", lazy="selectin")

    @property
    def password(self):
        return self.password_

    @password.setter
    def password(self, pwd: str):
        hash_password = bcrypt.hashpw(password=pwd.encode("utf-8"), salt=bcrypt.gensalt())
        self.password_ = hash_password.decode("utf-8")

    def is_verify_password(self, pwd: str):
        return bcrypt.checkpw(pwd.encode("utf-8"), self.password_.encode("utf-8"))

    def get_token(self, pwd: str):
        token = None
        if self.is_verify_password(pwd):
            exp = datetime.now(timezone.utc()) + timedelta(minutes=30)
            paylod = dict(sub=self.id, exp=exp)
            token = jwt.encode(payload=paylod, key=settings.secret_key, algorithm="HS256")

        return token


class Problem(Base):
    __tablename__ = "problems"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=True, default=None)
    description: Mapped[str] = mapped_column(Text())
    img: Mapped[str] = mapped_column(String(300))
    done: Mapped[bool] = mapped_column(Boolean(), default=False)
    warrantly: Mapped[Optional[datetime]] = mapped_column(DateTime(), nullable=True, default=None)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped[User] = relationship(foreign_keys=["user_id"], lazy="selectin", back_populates="problems_user")

    worker_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    worker: Mapped[User] = relationship(foreign_keys=["worker_id"], lazy="selectin", back_populates="problems_worker")

    response: Mapped["ResponseModel"] = relationship(back_populates="problem", lazy="selectin")


class ResponseModel(Base):
    __tablename__ = "responses"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)

    messages: Mapped[List["Message"]] = relationship(back_populates="response", lazy="selectin")

    problem_id: Mapped[int] = mapped_column(ForeignKey("problems.id", ondelete="CASCADE"))
    problem: Mapped["Problem"] = relationship(back_populates="response", lazy="selectin")


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[str] = mapped_column(Text())

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped[User] = relationship(back_populates="messages", lazy="selectin", foreign_keys=["user_id"])

    response_id: Mapped[ResponseModel] = mapped_column(ForeignKey("responses.id", ondelete="CASCADE"))
    response: Mapped[ResponseModel] = relationship(back_populates="messages", lazy="selectin", foreign_keys=["response_id"])


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    async with Session() as session:
        yield session
