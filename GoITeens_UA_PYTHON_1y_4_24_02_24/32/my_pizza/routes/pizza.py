from flask import Blueprint, render_template, request, redirect

from models.base import Session
from models.pizza import Pizza
from models.ingredient import Ingredint
from data.wheater import get_wheater


pizza_route = Blueprint("pizzas", __name__)


@pizza_route.get("/")
@pizza_route.post("/")
def index():
    city = "Odesa"
    if request.method == "POST":
        city = request.form.get("city")

    wheather = get_wheater(city)
    if wheather.get("text") == "Sunny":
        pizza = "Гавайська"
    elif wheather.get("text") == "Partly cloudy":
        pizza = "4 Сира"
    elif wheather.get("text") == "Light drizzle":
        pizza = "Преміум"

    return render_template("index.html", title="Моя супер піцерія", wheather=wheather, pizza=pizza)


@pizza_route.get("/menu/")
def menu():
    wheather = get_wheater()
    with Session() as session:
        pizzas = session.query(Pizza).all()
        ingredients = session.query(Ingredint).all()

        context = {
            "pizzas": pizzas,
            "ingredients": ingredients,
            "title": "Мега меню",
            "wheather": wheather
        }
        return render_template("menu.html", **context)


@pizza_route.post("/add_pizza/")
def add_pizza():
    with Session() as session:
        name = request.form.get("name")
        price = float(request.form.get("price"))

        ingredients = request.form.getlist("ingredients")
        ingredients = session.query(Ingredint).where(Ingredint.id.in_(ingredients)).all()

        pizza = Pizza(name=name, price=price, ingredients=ingredients)
        session.add(pizza)
        session.commit()
        return redirect("/menu/")
