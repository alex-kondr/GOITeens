from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import TIMESTAMP
from sqlalchemy import String, ForeignKey

from app.db import Base, Position


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    temp_pass: Mapped[str] = mapped_column(String(50), nullable=True)
    time_expected: Mapped[datetime] = mapped_column(TIMESTAMP(), nullable=True)
    position_id: Mapped[Position] = mapped_column(ForeignKey(Position.id))
