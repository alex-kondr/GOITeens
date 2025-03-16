from fastapi import FastAPI, Query
import uvicorn
from aiohttp import ClientSession
from sqlalchemy import insert, select

import db


# db.create_db()

URL = "https://jsonplaceholder.typicode.com/users/"
app = FastAPI()


async def fetch(url: str):
    async with ClientSession() as client:
        response = await client.get(url)
        return await response.json()


@app.on_event("startup")
async def startup():
    await db.database.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.database.disconnect()


@app.post("/add_user/")
async def add_user(name: str = Query(description="Введіть ім'я користувача")):
    query = db.users.insert().values(name=name)
    print(f"{query = }")
    f"INSERT INTO users(id, name) VALUES (1, {name})"
    "SELECT 1"
    await db.database.execute(query)
    return dict(msg=f"Користувача '{name}' успішно додано")


@app.get("/users/")
async def get_users():
    query = db.users.select()
    print(f"{query = }")
    "SELECT * FROM users"
    users = await db.database.fetch_all(query)
    return dict(msg="Запит дозволено", users=users)


@app.get("/users/{user_id}/")
async def get_user(user_id: int):
    query = db.users.select().filter_by(id=user_id)
    print(f"{query = }")
    f"SELECT * FROM users WHERE id={user_id}"
    user = await db.database.fetch_one(query)
    return dict(msg="Запит дозволено", user=user)


@app.get("/people/")
async def get_people():
    users = await fetch(URL)
    for user in users:
        query = insert(db.People).values(
            name=user.get("name"),
            username=user.get("username"),
            email=user.get("email")
        )
        await db.database.execute(query)
    return dict(msg="Нові користувач успішно додані")


@app.get("/people_from_db/")
async def people_from_db():
    query = select(db.People)
    users = await db.database.fetch_all(query)
    return dict(msg=users)


if __name__ == "__main__":
    uvicorn.run("main:app")
