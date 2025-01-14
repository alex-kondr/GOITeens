from flask import Flask, render_template, url_for, redirect

from src.models import Session, Review, Grade, create_db
from src.forms import ReviewForm


app = Flask(__name__, template_folder="src/templates")
app.secret_key = "secret_key"


@app.route("/add_review/", methods=["GET", "POST"])
def add_review():
    form = ReviewForm()

    with Session() as session:
        grades = session.query(Grade).all()
        form.grade.choices = []
        for grade in grades:
            form.grade.choices.append((grade.id, grade.grade))

        if form.validate_on_submit():
            review = Review(
                author=form.author.data,
                text=form.text.data,
                grade_id=form.grade.data
            )
            session.add(review)
            session.commit()
            return redirect(url_for("show_reviews"))


        return render_template("add_review.html", form=form)


@app.get("/reviews/")
def show_reviews():
    with Session() as session:
        reviews = session.query(Review).all()
        return render_template("reviews.html", reviews=reviews)


if __name__ == "__main__":
    create_db()
    app.run(debug=True, port=5050)
