from fastapi import FastAPI, Request, Response, status


app = FastAPI()
JWT_TOKEN = "Bearer 123456"


@app.middleware("http")
async def check_secure(request: Request, call_next):
    if 'Authorization' not in request.headers or request.headers["Authorization"] != JWT_TOKEN:
        return Response(content="Невірний jwt token", status_code=status.HTTP_403_FORBIDDEN)

    return await call_next(request)


@app.get("/secure/")
async def secure():
    return "Захищений маршрут!"
