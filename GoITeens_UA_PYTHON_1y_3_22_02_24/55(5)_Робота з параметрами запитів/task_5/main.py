from typing import List, Union, Dict, Optional
import time

from fastapi import FastAPI, Query, Path, Header, HTTPException, status
from fastapi.responses import JSONResponse, HTMLResponse
import uvicorn

from data import users


app = FastAPI()
SECRET = "secret"


@app.get("/users/", status_code=status.HTTP_200_OK)
async def get_users(
    Authorization: Optional[str] = Header(None, description="Bearer you_token"),
    Accept: str = Header(str(time.time()), description="Type data")
    ):
    if "json" in Accept and Authorization == f"Bearer {SECRET}":
        return JSONResponse(content=users)
    elif "html" in Accept and Authorization == f"Bearer {SECRET}":
        return HTMLResponse(content=f"<h1>{users}</h1>")

    return HTTPException(status_code=status.HTTP_403_FORBIDDEN)


@app.get("/users/name/", status_code=status.HTTP_200_OK)
async def get_user_name(name: str = Query(..., description="Введіть ім'я користувача для пошуку")):
    user = next((user for user in users if user["name"] == name), None)
    if user:
        return JSONResponse(content=user)
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get("/users/{user_id}/")
async def get_user(user_id: int = Path(..., description="User ID", gt=0, le=10)):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return JSONResponse(content=user)
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Користувача з id {user_id} не знайдено")




if __name__ == "__main__":
    uvicorn.run(app)
