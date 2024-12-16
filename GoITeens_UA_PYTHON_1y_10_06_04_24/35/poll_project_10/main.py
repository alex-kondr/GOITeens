from flask import Flask, render_template, redirect, request, url_for

from data import functions


app = Flask(__name__)


@app.get("/poll/")
def poll():
    question = "Яка мова програмування тобі подобається найбільше?"
    answers = ["Python", "JS", "C++", "C#", "TS", "Java", "Basic", "Assembler"]
    return render_template("poll.html", question=question, answers=answers)


@app.get("/add_vote/")
def add_vote():
    vote = request.args.get("vote")
    functions.write_file(vote)
    return redirect(url_for("results"))


@app.get("/results/")
def results():
    answers = functions.read_file()
    return render_template("results.html", answers=answers)


if __name__ == "__main__":
    app.run(debug=True)