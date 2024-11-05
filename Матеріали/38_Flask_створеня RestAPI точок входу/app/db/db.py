from app.db.base import Session
from app.db.models import Quote


def get_quotes():
    with Session() as session:
        return session.query(Quote).all()


def get_quote(quote_id):
    with Session() as session:
        return session.query(Quote).filter_by(id=quote_id).first()


def limit():
    with Session() as session:
        limit_number = session.query(Quote).count()
        return limit_number


def add_quote(author, quote):
    with Session() as session:
        quote_db = Quote(author=author, quote=quote)
        session.add(quote_db)
        session.commit()
        session.refresh(quote_db)
        return quote_db.id


def update_quote(id, author, quote):
    with Session() as session:
        quote_db = session.query(Quote).filter_by(id=id).first()
        quote_db.author = author
        quote_db.quote = quote
        session.commit()
        return 202


def delete_quote(id):
    with Session() as session:
        quote = session.query(Quote).filter_by(id=id).first()
        session.delete(quote)
        session.commit()
        return 200
