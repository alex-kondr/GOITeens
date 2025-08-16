from typing import Optional, List

from sqlalchemy import String, ForeignKey, create_engine, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, DeclarativeBase, relationship

from config import settings


engine = create_engine(settings.db, echo=True)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    def create_tables(self):
        Base.metadata.create_all(bind=engine)

    def drop_tables(self):
        Base.metadata.drop_all(bind=engine)


class UserSubjAssoc(Base):
    __tablename__ = "user_subj_assoc"

    user_id = Column(Integer(), ForeignKey("users.id"), primary_key=True)
    subject_id = Column(Integer(), ForeignKey("subjects.id"), primary_key=True)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20))
    cabinet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("cabinets.id"), nullable=True, default=None)
    cabinet: Mapped[Optional["Cabinet"]] = relationship(back_populates="users")
    subjects: Mapped[List["Subject"]] = relationship(secondary=UserSubjAssoc.__tablename__, back_populates="users")


class Cabinet(Base):
    __tablename__ = "cabinets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), unique=True)
    users: Mapped[List["User"]] = relationship(back_populates="cabinet")


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), unique=True)
    users: Mapped[List["User"]] = relationship(secondary=UserSubjAssoc.__tablename__, back_populates="subjects")


# base = Base()
# base.drop_tables()
# base.create_tables()
