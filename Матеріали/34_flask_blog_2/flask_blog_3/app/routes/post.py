from flask import Blueprint, request, render_template, flash, redirect, url_for

from app.db import Session, User, Post
from app.data.password import ADMIN_PASS


post_route = Blueprint("posts", __name__)


@post_route.get("/posts/")
@post_route.post("/posts/")
def add_post():
    block = False
    msg1 = ""

    with Session() as session:
        if request.method == "POST":
            title = request.form.get("title")
            text = request.form.get("text")
            user_id = request.form.get("user_id")
            post = Post(title=title, text=text, user_id=user_id)

            if request.form.get("password") == ADMIN_PASS:
                session.add(post)
                session.commit()
                flash("Статтю успішно додано")
                msg1 = "Статтю успішно додано"
            else:
                flash("Не вірний пароль", "block")
                block = True

        users = session.query(User).all()
        context = {
            "msg": msg1,
            "block": block,
            "users": users
        }
        return render_template("add_post.html", **context)


@post_route.get("/post/<int:id>")
def get_post(id):
    with Session() as session:
        post = session.query(Post).where(Post.id == id).first()
        return render_template("post.html", post=post)


@post_route.get("/")
def index():
    with Session() as session:
        posts = session.query(Post).all()
        return render_template("index.html", posts=posts)


@post_route.post("/post/del/<int:id>/")
def del_post(id):
    with Session() as session:
        if request.form.get("password") == ADMIN_PASS:
            session.query(Post).where(Post.id == id).delete()
            session.commit()
            return redirect("/")
        else:
            flash("Не вірний пароль", "block")
            return redirect(f"/post/{id}")


@post_route.get("/post/edit/<int:id>")
@post_route.post("/post/edit/<int:id>")
def edit_post(id):
    with Session() as session:
        post = session.query(Post).where(Post.id == id).first()

        if request.method == "POST":
            if request.form.get("password") == ADMIN_PASS:
                post.title = request.form.get("title")
                post.text = request.form.get("text")
                session.commit()
                return redirect(url_for("posts.get_post", id=id))
            else:
                flash("Невірний пароль")

        return render_template("add_post.html", post=post)