from datetime import datetime

from flask import Blueprint, render_template, request, redirect

from app.data.password import get_user
from app.db import Session, Position, User


position_route = Blueprint("positions", __name__, url_prefix="/positions/")


@position_route.get("/")
@position_route.post("/")
def add_position():
    temp_pass = ""
    with Session() as session:
        if request.method == "POST":
            name = request.form.get("name")
            user_name = request.form.get("user_name")
            password = request.form.get("password")
            temp_pass = request.form.get("temp_pass")

            user = get_user(user_name, password, temp_pass)

            if user:
                position = Position(name=name)
                session.add(position)
                session.commit()
                temp_pass = user.temp_pass
            else:
                return redirect("https://http.cat/401")

    return render_template("add_position.html", temp_pass=temp_pass)


@position_route.post("/validate_temp_pass/")
def is_validate_temp_pass():
    temp_pass = request.json.get("temp_pass")
    print("temp_pass=", temp_pass)
    with Session() as session:
        if temp_pass:
            user = session.query(User).where(User.temp_pass == temp_pass).first()
            if user and user.time_expected > datetime.now():
                return {"is_valid": True}

    return {"is_valid": False}
