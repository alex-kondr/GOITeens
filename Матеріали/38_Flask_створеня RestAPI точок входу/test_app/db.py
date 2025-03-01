from sqlalchemy import String, create_engine
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, DeclarativeBase


engine = create_engine("posts.db", echo=True)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str] = mapped_column(String(100))
    text: Mapped[str] = mapped_column(String())


def create_db():
    Base.metadata.create_all(bind=engine)
