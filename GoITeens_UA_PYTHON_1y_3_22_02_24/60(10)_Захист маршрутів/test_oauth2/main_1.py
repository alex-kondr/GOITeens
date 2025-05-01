from uuid import uuid4

from fastapi.concurrency import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn
from sqlalchemy import select, delete, update, insert

from models import database, User


app = FastAPI()
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/token/")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


async def get_current_user(token: str = Depends(oauth2_schema)):
    query = select(User).where(User.token == token)
    user = await database.fetch_one(query)

    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Невірний токен",
        headers={"WWW-Authenticate": "Bearer"}
    )


@app.post("/token/")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    query = select(User).where(User.email == form_data.username)
    user: User = await database.fetch_one(query)

    if user and user.password == form_data.password:
        return dict(access_token="123456", token_type="bearer")

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Логін або пароль не вірні",
        headers={"WWW-Authenticate": "Bearer"}
    )


@app.get("/users/me/")
async def read_users_me(current_user: str = Depends(get_current_user)):
    return dict(user=current_user)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
