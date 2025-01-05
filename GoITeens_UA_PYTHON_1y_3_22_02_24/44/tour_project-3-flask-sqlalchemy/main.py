import os
import binascii

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from flask_migrate import Migrate

from data import data
from data.tours_to_db import data_to_db
from data.base import db# Session, create_db
from data.models_old import Tour, User
from data.forms import SignUpForm, LoginForm


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:2@localhost:5432/tours_flask_sqlalchemy"
app.config['MAIL_SERVER'] = 'smtp.ukr.net'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "sounddummies@ukr.net"
app.config['MAIL_PASSWORD'] = "1dwqREdpvxlS7tWW"
app.config['MAIL_DEFAULT_SENDER'] = "sounddummies@ukr.net"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.secret_key = binascii.hexlify(os.urandom(24))
db.init_app(app)
mail = Mail(app)
app.app_context().push()
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_message = "Щоб забронювати тур увійдіть до системи"
login_manager.login_view = "login"
login_manager.init_app(app)


# with app.app_context():
#     db.create_all()
#     data_to_db()


@app.context_processor
def global_data():
    if current_user.is_authenticated:
        # user = db.session.query(User).where(User.id == current_user.id).first()
        user_tours = current_user.tours
        # user_tours = user.tours
    else:
        user_tours = []

    return dict(departures=data.departures, user_tours=user_tours)


@login_manager.user_loader
def user_loader(user_id):
    return db.session.query(User).where(User.id == user_id).first()


@app.route('/')
def index():
    tours = db.session.query(Tour).all()
    return render_template("index.html", tours=tours)


@app.route('/tour/<int:index>/')
def tour(index):
    tour = db.session.query(Tour).where(Tour.id == index).first()
    return render_template("tour.html", tour=tour)


@app.route('/departure/<dep>/')
def departure(dep):
    tours = db.session.query(Tour).where(Tour.departure == dep).all()
    return render_template("departure.html", tours=tours, dep=dep)


@app.route("/signup/", methods=["GET", "POST"])
def signup():
    signup_form = SignUpForm()
    print(f"{ request.root_path = }")
    print(f"{ request.root_url = }")

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        email = signup_form.email.data

        user = db.session.query(User).where(User.username == username).first()
        if user:
            flash("Користувач з таким логіном вже існує")
            return redirect(url_for("login"))

        password = generate_password_hash(signup_form.password.data)
        pass_validator = binascii.hexlify(os.urandom(15))
        user = User(username=username, email=email, password=password, email_pass_validator=pass_validator)
        db.session.add(user)
        db.session.commit()

        msg = Message(
            subject="Flask Tour project",
            body=f"Validate your email\n {request.root_url}/validate/{username}/{pass_validator}/"
        )
        mail.send(msg)
        flash("Вітаю, Ви успішно зареєструвались")
        return redirect(url_for("login"))

    return render_template("signup.html", form=signup_form)


@app.route("/login/", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        username = login_form.username.data

        user = db.session.query(User).where(or_(User.username == username, User.email == username)).first()

        if not user or not check_password_hash(user.password, login_form.password.data):
            flash("Логін або пароль невірний")
            return redirect(url_for("login"))

        login_user(user)
        return redirect(url_for("cabinet"))

    return render_template("login.html", form=login_form)


@app.get("/logout/")
@login_required
def logout():
    flash("До побачення.")
    logout_user()
    return redirect(url_for("index"))


@app.get("/reserve/<int:tour_id>/")
@login_required
def reserve(tour_id: int):
    tour = db.session.query(Tour).where(Tour.id == tour_id).first()
    user = db.session.query(User).where(User.id == current_user.id).first()
    user.tours.append(tour)
    db.session.commit()
    flash("Тур успішно заброньовано")
    return redirect(url_for("cabinet"))


@app.get("/cabinet/")
@login_required
def cabinet():
    return render_template("cabinet.html")



@app.get("/validate/<username>/<pass_validator>/")
def email_validator(username: str, pass_validator: str):
    print(f"{username = }")
    print(f"{pass_validator = }")
    flash("Успішно")
    return redirect(url_for("signup"))


if __name__ == "__main__":
    # create_db()
    # data_to_db()
    # msg = Message(
    #     subject="Hello",
    #     recipients=["alex_kondr@outlook.com"]
    # )
    # mail.send(msg)
    # migrate.init_app(command="")
    app.run(debug=True, host='0.0.0.0')