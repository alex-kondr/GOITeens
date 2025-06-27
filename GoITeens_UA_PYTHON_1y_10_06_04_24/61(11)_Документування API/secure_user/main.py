from typing import List, Union, Optional, Annotated
from uuid import uuid4

from fastapi import FastAPI, HTTPException, status, Path, Query, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
import uvicorn

from pydantic_models import UserModel, UserResponse, ContactModel, ContactModelResponse, Token, UserPassword
from models import get_db, User, Contact


app = FastAPI()


async def get_user(db: Annotated[AsyncSession, Depends(get_db)], token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))) -> Optional[User]:
    query = select(User).filter_by(token=token)
    result = await db.execute(query)
    user: Optional[User] = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Не вірний токен")

    return user


@app.post(
    "/users/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse, tags=["User"],
    summary="Реєстрація користувача",
    description="Для реєстрації введіть логін та пароль",
    name="Sign up"
)
async def create_user(user_model: UserModel, db: AsyncSession = Depends(get_db)):
    query = select(User).filter_by(username=user_model.username)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Користувач з таким логіном вже зареєстрований")

    user = User(**user_model.model_dump())
    db.add(user)
    await db.commit()
    return user


@app.post(
    "/token/",
    status_code=status.HTTP_200_OK, response_model=Token,
    summary="Отримання токену",
    description="Для входу у систему введіть логін та пароль",
    tags=["User"]
)
async def get_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: AsyncSession = Depends(get_db)):
    query = select(User).filter_by(username=form_data.username, password=form_data.password)
    result = await db.execute(query)
    user: Optional[User] = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Логін або пароль невірний")

    token = uuid4().hex
    user.token = token
    await db.commit()
    return dict(access_token=token)


@app.get(
    "/users/me/",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=UserResponse,
    tags=["User"],
    summary="Інформація про користувача",
    description="Для отримання інформації передайте токен"
)
async def get_user_me(user: Annotated[User, Depends(get_user)]):
    return user


@app.patch(
    "/users/update_password/",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=UserResponse,
    tags=["User", "Contact"],
    summary="Зміна пароля",
    description="Для зміни паролю передайте токен та новий пароль",
    deprecated=True
)
async def update_password(
    password_model: UserPassword,
    db: Annotated[AsyncSession, Depends(get_db)],
    user: Annotated[User, Depends(get_user)]
):
    user.password = password_model.password
    await db.commit()
    return user


@app.post(
    "/contacts/",
    status_code=status.HTTP_201_CREATED,
    response_model=ContactModelResponse,
    tags=["Contact"],
    summary="Створити новий контакт",
    description="Для додавання нового контакту передайте токен та необхідні поля"
)
async def add_contact(
    contact_model: ContactModel,
    user: Annotated[User, Depends(get_user)],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    contact = Contact(**contact_model.model_dump(), user_id=user.id)
    db.add(contact)
    await db.commit()
    return contact


@app.get(
    "/contacts/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Список всіх контактів користувача",
    tags=["Contact"],
    response_model=List[ContactModelResponse]
)
async def get_contacts(
    user: Annotated[User, Depends(get_user)],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    query = select(Contact).filter_by(user_id=user.id)
    result = await db.execute(query)
    return result.scalars()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
