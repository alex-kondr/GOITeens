from flask import Flask, render_template


app = Flask(__name__)


CONTACT = "099-456-78-98"


@app.get("/")
def index():
    context = {
        "title": "Початок тестування теми № 2",
        "contact": CONTACT
    }
    return render_template("index.html", **context)


@app.get('/results_ababagalamaga/')
def results():
    context = {
        "max_score": 100,
        "test_name": "Python Challenge",
        "students": [
        {"name": "Vlad", "score": 100},
        {"name": "Sviatoslav", "score": 99},
        {"name": "Юстин", "score": 100},
        {"name": "Viktor", "score": 79},
        {"name": "Ярослав", "score": 93},
        ],
        "title": "Результати тестування",
        "contact": CONTACT
    }

    return render_template("results.html", **context)


if __name__ == "__main__":
    app.run(debug=True)