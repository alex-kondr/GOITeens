from fastapi import FastAPI, Query, Path, Header, Request, Response, HTTPException, status
import uvicorn
import logging
import time

import secure_app


app = FastAPI()
app.mount("/check/", secure_app.app)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(name="test log")
# tokens = ["token1", "token2", "token3"]
# JWT_TOKEN = "Bearer Token"


# @app.middleware("http")
# async def add_logging(request: Request, call_next):
#     log.info("Стартувала перевірка запиту....")
#     start_time = time.time()

#     # if "token" not in request.headers or request.headers["token"] not in tokens:
#     #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Відсутній або невірний токен")

#     if 'Authorization' not in request.headers or request.headers["Authorization"] != JWT_TOKEN:
#         return Response(content="Невірний jwt token", status_code=status.HTTP_403_FORBIDDEN)

#     time.sleep(2)
#     response: Response = await call_next(request)
#     runing_time = time.time() - start_time
#     response.headers["TIME-EXECUTE"] = f"{runing_time * 1000} mc"
#     log.info("Перевірка запиту завершилась успішно!")
#     return response


@app.get("/hello/")
async def hello():
    return "Hello world!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
