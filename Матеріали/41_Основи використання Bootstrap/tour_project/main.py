from flask import Flask, render_template

from data import data


app = Flask(__name__)
NAVIGATION = data.departures

@app.get("/")
def index():
    return render_template("index.html", navigation=NAVIGATION)



@app.get("/tour/<tour_name>")
def tour(tour_name):
    tour_info = {}

    tours = [dep for dep in data.tours.values() if dep["title"] == tour_name]
    if tours:
        tour_info = tours[0]

    return render_template("tour.html", navigation=NAVIGATION, tour=tour_info)


@app.get("/departure/<dep_eng>")
def departure(dep_eng):
    deps = [dep for dep in data.tours.values() if dep["departure"] == dep_eng ]
    return render_template("departure.html", navigation=NAVIGATION, deps=deps, dep_ukr=data.departures[dep_eng])


if __name__ == "__main__":
    app.run(debug=True)