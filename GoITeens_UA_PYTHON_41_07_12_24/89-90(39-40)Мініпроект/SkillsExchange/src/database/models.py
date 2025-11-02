from typing import Optional, List
import enum
from datetime import datetime

from sqlalchemy import String, Text, ForeignKey, func, DateTime, Boolean, Enum, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.db import Base


class SkillLevel(enum.StrEnum):
    begin = "begin"
    medium = "medium"
    intermediate = "intermediate"
    high = "high"


class ReviewLevel(enum.IntEnum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5


class ExchangeStatus(enum.StrEnum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    completed = "completed"


class UserSkillAssoc(Base):
    __tablename__ = "user_skill_assoc"

    user_id = Column("user_id", ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    skill_id = Column("skill_id", ForeignKey("skills.id", ondelete="CASCADE"), primary_key=True)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50))
    full_name: Mapped[str] = mapped_column(String(50))
    bio: Mapped[Optional[str]] = mapped_column(Text(), nullable=True, default=None)
    skills: Mapped[List["Skill"]] = relationship(secondary=UserSkillAssoc.__tablename__, back_populates="users", lazy="selectin")
    send_reviews: Mapped[List["Review"]] = relationship(foreign_keys="Review.sender_id", back_populates="sender", lazy="selectin")
    received_reviews: Mapped[List["Review"]] = relationship(foreign_keys="Review.received_id", back_populates="received", lazy="selectin")
    send_exchanges: Mapped[List["Exchange"]] = relationship(foreign_keys="Exchange.sender_id", back_populates="sender", lazy="selectin")
    received_exchanges: Mapped[List["Exchange"]] = relationship(foreign_keys="Exchange.received_id", back_populates="received", lazy="selectin")
    create_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now())
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)


class Skill(Base):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), index=True)
    description: Mapped[Optional[str]] = mapped_column(Text(), default=None, nullable=True)
    level: Mapped[SkillLevel] = mapped_column(Enum(SkillLevel))
    exchanges: Mapped[List["Exchange"]] = relationship(back_populates="skill", lazy="selectin")
    creat_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(DateTime(), onupdate=func.now())
    users: Mapped[List[User]] = relationship(secondary=UserSkillAssoc.__tablename__, back_populates="skills", lazy="selectin")
    can_teach: Mapped[bool] = mapped_column(Boolean(), default=False)
    want_learn: Mapped[bool] = mapped_column(Boolean(), default=False)


class Exchange(Base):
    __tablename__ = "exchanges"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    received_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    skill_id: Mapped[int] = mapped_column(ForeignKey("skills.id", ondelete="CASCADE"))
    date_at_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    message: Mapped[str] = mapped_column(Text(1000))
    status: Mapped[ExchangeStatus] = mapped_column(Enum(ExchangeStatus), default=ExchangeStatus.pending)
    create_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now())
    skill: Mapped[Skill] = relationship(foreign_keys=[skill_id], back_populates="exchanges", lazy="selectin")
    sender: Mapped[User] = relationship(foreign_keys=[sender_id], back_populates="send_exchanges", lazy="selectin")
    received: Mapped[User] = relationship(foreign_keys=[received_id], back_populates="received_exchanges", lazy="selectin")
    reviews: Mapped["Exchange"] = relationship(back_populates="exchange", lazy="selectin")


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    received_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    rating: Mapped[ReviewLevel] = mapped_column(Enum(ReviewLevel), default=ReviewLevel.five)
    create_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now())
    comment: Mapped[Optional[str]] = mapped_column(String(250), default=None, nullable=True)
    sender: Mapped[User] = relationship(foreign_keys=[sender_id], back_populates="send_reviews", lazy="selectin")
    received: Mapped[User] = relationship(foreign_keys=[received_id], back_populates="received_reviews", lazy="selectin")
    exchange_id: Mapped[int] = mapped_column(ForeignKey("exchanges.id", ondelete="CASCADE"))
    exchange: Mapped[Exchange] = relationship(back_populates="reviews", lazy="selectin")