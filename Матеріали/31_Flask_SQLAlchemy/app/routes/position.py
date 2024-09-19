from flask import render_template, request, Blueprint
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.base import Session
from app.models.position import Position


positions_blueprint = Blueprint("positions", __name__, url_prefix="/positions/")


@positions_blueprint.get("/")
@positions_blueprint.post("/")
def add_position():
    with Session() as session:
        if request.method == "POST":
            session.add(Position(name=request.form.get("name")))
            session.commit()

        positions = session.query(Position).all()

    return render_template("position/management.html", positions=positions)


@positions_blueprint.get("/<int:id>/")
def get_position(id):
    with Session() as session:
        position = session.scalars(select(Position).where(Position.id == id)).first()
        return render_template("position/info.html", position=position, title="Інформація про посаду")
