from typing import List

from fastapi import FastAPI, status, HTTPException, Path
import uvicorn

from models import BookModel


app = FastAPI()
books = [BookModel(name="Зелена книга")]


@app.post("/books/", status_code=status.HTTP_201_CREATED)
async def add_book(book: BookModel):
    books.append(book)
    return dict(msg="OK")


@app.get("/books/", response_model=List[BookModel])
async def get_books():
    return books


@app.get("/books/{book_id}/", response_model=BookModel)
async def get_book(book_id: int = Path(description="Номер книги")):
    if 0 <= book_id < len(books):
        return books[book_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Такої книги не існує")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)
