from typing import Optional, Annotated
from uuid import uuid4

from fastapi import FastAPI, Query, Path, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import uvicorn

from models import Contact, get_db, User
from pydantic_models import ContactModel, ContactModelResponse, UserModel


app = FastAPI()


async def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token")), db: AsyncSession = Depends(get_db)):
    query = select(User).where(User.token == token)
    result = await db.execute(query)
    user: Optional[User] = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

    return user


@app.post("/token/")
async def get_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    query = select(User).where(User.username == form_data.username)
    user: Optional[User] = (await db.execute(query)).scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    if user.password != form_data.password:
        user.token = None
        await db.commit()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    user.token = uuid4().hex
    await db.commit()
    return {"access_token": user.token, "token_type": "bearer"}


@app.post("/users/", tags=["Users"], summary="Додати нового користувача", status_code=status.HTTP_201_CREATED)
async def add_user(user_model: UserModel, db: AsyncSession = Depends(get_db)):
    user = User(**user_model.model_dump())
    db.add(user)
    await db.commit()


@app.get("/users/me111111/", tags=["Users"], summary="Отримати інформацію про користувача", status_code=status.HTTP_200_OK)
async def get_user(current_user: User = Depends(get_current_user)):
    return current_user


@app.post("/contacts/", tags=["Contacts"], summary="Додати новий контакт", status_code=status.HTTP_201_CREATED, response_model=ContactModelResponse)
async def add_contact(contact_model: ContactModel, db: AsyncSession = Depends(get_db)):
    contact = Contact(**contact_model.model_dump())
    db.add(contact)
    await db.commit()
    # await db.refresh(contact)
    return contact


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
