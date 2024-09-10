import random

from flask import Flask, render_template


app = Flask(__name__)


CONTACT = "+380731570901"


@app.get("/")
def index():
    numbers = [random.randint(0, 100) for _ in range(10)]
    return render_template("index.html", contact=CONTACT, numbers=numbers)


@app.get('/results-ababagalamaga/')
def results():
    context = {
        "max_score": 100,
        "test_name": "Python Challenge",
        "students": [
        {"name": "Vlad", "score": 100},
        {"name": "Vlad", "score": 42},
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