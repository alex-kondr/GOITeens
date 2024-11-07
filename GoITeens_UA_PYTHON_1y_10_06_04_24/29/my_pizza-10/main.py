from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
    pizzas = [
        {"name": "Пепероні", "ingredients": "Ковбаса пепероні, сир моцарела, соус", "price": 150},
        {"name": "Класична", "ingredients": "Помідори, сир сулугі, соус", "price": 120},
        {"name": "4 сира", "ingredients": "Сир моцарела, сир солугуні, сир брі, сир фета, соус", "price": 200}
    ]
    return render_template("menu.html", pizzas=pizzas)


if __name__ == "__main__":
    app.run(debug=True, port=80)