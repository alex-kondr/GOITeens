from typing import Optional

from flask import Flask, flash, render_template, redirect, url_for
from flask_login import LoginManager, login_required, current_user, login_user, logout_user

from models import db, User, Menu, Order, Reservation
from forms import SignInForm, SignUpForm, OrderForm, ReservationForm
from config import settings


app = Flask(__name__)
app.secret_key = settings.secret_key
app.config["SQLALCHEMY_DATABASE_URI"] = settings.sqlalchemy_uri
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_message = "Спочатку увійдіть у застосунок"
login_manager.login_view = "sign_in"


# with app.app_context():
#     db.drop_all()
#     db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.route("/sign_up/", methods=["POST", "GET"])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash(message="Ви успішно зареєструвались!")
        return redirect(url_for("sign_in"))

    return render_template("sign_up.html", form=form)


@app.route("/sign_in/", methods=["GET", "POST"])
def sign_in():
    form = SignInForm()
    if form.validate_on_submit():
        user: User = User.query.filter_by(username=form.username.data).first()
        if not user or not user.is_verify_password(form.password.data):
            flash(message="Неправильно введено логін або пароль")
            return redirect(url_for("sign_in"))

        login_user(user)
        flash(message="Вхід успішний!")
        return redirect(url_for("get_menu"))

    return render_template("sign_in.html", form=form)


@app.get("/logout/")
@login_required
def logout():
    logout_user()
    flash(message="Ви успішно вийшли із системи!")
    return redirect(url_for("sign_in"))


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def get_menu():
    menu = Menu.query.all()
    form = OrderForm()
    form.name.choices = [item.name for item in menu]
    return render_template("menu.html", menu=menu, form=form)


if __name__ == "__main__":
    app.run(debug=True)
