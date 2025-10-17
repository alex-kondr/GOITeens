from typing import Optional, List, Dict

from fastapi import FastAPI, status, HTTPException, Path, Query, Header
from fastapi.responses import JSONResponse
import uvicorn
import requests


BOOKS: List[Dict[str, str|int]] = requests.get("https://potterapi-fedeperin.vercel.app/uk/books").json()


app = FastAPI()


@app.get("/books/")
async def get_books():
    # return dict(books=BOOKS)
    return JSONResponse(content=BOOKS, status_code=status.HTTP_202_ACCEPTED)


@app.get("/books/index/{index}/", status_code=status.HTTP_202_ACCEPTED)
async def get_book(index: int = Path(..., description="Індекс книги")):
    return next((book for book in BOOKS if book.get('index') == index), {})


@app.get("/books/number/{number}/", status_code=status.HTTP_202_ACCEPTED)
async def get_book_number(number: int = Path(..., description="Номер книги")):
    return next((book for book in BOOKS if book.get("number") == number), {})


@app.post("/books/", status_code=status.HTTP_201_CREATED)
async def add_book(
    number: int = Query(..., description="Номер книги"),
    title: str = Query(..., description="Назва книги"),
    originalTitle: Optional[str] = Query(None, description="Назва оригіналу"),
    releaseDate: Optional[str] = Query(None, description="Дата виходу книги"),
    description: Optional[str] = Query(None, description="Опис книги"),
    pages: int = Query(..., description="Кількість сторінок"),
    cover: Optional[str] = Query(None, description="Обложка книги"),
    index: int = Query(..., description="Індекс книги")
):
    BOOKS.append(dict(
        number=number,
        title=title,
        originalTitle=originalTitle,
        releaseDate=releaseDate,
        description=description,
        pages=pages,
        cover=cover,
        index=index
    ))
    return dict(message="Нову книгу успішно додано до списку")


@app.put("/books/{index}/", status_code=status.HTTP_202_ACCEPTED)
async def update_book(
    index: int = Path(..., description="Індекс книги"),
    number: Optional[int] = Query(None, description="Номер книги"),
    title: Optional[str] = Query(None, description="Назва книги"),
    originalTitle: Optional[str] = Query(None, description="Назва оригіналу"),
    releaseDate: Optional[str] = Query(None, description="Дата виходу книги"),
    description: Optional[str] = Query(None, description="Опис книги"),
    pages: Optional[int] = Query(None, description="Кількість сторінок"),
    cover: Optional[str] = Query(None, description="Обложка книги"),
):
    book = next((book for book in BOOKS if book["index"] == index), None)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Книгу з таким індексом не знайдено")

    if number:
        book["number"] = number
    if title:
        book["title"] = title
    if originalTitle:
        book["originalTitle"] = originalTitle
    if releaseDate:
        book["releaseDate"] = releaseDate
    if description:
        book["description"] = description
    if pages:
        book["pages"] = pages
    if cover:
        book["cover"] = cover

    return book


@app.delete("/books/{index}/")
async def remove_book(index: int = Path(..., description="Індекс книги")):
    for i, book in enumerate(BOOKS):
        if book["index"] == index:
            break
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Книгу з індексом '{index}' не знайдено")

    book = BOOKS.pop(i)
    return dict(
        message="Книга успішно видалена",
        book=book
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
