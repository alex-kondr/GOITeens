from sqlalchemy import Table, Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from databases import Database


DATABASE_URI = "sqlite:///products.db"
engine = create_engine(DATABASE_URI, echo=True)
database = Database(DATABASE_URI)
Base = declarative_base()


products_db = Table(
    "products",
    Base.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("name", String)
)


def create_db():
    Base.metadata.create_all(engine)
