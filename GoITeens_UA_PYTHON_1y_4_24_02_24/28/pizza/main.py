import random

from flask import Flask, render_template, redirect


app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True, port=1234)