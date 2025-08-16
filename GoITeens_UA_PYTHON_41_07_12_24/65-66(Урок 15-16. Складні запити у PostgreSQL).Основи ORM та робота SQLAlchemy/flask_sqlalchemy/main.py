from typing import Optional, List

from flask import Flask, render_template, redirect, request, url_for

from models import Session, User, Cabinet, Subject, UserSubjAssoc


app = Flask(__name__)


@app.route("/add_cabinet/", methods=["GET", "POST"])
def add_cabinet():
    if request.method == "POST":
        name = request.form.get("name")
        cabinet = Cabinet(name=name)
        with Session() as session:
            session.add(cabinet)
            session.commit()

        return redirect(url_for("get_cabinets"))

    return render_template("add_cabinet.html")


@app.get("/cabinets/")
def get_cabinets():
    with Session() as session:
        cabinets = session.query(Cabinet).all()
        return render_template("cabinets.html", cabinets=cabinets)


@app.get("/")
def index():
    pass


@app.get("/del-cabinet/<int:id>/")
def remove_cabinet(id: int):
    with Session() as session:
        cabinet = session.query(Cabinet).filter_by(id=id).first()
        session.delete(cabinet)
        session.commit()
        return redirect(url_for("get_cabinets"))


if __name__ == "__main__":
    app.run(debug=True)
