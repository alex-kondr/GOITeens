from flask import Flask, render_template, redirect


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
    return redirect("/")


@app.get("/contacts/")
def contacts():
    return render_template("contacts.html")


if __name__ == "__main__":
    app.run(debug=True, port=1234)