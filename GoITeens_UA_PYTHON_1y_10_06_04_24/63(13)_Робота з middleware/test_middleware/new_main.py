from typing import Callable

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
import uvicorn


new_app = FastAPI()


@new_app.middleware("http")
async def test_middleware(request: Request, call_next: Callable) -> Response:
    if request.headers.get("Authorization"):
        return await call_next()
    return JSONResponse(content="Not authorization", status_code=401)


@new_app.get("/")
async def start():
    return "Все працює"


if __name__ == "__main__":
    uvicorn.run("new_main:new_app")
