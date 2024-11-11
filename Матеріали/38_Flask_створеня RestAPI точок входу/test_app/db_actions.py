from db import Session, Post


def get_posts():
    with Session() as session:
        return session.query(Post).all()


def get_post(id):
    with Session() as session:
        return session.query(Post).filter_by(id=id).first()


def add_post(author, text):
    with Session() as session:
        post = Post(author=author, text=text)
        session.add(post)
        session.commit()
        session.refresh(post)
        return post.id

