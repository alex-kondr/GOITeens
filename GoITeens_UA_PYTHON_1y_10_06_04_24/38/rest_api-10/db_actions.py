from db import Session, Quote


def get_quotes():
    with Session() as session:
        return session.query(Quote).all()


def get_quote(id):
    with Session() as session:
        return session.query(Quote).where(Quote.id == id).first()


def add_quote(author, text):
    with Session() as session:
        quote = Quote(author=author, text=text)
        session.add(quote)
        session.commit()
        session.refresh(quote)
        return quote.id


def update_quote(id, author, text):
    with Session() as session:
        quote = session.query(Quote).where(Quote.id == id).first()
        quote.author = author
        quote.text = text
        session.commit()
        return f"Цитата під номером {id} успішно оновлена"


def delete_quote(id):
    with Session() as session:
        quote = session.query(Quote).where(Quote.id == id).first()
        session.delete(quote)
        session.commit()
        return f"Цитата підномером {id} успішно видалена"