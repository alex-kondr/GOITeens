import os

from flask import Flask
from dotenv import load_dotenv

from app.routes.blog import blog_route
from app.db import Post, create_db


load_dotenv()
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

app = Flask(__name__)
app.register_blueprint(blog_route)


def main():
    create_db()
    app.run(debug=True)
