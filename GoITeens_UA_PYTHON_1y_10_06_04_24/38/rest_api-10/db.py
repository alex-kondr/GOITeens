from sqlalchemy import String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column


engine = create_engine("sqlite:///quotes.db", echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Quote(Base):
    __tablename__ = "quotes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    author: Mapped[str] = mapped_column(String(100))
    text: Mapped[str] = mapped_column(String(500))


def create_db():
    Base.metadata.create_all(bind=engine)
