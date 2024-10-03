from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey

from app.db import Base, Position


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    position: Mapped[Position] = mapped_column(ForeignKey(Position.id))