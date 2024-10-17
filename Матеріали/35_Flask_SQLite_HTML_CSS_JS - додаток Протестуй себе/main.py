from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.get("/")
def index():
    data = {
        "question": "Яка мова програмування тобі подобається найбільше?",
        "fields": ["Python", "JS", "C++", "C#"]
    }
    return render_template("index.html", data=data)


@app.get("/poll/")
def poll():
    vote = request.args.get("vote")
    with open("data/answers.txt", "a", encoding="utf=8") as file:
        file.write(vote + "\n")

    return redirect(url_for("answers"))


@app.get("/answers/")
def answers():
    with open("data/answers.txt", "r", encoding="utf-8") as file:
        votes = file.readlines()
        return render_template("answers.html", votes=votes)

if __name__ == "__main__":
    app.run(debug=True)
