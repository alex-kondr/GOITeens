from fastapi import FastAPI, Path, Query, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBasic, HTTPBasicCredentials
import uvicorn


app = FastAPI()


async def get_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    if token != "super_secret":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Невірний токен")
    return "super_user"


async def verification_http_basic(credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
    if credentials.username != "login1" or credentials.password != "password1":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return "super_basic_user"


@app.get("/secret/user/", status_code=status.HTTP_200_OK)
async def get_secret_user(user: str = Depends(get_user)):
    return user


@app.get("/unsecret/user/", status_code=status.HTTP_200_OK)
async def get_unsecret_user():
    return "not_super_user"


@app.post("/token/", status_code=status.HTTP_202_ACCEPTED)
async def get_token(form: OAuth2PasswordRequestForm = Depends()):
    if form.username != "login" or form.password != "password":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Логін або пароль не вірний.")
    return dict(access_token="super_secret", token_type="Bearer")


@app.get("/basic/user/")
async def get_basic_user(user: str = Depends(verification_http_basic)):
    return user


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
