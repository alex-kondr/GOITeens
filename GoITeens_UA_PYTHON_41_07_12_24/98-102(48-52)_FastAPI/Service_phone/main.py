import asyncio

from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
import uvicorn

from src.db.models import User, Problem, ResponseModel, Message, get_db, create_db


template = Jinja2Templates(directory="src/templates")

app = FastAPI()


@app.get("/")
async def index(request: Request):
    return template.TemplateResponse(request=request, name="index.html", context=dict(message="Hello!"))


if __name__ == "__main__":
    # asyncio.run(create_db())
    uvicorn.run("main:app")
