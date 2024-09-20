from flask import render_template, Blueprint
# from sqlalchemy import 

from app.models.base import Session
from app.models.position import Position


position_blueprint = Blueprint("positions", __name__, url_prefix="/position/")


@position_blueprint.get("/<int:id>")
def get_position(id):
    with Session() as session:
        position = session.query(Position).where(Position.id == id).first()
        return render_template("..html", position=position)
