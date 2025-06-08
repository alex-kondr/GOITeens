from typing import List, Union, Optional

from fastapi import FastAPI, status, HTTPException, Path, Query
import uvicorn

from models import User


users: List[User] = []

app = FastAPI()


@app.post("/users/", status_code=status.HTTP_201_CREATED, response_model=User)
async def add_user(user_model: User):
    users.append(user_model)
    return user_model


@app.get("/users/", status_code=status.HTTP_202_ACCEPTED, response_model=List[User])
async def get_users():
    return users


@app.get("/users/{full_name}/", status_code=status.HTTP_202_ACCEPTED, response_model=User)
async def get_user(full_name: str = Path(..., examples=["Вася Пупкін"])):
    user = next((user for user in users if user.full_name == full_name), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Такого користувача не знайдено")
    return user


@app.delete("/users/", status_code=status.HTTP_204_NO_CONTENT)
async def remove_user(full_name: str = Query(...)):
    user = next((user for user in users if user.full_name == full_name), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Такого користувача не знайдено")
    users.remove(user)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
