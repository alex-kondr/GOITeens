import sqlite3
import psycopg2
import psycopg

from flask import Flask, render_template, redirect, request, g, url_for


app = Flask(__name__)


def get_db():
    if "db" not in g:
        # g.db = sqlite3.connect("products.db")
        conn_info = psycopg.connection.conninfo_to_dict("postgres://avnadmin:AVNS_YqhgeEauuP-KVS-t6os@internet-shop-4-alex-kondr.e.aivencloud.com:13316/defaultdb?sslmode=require")
        g.db = psycopg2.connect(**conn_info)
        # g.db = psycopg2.connect(
        #     host="internet-shop-4-alex-kondr.e.aivencloud.com",
        #     port=13316,
        #     user="avnadmin",
        #     password="AVNS_YqhgeEauuP-KVS-t6os",
        #     database="defaultdb"
        # )

    return g.db


def create_db():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            count INTEGER NOT NULL
        );
    """)
    db.commit()


@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.get("/")
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products;")
    products = cursor.fetchall()
    cursor.close()
    return render_template("index.html", products=products)


@app.route("/add-product/", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form.get("name")
        count = request.form.get("count")
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO products (name, count) VALUES (%s, %s)", (name, count))
        db.commit()
        return redirect(url_for("index"))

    return render_template("add_product.html")


if __name__ == "__main__":
    with app.app_context():
        create_db()

    app.run(debug=True)
