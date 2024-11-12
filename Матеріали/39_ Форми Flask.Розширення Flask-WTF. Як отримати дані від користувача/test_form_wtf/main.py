from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField, RadioField


class SubscriptionForm(FlaskForm):
    name = StringField("Ім'я")
    email = StringField("Пошта")
    submit = SubmitField("Відправити")


class IcecreamForm(FlaskForm):
    tastes = SelectField("Смак")
    topping = SelectMultipleField("Топінг")
    cup_size = RadioField("Стаканчик")
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
    form.tastes.choices = []


if __name__ == "__main__":
    app.run(debug=True)