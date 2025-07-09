import logging
import time
import asyncio

import uvicorn
from fastapi import FastAPI, HTTPException, status, Request, Response
from fastapi.responses import JSONResponse

from routes import test_route
from new_main import new_app


logging.basicConfig(level=logging.INFO)
log = logging.getLogger("LOGGER")
app = FastAPI(root_path="/")
app.include_router(test_route)
app.mount(app=new_app, path="/new-app")


# @app.middleware("http")
# async def test_middleware(request: Request, call_next) -> Response:
#     return call_next(request)


# @app.middleware("http")
# async def test_middleware(request: Request, call_next) -> Response:
#     token = request.headers.get("Authorization")
#     if not token or token != "Bearer token":
#         return JSONResponse(content=dict(detail="Токен неправильний"), status_code=status.HTTP_401_UNAUTHORIZED)

#     log.info("Старт middleware")
#     log.info(f"Твій супер-дупер токен: {token}")
#     time_start = time.time()
#     await asyncio.sleep(2)
#     response: Response = await call_next(request)
#     time_end = time.time()
#     message = f"Time execute {time_end - time_start} s"
#     log.info(message)
#     response.headers["Time-Execute"] = message
#     response.headers["Super-Token"] = token
#     log.info("Кінець middleware")
#     return response


@app.get("/test/", status_code=status.HTTP_200_OK)
async def test_route():
    return dict(msg="Тестовий роут")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
