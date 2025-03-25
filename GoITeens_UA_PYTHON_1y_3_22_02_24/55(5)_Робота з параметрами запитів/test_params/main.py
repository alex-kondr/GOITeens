from typing import List, Union, Optional, Dict

from pydantic import BaseModel
from fastapi import FastAPI, Query, Path, HTTPException, status, Header
from fastapi.responses import JSONResponse, HTMLResponse
import uvicorn

from data import users


app = FastAPI()


@app.get("/users/")
async def get_users():
    return JSONResponse(content=users, status_code=status.HTTP_200_OK)


@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(title="The ID of the user to get", ge=1, le=10)):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return JSONResponse(content=user, status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@app.get("/users/{user_id}/name")
async def get_user_name(user_id: int, x_token: Optional[str] = Header(None, description="Secret token"), accept: str = Header(description="The response media type")):
    if x_token != "token":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    print(f"{accept=}")

    user = next((user for user in users if user["id"] == user_id), None)
    if user:

        if accept == "application/json":
                return JSONResponse(content=user["name"], status_code=status.HTTP_200_OK)
        elif accept == "text/html":
                return HTMLResponse(content=f"<h1>{user['name']}</h1>", status_code=status.HTTP_200_OK)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")



if __name__ == "__main__":
    uvicorn.run(app)

