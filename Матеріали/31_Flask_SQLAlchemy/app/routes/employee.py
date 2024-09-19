from flask import render_template, Blueprint, request
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.base import Session
from app.models.employee import Employee
from app.models.position import Position


employees_blueprint = Blueprint("employees", __name__, url_prefix="/employees/")


@employees_blueprint.get("/")
@employees_blueprint.post("/")
def add_employee():
    with Session() as session:

        if request.method == "POST":
            positions = session.query(Position).where(Position.id.in_(request.form.getlist("positions"))).all()
            employee_data = {key: value for key, value in request.form.items() if key != "positions"}

            employee = Employee(**employee_data, positions=positions)

            session.add(employee)
            session.commit()

        employees = session.query(Employee).all()
        positions = session.query(Position).all()

        return render_template("employee/management.html", employees=employees, positions=positions)


@employees_blueprint.get("/<int:id>/")
def get_employee(id):
    with Session() as session:
        employee = session.scalars(select(Employee).where(Employee.id == id)).first()

        cabinets = set()
        for position in employee.positions:
            cabinets |= {cab.name for cab in position.cabinets}

        return render_template("employee/info.html", employee=employee, cabinets=cabinets, title="Інформація про працівника")
