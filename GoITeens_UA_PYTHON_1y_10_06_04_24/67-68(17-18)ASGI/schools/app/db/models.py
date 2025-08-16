from typing import List, Optional
import enum
import asyncio
from datetime import datetime, timedelta, timezone

from sqlalchemy import String, Integer, ForeignKey, Column, Enum
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import bcrypt
import jwt

from app.config import settings


engine = create_async_engine(settings.sqlalchemy_uri, echo=True)
Session = async_sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()


class Role(enum.Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"
    editor = "editor"


class UserThemAssoc(Base):
    __tablename__ = "user_them_assoc"

    user_id = Column(ForeignKey("users.id", ondelete="cascade", onupdate="cascade"), primary_key=True)
    subject_id = Column(ForeignKey("subjects.id", ondelete="cascade", onupdate="cascade"), primary_key=True)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    password_: Mapped[str] = mapped_column(String(100))
    role: Mapped[Role] = mapped_column(default=Role.student)
    cabinet_id: Mapped[int] = mapped_column(ForeignKey("cabinets.id", ondelete="cascade", onupdate="cascade"), nullable=True, default=None)
    cabinet: Mapped["Cabinet"] = relationship(lazy="selectin", back_populates="users")
    subjects: Mapped[List["Subject"]] = relationship(secondary=UserThemAssoc.__tablename__, back_populates="users", lazy="selectin")

    @property
    def password(self):
        return self.password_

    @password.setter
    def password(self, pwd: str):
        self.password_ = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())

    def is_verify_password(self, pwd: str):
        return bcrypt.checkpw(pwd.encode(), self.password_.encode())

    def get_token(self, pwd: str, exp_time_minutes: int = settings.exp_time_minutes):
        if self.is_verify_password(pwd):
            payload = dict(
                sub=str(self.id),
                exp=datetime.now(timezone.utc) + timedelta(minutes=exp_time_minutes)
            )
            return jwt.encode(payload=payload, key=settings.secret_key, algorithm=settings.algorithm)


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    users: Mapped[List["User"]] = relationship(secondary=UserThemAssoc.__tablename__, back_populates="subjects", lazy="selectin")


class Cabinet(Base):
    __tablename__ = "cabinets"

    id:  Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(10), unique=True)
    users: Mapped[List["User"]] = relationship(lazy="selectin", back_populates="cabinet")


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    async with Session() as session:
        yield session
