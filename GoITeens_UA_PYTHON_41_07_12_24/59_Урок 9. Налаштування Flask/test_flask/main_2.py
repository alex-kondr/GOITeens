from flask import Flask


app = Flask(__name__)


books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "genre": "Dystopian"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic"}
]


@app.get("/")
def index():
    return "<h1>Головна сторінка</h1>"


@app.get("/books/")
def get_books():
    return "".join([f"<p>title: {book['title']} author: {book['author']} genre: {book['genre']}</p>" for book in books])


@app.get("/books/<int:id>/")
def get_book(id: int):
    book = next((book for book in books if book["id"]==id))
    return f"<p>title: {book['title']} author: {book['author']} genre: {book['genre']}</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
