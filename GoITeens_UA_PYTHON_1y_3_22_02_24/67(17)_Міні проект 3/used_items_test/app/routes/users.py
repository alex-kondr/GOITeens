from typing import Optional, Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.users.models import User, get_db
from app.db.users import db_actions
from app.pydantic_models.users.models import UserModel, Token, UserModelDB


users_route = APIRouter(prefix="/users", tags=["User"])


@users_route.post("/", status_code=status.HTTP_201_CREATED)
async def sign_up(user_model: UserModel, db: Annotated[AsyncSession, Depends(get_db)]):
    await db_actions.sign_up(user_model, db)


@users_route.post("/token/", status_code=status.HTTP_200_OK)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[AsyncSession, Depends(get_db)]):
    user_model = UserModel(username=form_data.username, password=form_data.password)
    token = await db_actions.login(user_model, db)
    return Token(access_token=token)


@users_route.get("/me/", status_code=status.HTTP_202_ACCEPTED, response_model=UserModelDB)
async def get_user(current_user: User = Depends(db_actions.get_current_user)):
    return current_user
