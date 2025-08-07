import random

from flask import Flask, render_template, request, redirect, url_for
from faker import Faker


app = Flask(__name__)
fake = Faker("uk_UA")

data = {
    random.randint(1, 50):
        {
            "name": fake.first_name(),
            "last_name": fake.last_name(),
            "address": fake.address(),
            "phone_number": fake.phone_number()
        }
        for _ in range(15)
}


@app.get("/")
def index():
    context = dict(
        title="Підставлений title",
        title_h1="Тут підставляється заголовок сторінки",
        text="Текст сторінки"
    )
    return render_template("index.html", **context)


@app.get("/context/")
def text_context():
    numbers = [random.randint(1, 10) for _ in range(10)]
    return render_template("test_template.html", numbers=numbers)


@app.get("/contacts/")
def contacts():
    return render_template("contacts.html", contacts=data)


@app.route("/add_contact/", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        data.update(
            {
                request.form.get("id"):
                    {
                        "name": request.form.get("name"),
                        "last_name": request.form.get("last_name"),
                        "address": request.form.get("address"),
                        "phone_number": request.form.get("phone_number")
                    }
            }
        )
        return redirect(url_for("contacts"))

    return render_template("add_contact.html")


if __name__ == "__main__":
    app.run(debug=True)
