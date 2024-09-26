from flask import render_template, Blueprint, request, redirect

from models.base import Session
from models.pizza import Pizza
from models.ingredient import Ingredient
from data import wheather


root_router = Blueprint("root", __name__)


@root_router.get("/")
def index():
    wheather_info = wheather.get_wheater()
    return render_template("index.html", wheather_info=wheather_info, title="Моя супер піцерія")


@root_router.get("/menu/")
def menu():
    wheather_info = wheather.get_wheater("Kyiv")

    with Session() as session:
        pizzas = session.query(Pizza).all()
        ingredients = session.query(Ingredient).all()

        context = {
            "pizzas": pizzas,
            "ingredients": ingredients,
            "title": "Мега меню",
            "wheather_info": wheather_info
        }

        return render_template("menu.html", **context)


@root_router.post("/add_pizza/")
def add_pizza():
    with Session() as session:
        name = request.form.get("name")
        price = request.form.get("price")

        ingredients = request.form.getlist("ingredients")
        print(f"{ingredients = }")
        ingredients = session.query(Ingredient).where(Ingredient.id.in_(ingredients)).all()
        print(f"{ingredients = }")

        pizza = Pizza(name=name, price=price, ingredients=ingredients)
        print(f"{pizza = }")
        session.add(pizza)
        session.commit()
        return redirect("/menu/")
