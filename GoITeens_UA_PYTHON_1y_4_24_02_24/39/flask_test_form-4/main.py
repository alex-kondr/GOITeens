from flask import Flask, request, render_template
from flask_wtf import FlaskForm
import wtforms


app = Flask(__name__)
app.secret_key = "123"


class FormWTFTest(FlaskForm):
    name = wtforms.StringField("Введіть назву у поле")
    text = wtforms.TextAreaField("Введіть свій текст")
    price = wtforms.FloatField("Введіть ціну у полу")
    choice = wtforms.RadioField("Виберіть місто")
    submit = wtforms.SubmitField("Відправити форму")


@app.route("/form-wtf-1/", methods=["GET", "POST"])
def form_wtf_1():
    form_twf = FormWTFTest()
    form_twf.choice.choices = [("Київ", "Київ"), ("Одеса", "Одеса"), ("Харків", "Харків")]
    if request.method == "POST":
        name = form_twf.name.data
        text = form_twf.text.data
        price = form_twf.price.data
        choice = form_twf.choice.data

        msg = f"Test_WTF: {name = }; {price = }; { text = }; {choice = }"
        print(msg)
        return msg
    return render_template("form_wtf.html", form=form_twf)


@app.route("/form/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")

        msg = f"{name = }; {price = }"
        print(msg)
        return msg
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)