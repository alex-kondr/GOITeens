from flask import render_template, Blueprint


root_blueprint = Blueprint("root", __name__)


@root_blueprint.get("/")
def index():
    return render_template("index.html", title="Головна сторінка")