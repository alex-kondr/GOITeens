from flask import Flask

from app.routes import blog_route, position_route
from app.db import Post, create_db


app = Flask(__name__)
app.register_blueprint(blog_route)
app.register_blueprint(position_route)


def main():
    create_db()
    app.run(debug=True)
