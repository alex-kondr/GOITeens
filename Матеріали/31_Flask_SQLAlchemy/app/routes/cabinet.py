from flask import render_template, request, Blueprint
from sqlalchemy import select

from app.models.base import Session
from app.models.cabinet import Cabinet
from app.models.position import Position


cabinets_blueprint = Blueprint("cabinets", __name__, url_prefix="/cabinets/")


@cabinets_blueprint.get("/")
@cabinets_blueprint.post("/")
def add_cabinet():
    with Session() as session:
        if request.method == "POST":
            positions = request.form.getlist("positions")
            positions = session.query(Position).where(Position.id.in_(positions)).all()
            name = request.form.get("name")

            cabinet = Cabinet(name=name, positions=positions)
            session.add(cabinet)
            session.commit()

        cabinets = session.query(Cabinet).all()
        positions = session.query(Position).all()

        return render_template("cabinet/management.html", cabinets=cabinets, positions=positions)


@cabinets_blueprint.get("/<int:id>")
def get_cabinet(id):
    with Session() as session:
        cabinet = session.scalars(select(Cabinet).where(Cabinet.id == id)).first()
        return render_template("cabinet/info.html", cabinet=cabinet, title="Інформація про кабінет")
