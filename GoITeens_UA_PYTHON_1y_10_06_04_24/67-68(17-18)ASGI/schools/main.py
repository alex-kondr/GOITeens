import asyncio

from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
import uvicorn

from app.db.models import create_db
from app.routes.users import users_route
from app.routes.subjects import subjects_route


app = FastAPI(root_path="/api")
app.include_router(users_route)
app.include_router(subjects_route)

# app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(TrustedHostMiddleware, ["localhost", "127.0.0.1"])
app.add_middleware(GZipMiddleware, minimum_size=1000)


if __name__ == "__main__":
    # asyncio.run(create_db())
    uvicorn.run("main:app", reload=True)

