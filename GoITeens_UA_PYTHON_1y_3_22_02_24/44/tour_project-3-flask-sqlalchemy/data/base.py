from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, declarative_base
from flask_sqlalchemy import SQLAlchemy


# engine = create_engine("sqlite:///tours.db", echo=True)
# engine = create_engine("postgresql+psycopg2://postgres:2@localhost:5432/tours-3", echo=True)
# Session = sessionmaker(bind=engine)


# class Base(DeclarativeBase):
#     pass

Base = declarative_base()
db = SQLAlchemy(model_class=Base, engine_options=dict(echo=True))


# def create_db():
#     Base.metadata.create_all(bind=engine)
