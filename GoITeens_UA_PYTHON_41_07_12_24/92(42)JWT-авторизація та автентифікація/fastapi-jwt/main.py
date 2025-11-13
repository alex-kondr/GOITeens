from typing import Annotated
from datetime import datetime, timedelta, timezone

from fastapi import FastAPI, Path, Query, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn
import jwt
from jwt.exceptions import InvalidTokenError


SECRET_KEY = "secret key"


app = FastAPI()


def get_user(token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="/token/"))]):
    try:
        payload: dict = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return dict(user=f"User from {user_id}")

    except InvalidTokenError as error:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Error: {error}")


@app.post("/token/")
async def get_token(form: Annotated[OAuth2PasswordRequestForm, Depends()]):
    if form.username == "login" and form.password == "super_pass":
        payload = dict(sub="user_id_5", exp=datetime.now(timezone.utc) + timedelta(minutes=1))
        print(f"{payload = }")
        token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm="HS256")
        return dict(access_token=token, type_token="Bearer")

    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


@app.get("/users/me/")
async def get_me(user: Annotated[str, Depends(get_user)], file: UploadFile = File(...)):
    return user


if __name__ == "__main__":
    uvicorn.run("main:app")
