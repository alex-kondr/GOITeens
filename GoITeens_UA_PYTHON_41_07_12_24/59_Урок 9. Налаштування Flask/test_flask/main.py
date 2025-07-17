from flask import Flask


app = Flask(__name__)


@app.route("/")
def index_1():
    return "<h1>Всім привіт!</h1>"


@app.route("/info/", methods=["GET", "POST"])
def info_1():
    return "<p>Інформаційна сторінка</p>"


@app.post("/about/")
@app.get("/about/")
def about():
    return "Сторінка про нашу компанію"


@app.post("/about-2/")
def about_2():
    return "Сторінка про нашу компанію 2"


@app.get("/concat-1/<a>/<b>/")
@app.get("/concat-2/<a>/<b>/")
def concat(a: str, b: str):
    return f"Конкатенація {a} та  {b} = {a + b}"


def sum(a: int, b: int):
    return str(a + b)


app.add_url_rule("/sum/<int:a>/<int:b>/", view_func=sum)


if __name__ == "__main__":
    app.run(debug=True)
