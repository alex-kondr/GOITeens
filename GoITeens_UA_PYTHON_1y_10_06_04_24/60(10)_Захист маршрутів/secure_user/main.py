from typing import List, Union, Optional
from uuid import uuid4

from fastapi import FastAPI, HTTPException, status, Path, Query, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from pydantic_models import UserModel, UserResponse
from models import get_db, User, Contact


app = FastAPI()


async def get_user(db: AsyncSession, token: str = OAuth2PasswordBearer(tokenUrl="token")) -> Optional[User]:
    query = select(User).filter_by(token=token)
    result = await db.execute(query)
    user: Optional[User] = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Не вірний токен")

    return user


@app.post("/users/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(user_model: UserModel, db: AsyncSession = Depends(get_db)):
    user = User(**user_model.model_dump())
    db.add(user)
    await db.commit()
    return user


@app.post("/token/", status_code=status.HTTP_200_OK)
async def get_token(user_model: UserModel, db: AsyncSession = Depends(get_db)):
    query = select(User).filter_by(username=user_model.username, password=user_model.password)
    result = await db.execute(query)
    user: Optional[User] = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Логін або пароль невірний")

    token = uuid4().hex
    user.token = token
    await db.commit()
    return dict(access_token=token, toke_type="bearer")
