from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, declarative_base, relationship


engine = create_engine("sqlite:///reviews.db", echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(primary_key=True)
    grade: Mapped[str] = mapped_column(String())


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str] = mapped_column(String(100))
    text: Mapped[str] = mapped_column(String())
    grade_id: Mapped[int] = mapped_column(ForeignKey(Grade.id))
    grade: Mapped[Grade] = relationship()


def create_db():
    Base.metadata.create_all(bind=engine)