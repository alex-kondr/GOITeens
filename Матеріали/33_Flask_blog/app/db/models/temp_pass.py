from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String
from sqlalchemy.types import TIMESTAMP

from app.db import Base, User


class TempPass(Base):
    __tablename__ = "temp_pass"

    id: Mapped[int] = mapped_column(primary_key=True)
    password: Mapped[str] = mapped_column(String(10))
    time_expected: Mapped[datetime] = mapped_column(TIMESTAMP())
    user_id: Mapped[User] = mapped_column(ForeignKey(User.id))
