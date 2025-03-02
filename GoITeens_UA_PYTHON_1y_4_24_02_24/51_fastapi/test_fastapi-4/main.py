from fastapi import FastAPI, Query

import data


app = FastAPI()


@app.get("/")
def index():
    return dict(msg="Hello world!")


@app.get("/name/")
def get_name(
    name: str = Query("Ви не ввели ім'я", description="Введіть своє ім'я"),
    age: int = Query(0, description="Введіть свій вік")
):
    return dict(
        msg=f"Вітаю '{name}' в нашій інформаційній системі",
        age=age,
        age_type=f"{type(age)}"
        )


@app.get("/departures/")
def departures(departure: str = Query(None, description="Виберіть напрямок (ex.: odesa)")):
    if departure:
        return dict(msg=data.departures.get(departure, "Такий напрямоу відсутній"))

    return dict(msg=data.departures)


@app.get("/tours/")
def tours(tour_id: int = Query(None, description="Введіть індекс туру")):
    if tour_id:
        return dict(msg=data.tours.get(tour_id, "Такого туру немає"))

    return dict(msg=data.tours)


@app.get("/tour/")
def get_tour(tour_id: int = Query(description="Введіть індекс туру"), param: str = Query(None, description="Яка інформація Вас цікавить")):
    if param:
        return dict(msg=data.tours.get(tour_id, {}).get(param))

    return dict(msg=data.tours.get(tour_id))