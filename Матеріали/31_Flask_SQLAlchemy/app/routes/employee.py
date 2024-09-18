from flask import render_template, Blueprint


employees_blueprint = Blueprint("employees", __name__)


@employees_blueprint.get("/")
def index():
    return render_template("index.html", title="Головна")
