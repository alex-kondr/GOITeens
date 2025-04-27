from typing import List, Dict, Optional, Union

from fastapi import FastAPI, Query, status, HTTPException, Path
from sqlalchemy import insert, select, delete
from aiohttp import ClientSession
import uvicorn

from db import User, database


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/users/")
async def add_users(
    name: str = Query(..., description="Ім'я користувача"),
    address: Optional[str] = Query(None, description="Адреса користувача")
):
    query = insert(User).values(name=name, address=address)
    await database.execute(query)
    return dict(msg=f"Користувача з ім'ям '{name}' та адресою '{address}' успішно створено.")


@app.get("/users/")
async def get_users():
    users = await database.fetch_all(select(User))
    return users


@app.get("/users/name/")
async def get_user_by_name(name: str = Query(..., description="Ім'я користувача")):
    query = select(User).where(User.name==name)
    user = await database.fetch_one(query)
    if user:
        return dict(msg="Користувача знайдено", user=user)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Користувача з ім'я '{name}' не знайдено")


@app.get("/users/{user_id}/")
async def get_user_by_id(user_id: int = Path(..., description="ID користувача")):
    query = select(User).filter_by(id=user_id)
    user = await database.fetch_one(query)
    if user:
        return dict(msg="Користувача знайдено", user=user)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Користувача з id '{user_id}' не знайдено")


@app.delete("/users/{user_id}/")
async def get_user_by_id(user_id: int = Path(..., description="ID користувача")):
    query = delete(User).where(User.id==user_id)
    await database.execute(query)
    return dict(msg=f"Користувача з ID '{user_id}' успішно видалено")


async def fetch_data(url: str = "https://jsonplaceholder.typicode.com/users/") -> List[Dict]:
    async with ClientSession() as session:
        response = await session.get(url)
        return await response.json()


@app.get("/users_json/")
async def get_users_by_json():
    users = await fetch_data()
    return dict(msg="Список користувачів", users=users)


@app.get("/users_json/{user_id}/")
async def get_user_by_json_id(user_id: int = Path(..., description="ID користувача")):
    users = await fetch_data()
    user = next((user for user in users if user.get("id")==user_id), None)
    if user:
        return dict(msg="Користувача знайдено", user=user)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Користувача не знайдено")


@app.get("/user_json/")
async def get_user_by_json_name(name: str = Query(..., description="Ім'я користувача")):
    users = await fetch_data()
    user = next((user for user in users if user.get("name")==name), None)
    if user:
        return dict(msg="Користувача знайдено", user=user)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Користувача не знайдено")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
