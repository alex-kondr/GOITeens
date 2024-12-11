from flask import Flask, render_template, request, redirect, url_for

from data import data
from data.base import create_db
from data.data_to_db import write_data_to_db
from data.base import Session
from data.models import Reserve


app = Flask(__name__)
NAVIGATION = data.departures


@app.get("/")
def index():
    return render_template("index.html", departures=NAVIGATION, tours=data.tours)


@app.get("/tour/<int:id>/")
def get_tour(id):
    tour = data.tours.get(id)
    return render_template("tour.html", departures=NAVIGATION, tour=tour, id=id)


@app.get("/departure/<dep_eng>/")
def departure(dep_eng):
    tours = {}
    for id, tour in data.tours.items():
        if tour["departure"] == dep_eng:
            tours[id] = tour

    return render_template("departure.html", departures=NAVIGATION, tours=tours)


@app.post("/tour/reserve/<int:id>/")
def reserve(id):
    with Session() as session:
        name = request.form.get("name")
        reserve_tour = Reserve(name=name, tour_id=id)
        session.add(reserve_tour)
        session.commit()
        return redirect(url_for("index"))


if __name__ == "__main__":
    create_db()
    write_data_to_db()
    # app.run(debug=True)
