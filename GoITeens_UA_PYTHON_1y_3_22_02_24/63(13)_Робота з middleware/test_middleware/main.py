import time
import logging
import asyncio

from fastapi import FastAPI, Request, Response, HTTPException, status, Query
import uvicorn

from test_route import router
from new_main import new_app


app = FastAPI()
app.include_router(router)
app.mount("/new-app/", new_app)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test_middleware")


@app.middleware("http")
async def test_middleware(request: Request, call_next) -> Response:
    x_custom_header = request.headers.get("X-Custom-Header")
    if not x_custom_header:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Заголовок 'X-Custom-Header' є обов'язковим")

    time_start = time.time()

    response: Response = await call_next(request)
    await asyncio.sleep(1)

    time_end = time.time() - time_start
    logger.info(f"Визвали функцію {call_next} за допомогою методу {request.method} {request.url} витратили {time_end} с")
    response.headers["Execute-time"] = str(time_end)

    return response


@app.get("/message/")
async def test_message():
    logger.info("Повідомлення від основної функції")
    return dict(msg="Тестове повідомлення")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
