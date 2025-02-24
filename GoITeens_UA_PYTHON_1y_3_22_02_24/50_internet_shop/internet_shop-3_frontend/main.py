import os
import binascii

from flask import Flask, request, url_for, redirect, render_template, session, flash

from src.data import data_actions
from src.data.forms import SignUpForm, LoginForm


app = Flask(__name__, template_folder="src/templates")
app.secret_key = binascii.hexlify(os.urandom(24))


@app.get("/")
def index():
    products = data_actions.get_products()
    return render_template("index.html", products=products)


@app.get("/product/<product_id>/")
def get_product(product_id):
    product = data_actions.get_product(product_id)
    return render_template("product.html", product=product)


@app.get("/buy_product/<product_id>/")
def buy_product(product_id):
    product = data_actions.get_product(product_id)
    return f"Ви успішно придбали '{product['name']}'"


@app.route("/signup/", methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        data_actions.signup(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=form.password.data
        )
        return redirect(url_for("login"))

    return render_template("signup.html", form=form)


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        msg = data_actions.login(
            email=form.email.data,
            password=form.password.data
        )
        if msg:
            flash(msg)
            return redirect(url_for("cabinet"))
        else:
            flash("Логін або пароль невірний")
            return redirect(url_for("login"))

    return render_template("login.html", form=form)


@app.get("/cabinet/")
def cabinet():
    user = data_actions.get_user()
    if user:
        return render_template("cabinet.html", user=user)
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
