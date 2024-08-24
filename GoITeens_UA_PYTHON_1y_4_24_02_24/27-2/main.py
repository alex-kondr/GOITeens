from flask import Flask, render_template, redirect


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index2.html")


@app.route("/page_2/")
def page_2():
    return render_template("page_2.html")


@app.route("/2/")
def redir():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="localhost")