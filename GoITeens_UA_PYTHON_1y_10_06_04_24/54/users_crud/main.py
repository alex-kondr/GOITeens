from typing import List, Optional, Union

from sqlalchemy import insert, select, delete, update
from fastapi import FastAPI, HTTPException, status, Query
from fastapi.concurrency import asynccontextmanager
from pydantic import BaseModel, EmailStr
import uvicorn

from models import User, database


class UserModel(BaseModel):
    name: Optional[str] = None
    email: EmailStr


class UserModelResponse(UserModel):
    id: int


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def add_user(user_model: UserModel):
    query = select(User).filter_by(email=user_model.email)
    user = await database.fetch_one(query)
    if user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Користувач з email={user_model.email} вже зареєстровий у системі")

    query = insert(User).values(**user_model.model_dump())
    await database.execute(query)


@app.get("/users/found/", response_model=UserModelResponse)
async def get_user_by_attr(
    name: Optional[str] = Query(None, description="Ім'я користувача для пошуку"),
    email: Optional[str] = Query(None, description="Email для пошуку")
):
    if name and email:
        query = select(User).filter_by(name=name, email=email)
    elif name:
        query = select(User).filter_by(name=name)
    elif email:
        query = select(User).filter_by(email=email)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    user = await database.fetch_one(query)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


@app.get("/users/{user_id}/", response_model=UserModelResponse)
async def get_user_by_id(user_id: int):
    query = select(User).filter_by(id=user_id)
    user = await database.fetch_one(query)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Користувача з таким ID не знайдено")

    return user


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
