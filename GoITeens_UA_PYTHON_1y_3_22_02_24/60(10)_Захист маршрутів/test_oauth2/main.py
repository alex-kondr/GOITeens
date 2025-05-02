from uuid import uuid4

from fastapi.concurrency import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBasic, HTTPBasicCredentials
import uvicorn
from sqlalchemy import select, delete, update, insert
from sqlalchemy.orm import Session

from models import database, User, get_db
from pydantic_models import UserModel, UserModelResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/token/")
security = HTTPBasic()


async def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    query = select(User).where(User.email==credentials.username)
    user: User = await database.fetch_one(query)

    print(f"{credentials.username = }")
    print(f"{credentials.password = }")

    if not user or user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Невірні логін або пароль")

    return user


async def get_user(token: str = Depends(oauth2_schema)):
    query = select(User).where(User.token == token)
    user = await database.fetch_one(query)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Ойой, а це що це за токен?")

    return user


async def get_user_new(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    user: User = db.query(User).where(User.token==token).one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Невірний токен")

    return user





@app.post("/token/")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    query = select(User).where(User.email == form_data.username)
    user: User = await database.fetch_one(query)

    if not user or user.password != form_data.password:
        if user:
            query = update(User).where(User.id==user.id).values(token=None)
            await database.execute(query)

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Логін або пароль не вірні")

    accsess_token = uuid4().hex
    query = update(User).where(User.id == user.id).values(token=accsess_token)
    await database.execute(query)
    return dict(access_token=accsess_token, token_type="bearer")


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user_model: UserModel, db: Session = Depends(get_db)):
    user = db.query(User).where(User.email==user_model.email).one_or_none()

    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    user = User(**user_model.model_dump())
    db.add(user)
    db.commit()

    # query = insert(User).values(user.model_dump())
    # await database.execute(query)
    return dict(message="Користувача створено")


@app.get("/users/me/", status_code=status.HTTP_200_OK, response_model=UserModelResponse)
async def read_user(user: User = Depends(get_user)):
    return user


@app.get("/users/me/basic/", response_model=UserModelResponse, status_code=status.HTTP_200_OK)
async def get_user_basic(user: User = Depends(verify_credentials)):
    return user


@app.get("/users/me/new/", response_model=UserModelResponse, status_code=status.HTTP_200_OK)
async def read_user_new(user: User = Depends(get_user_new)):
    return user





if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
