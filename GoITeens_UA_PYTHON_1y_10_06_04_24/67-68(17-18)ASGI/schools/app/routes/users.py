from typing import Optional, List, Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Path, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
import jwt
from jwt.exceptions import InvalidTokenError

from app.db.models import User, get_db
from app.pydantic_models.users import UserModel, UserModelResponse, TokenModel
from app.config import settings
from app.db import db_actions


users_route = APIRouter(prefix="/users", tags=["User"])


def get_user_id(token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="/users/token/"))]):
    try:
        payload: dict = jwt.decode(token, key=settings.secret_key, algorithms=[settings.algorithm])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return int(user_id)
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@users_route.post("/", status_code=status.HTTP_201_CREATED, summary="Реєстрація нового користувача")
async def sign_up(
    user_model: UserModel,
    db: Annotated[AsyncSession, Depends(get_db)]
):
    await db_actions.sign_up(user_model=user_model, db=db)


@users_route.post("/token/", status_code=status.HTTP_202_ACCEPTED, response_model=TokenModel, summary="Вхід у систему та отримання токену")
async def sign_in(
    form: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    token = await db_actions.sign_in(name=form.username, password=form.password, db=db)
    if not token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return dict(access_token=token)


@users_route.get("/", status_code=status.HTTP_202_ACCEPTED, response_model=UserModelResponse, summary="Отримати інформацію про користувача")
async def get_me(
    user_id: Annotated[str, Depends(get_user_id)],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    return await db_actions.get_user(id=user_id, db=db)
