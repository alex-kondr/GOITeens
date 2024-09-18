from flask import render_template, Blueprint, request

from app import Session
from app.models import Employee


employees_blueprint = Blueprint("employees", __name__)


@employees_blueprint.get("/")
@employees_blueprint.post("/")
def add_employee():
    with Session() as session:
        if request.method == "POST":
            employee = Employee(**request.form)
            session.add(employee)
            session.commit()

        employees = session.query(Employee).all()

    return render_template("employee/management.html", employees=employees)


@employees_blueprint.get("/<int:id>/")
def get_employee(id):
    with Session() as session:
        pass
