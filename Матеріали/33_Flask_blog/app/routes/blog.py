from flask import render_template, Blueprint

from app.db.base import Session


blog_route = Blueprint("blog", __name__, url_prefix="/blog/")


@blog_route.get("/")
def index():
    
    return render_template("index.html")
