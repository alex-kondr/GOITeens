from typing import Optional, List, Union

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBasic, HTTPBasicCredentials
from fastapi.concurrency import asynccontextmanager
from sqlalchemy import select, insert, update
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn

from models import get_db, User, get_async_db
from pydantic_models import UserModelResponse, UserModel


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await database.connect()
#     yield
#     await database.disconnect()


# oauth2_schema = OAuth2PasswordBearer(tokenUrl="/token/")
app = FastAPI()


# async def get_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
#     if token != "1234":
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Йой, а це со це за токен...)))")

#     user = db.query(User).where(User.id==1).one()
#     return user


# @app.post("/token/")
# async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     if form_data.username == "user" and form_data.password == "pass":
#         return dict(access_token="1234", token_type="bearer")
#     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Логін або пароль не вірні")


# @app.get("/users/me/", response_model=UserModelResponse)
# async def get_user_me(current_user: User = Depends(get_user)):
#     return current_user


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def add_user(user_model: UserModel, db: AsyncSession = Depends(get_async_db)):
    user = User(**user_model.model_dump())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user





if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
