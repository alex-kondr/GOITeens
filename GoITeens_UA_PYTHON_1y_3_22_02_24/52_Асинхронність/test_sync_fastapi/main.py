from fastapi import FastAPI, Query
import uvicorn

import db


app = FastAPI()


@app.get("/")
async def index():
    return dict(msg="Вітаємо в нашій системі")


@app.post("/add_data/")
async def add_data(name: str = Query(), data: str = Query()):
    if name not in db.data:
        db.data.update({name: data})
        return dict(msg="Дані успішно збережені")
    else:
        return dict(msg="Такі дані з такою назвою вже існують")


@app.get("/data/")
async def get_data():
    return dict(data=db.data, msg="Тут відображаються всі наявні дані")


if __name__ == "__main__":
    uvicorn.run("main:app")

