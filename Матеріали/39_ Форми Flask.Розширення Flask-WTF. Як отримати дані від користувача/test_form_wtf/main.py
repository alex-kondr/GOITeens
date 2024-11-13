from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField, RadioField, PasswordField, BooleanField, IntegerField, validators


def is_luggage_weight_valid(form, field):
    if field.data > 30:
        raise validators.ValidationError('Вага багажа надто велика')


class SubscriptionForm(FlaskForm):
    name = StringField("Ім'я")
    email = StringField("Пошта")
    submit = SubmitField("Відправити")


class IcecreamForm(FlaskForm):
    tastes = SelectField("Смак")
    topping = SelectMultipleField("Топінг")
    cup_size = RadioField("Стаканчик")
    submit = SubmitField("Відправити")


class RegistrationForm(FlaskForm):
    email = StringField("Пошта")
    password = PasswordField("Пароль")
    submit = SubmitField("Відправити")
    remember = BooleanField("Запам'ятати мене")


class LuggageForm(FlaskForm):
    last_name = StringField("Прізвище", validators=[validators.InputRequired()])
    first_name = StringField("Ім'я", validators=[validators.InputRequired()])
    pass_id = IntegerField("Номер паспорта", validators=[validators.InputRequired()])
    weight = IntegerField("Вага багажа", validators=[validators.InputRequired(), is_luggage_weight_valid])
    submit = SubmitField("Відправити")


app = Flask(__name__)
app.secret_key = "123"

@app.route("/subscribe/", methods=["GET", "POST"])
def subscribe():
    form = SubscriptionForm()
    if request.method == "GET":
        return render_template("subscribe.html", form=form)

    return form.name.data


@app.route("/ice/", methods=["GET", "POST"])
def ice():
    form = IcecreamForm()
    form.tastes.choices = [('vanilla','vanilla'),('choko','choko'),('mango','mango')]
    form.topping.choices = [('coffee','coffee'), ('coffee','coffee'),('strawbery','strawbery')]
    form.cup_size.choices = [('little','little'), ('medium','medium'), ('big','big')]
    if request.method == "GET":
        return render_template("ice.html", form=form)
    return form.topping.data


@app.route("/register/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "GET":
        return render_template("registration.html", form=form)
    return form.email.data


@app.route("/luggage/", methods=["GET", "POST"])
def luggage():
    form = LuggageForm()
    print(form)
    if request.method == "GET":
        return render_template("luggage.html", form=form)

    if form.validate_on_submit():
        return "Ok"
    else:
        return form.errors


if __name__ == "__main__":
    app.run(debug=True)