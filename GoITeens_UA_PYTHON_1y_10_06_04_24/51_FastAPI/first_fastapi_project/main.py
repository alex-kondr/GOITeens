from fastapi import FastAPI, Query
import uvicorn


app = FastAPI()


@app.get("/test-api/")
def test_api():
    return dict(msg="Привіт! Вітаємо в нашій новій системі")


@app.get("/params/")
def test_params(name: str = "...", age: int = 0):
    return dict(
        msg="Ви надіслали такі параметри",
        name=name,
        age=age
    )


@app.get("/book/")
def get_book(
    name: str = Query("Alex", description="Введіть назву книги для пошуку"),
    author: str = Query(..., description="Введіть автора книги")
):
    return dict(
        msg=f"Шукаємо книгу з назвою '{name}', яку написав '{author}'"
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)
