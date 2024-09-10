from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", title="Моя супер піцерія")


@app.get("/menu-ababagalamaga/")
def menu():
    pizzas = [
        {"name": "Пепероні", "price": 22, "ingredients": "ковбаса 'Пепероні', сир, соус"},
        {"name": "Пепероні", "price": 29, "ingredients": "ковбаса 'Пепероні', сир, соус"},
        {"name": "Моцарела", "price": 20, "ingredients": "сир 'Моцарела', соус, петрушка"},
        {"name": "Чотири сира", "price": 30, "ingredients": "сир 'Моцарела', сир 'Чедер', сир 'Сологуні', сир 'Брі'"}
    ]
    context = {
        "pizzas": pizzas,
        "title": "Мега меню"
    }
    return render_template("menu.html", **context)


if __name__ == "__main__":
    app.run(debug=True)