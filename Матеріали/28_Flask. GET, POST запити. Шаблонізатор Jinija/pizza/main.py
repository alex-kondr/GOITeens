import random

from flask import Flask, render_template, request, url_for, abort


app = Flask(__name__, template_folder="templates", static_folder="static")

count = 0

max_score = 100
test_name = "Python Challenge"
students = [
  {"name": "Vlad", "score": 100},
  {"name": "Sviatoslav", "score": 99},
  {"name": "Юстин", "score": 100},
  {"name": "Viktor", "score": 79},
  {"name": "Ярослав", "score": 93},
]

@app.get('/results/')
def results():
    context = {
        "title": "Results",
        "students": students,
        "test_name": test_name,
        "max_score": max_score,
    }
    return render_template("results_2.html", **context)


@app.get("/")
def index():
    return render_template("index.html", count=count)


@app.get("/menu/")
def menu():
    context = {
        "name_pizza": "Чотири сира",
        "pizza_ingredients": "Сир чедер, сир сологуні"
    }
    return render_template("menu.html", **context)
    # global count
    # count += 1
    # return redirect("/")


@app.get("/contacts/")
def contacts():
    context = {
        "numb_3": random.randint(100, 999),
        "numb_4": random.randint(1000, 9999)
    }
    return render_template("contacts.html", **context)


@app.get("/test/")
def testr():
    return render_template("test.html", title="Hello")


@app.get("/api/results/")
def api_results():
    context = {
        "title": "Results",
        "students": students,
        "test_name": test_name,
        "max_score": max_score,
    }
    return context


@app.get("/login/")
@app.post("/login/")
def login():
    name = request.form.get("name")
    print(request.form)
    return render_template("login.html", name=name)


@app.get("/url_test/")
def url_test():
    return url_for("login")


@app.get("/url/")
def test_url():
    abort(401)
    return "Доступ заборонено"


@app.errorhandler(404)
def page_not_found(error):
    print(f"{error = }")
    print(request.base_url)
    return "error", 404


@app.get("/test_index/")
def test_index():
    return render_template("test_index.html")


if __name__ == "__main__":
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('contacts'))
        print(url_for('menu'))
        print(url_for('login'))
        print(url_for('results'))

    app.run(debug=True, port=1234)
