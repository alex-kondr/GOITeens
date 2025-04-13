from fastapi import FastAPI, Query
import uvicorn


app = FastAPI()
products = []

@app.get("/hello/")
def hello(
    name: str = Query("Анонім", description="Вкажіть своє ім'я"),
    age: int = Query(..., description="Вкажіть свій вік"),
    city: str = Query("Одеса", description="Ваше місто проживання")
):
    return dict(msg=f"Вітаю! Мене звати '{name}'. Мені {age} р. та проживаю в {city}.")


@app.post("/products/")
def add_product(
    index: int = Query(..., description="Номер по порядку"),
    name: str = Query(..., description="Назва товару")
):
    products.append(dict(
        index=index,
        name=name
    ))
    return dict(msg=f"Товар '{name}' успішно додано під номером {index}.")


@app.get("/products/")
def get_products():
    return dict(
        msg="Всі наявні товари",
        products=products
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)
