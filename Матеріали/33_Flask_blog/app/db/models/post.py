from datetime import datetime

from sqlalchemy.types import Text, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from app.db import Base, User


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(TIMESTAMP(), server_default=func.now())
    title: Mapped[str] = mapped_column(Text(), nullable=False)
    content: Mapped[str] = mapped_column(Text(), nullable=False)
    user: Mapped[User] = mapped_column(ForeignKey(User.id))
