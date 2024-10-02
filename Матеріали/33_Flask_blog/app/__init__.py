from flask import Flask

from app.routes.blog import blog_route
from app.db.models.post import Post
from app.db.base import create_db


app = Flask(__name__)
app.register_blueprint(blog_route)


def main():
    create_db()
    app.run(debug=True)
