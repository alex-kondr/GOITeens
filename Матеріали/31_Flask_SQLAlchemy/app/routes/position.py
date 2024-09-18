from flask import render_template, request, Blueprint
from sqlalchemy import select

from app.models.base import Session
from app.models.position import Position


positions_blueprint = Blueprint("positions", __name__)


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
def get_positions(id):
    with Session() as session:
        content = session.scalars(select(Position).where(Position.id == id)).first()
        return render_template("index.html", content=content, title="Інформація про посаду")
