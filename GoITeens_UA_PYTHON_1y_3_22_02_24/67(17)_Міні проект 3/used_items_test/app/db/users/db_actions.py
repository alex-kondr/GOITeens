from typing import Annotated, Optional

import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.config import settings
from app.db.users.models import User, get_db
from app.pydantic_models.users.models import UserModel


async def get_user(username: str, db: AsyncSession) -> Optional[User]:
    query = select(User).filter_by(username=username)
    result = await db.execute(query)
    return result.scalar_one_or_none()


def decode_token(token: str) -> str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload: dict = jwt.decode(jwt=token, key=settings.secret_key, algorithms=[settings.algorithm])
        username = payload.get("sub")
        if not username:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    return username


async def sign_up(user_model: UserModel, db: AsyncSession):
    if await get_user(username=user_model.username, db=db):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Такий користувач вже зареєстрований")

    user = User(**user_model.model_dump())
    db.add(user)
    await db.commit()


async def login(user_model: UserModel, db: AsyncSession) -> str:
    user: Optional[User] = await get_user(username=user_model.username, db=db)
    if not user or not user.verify_password(user_model.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Логін або пароль не вірний")
    return user.create_access_token()


async def get_current_user(token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="/users/token/"))], db: Annotated[AsyncSession, Depends(get_db)]) -> Optional[User]:
    username = decode_token(token)
    user: Optional[User] = await get_user(username=username, db=db)
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Неактивний користувач")
    return user
