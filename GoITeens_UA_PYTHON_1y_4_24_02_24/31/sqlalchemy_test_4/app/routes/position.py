from flask import render_template, Blueprint


positions_route = Blueprint("positions", __name__, url_prefix="/positions/")


@positions_route.get("/")
def add_position():
    pass
