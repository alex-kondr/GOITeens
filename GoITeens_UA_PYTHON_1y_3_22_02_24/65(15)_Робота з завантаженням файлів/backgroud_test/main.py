import asyncio
import logging
from typing import List
from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, BackgroundTasks, status, Query, Depends, HTTPException, File, UploadFile
import uvicorn
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import aiofiles
from PIL import Image

from models import User, Message, get_db
from pydantic_models import UserModel, MessageModel


app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test_backgroud")
ORIGINAL_PATH = Path("files/original")
RESIZED_PATH = Path("files/resized")
ALLOW_TYPE = {"image/jpeg", "image/png"}


async def send_message(text: str, user_id: int, db: AsyncSession):
    message = Message(send_mail=text, user_id=user_id)
    db.add(message)
    await db.commit()
    logging.info(f"Повідомлення '{text}' успішно надіслано від користувача '{user_id}'")

    await asyncio.sleep(10)

    await db.refresh(message)
    message.incoming = f"Надійшла відповідь для користувача '{user_id}'"
    await db.commit()
    logging.info(f"Надійшла відповідь для користувача '{user_id}'")


@app.post("/send_mail/", status_code=status.HTTP_201_CREATED)
async def send_mail(
    backgroud_task: BackgroundTasks,
    text: str = Query(..., description="Повідомлення"),
    login: str = Query(..., description="Логін користувача"),
    db: AsyncSession = Depends(get_db)
):
    query = select(User).filter_by(login=login)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    backgroud_task.add_task(send_message, text=text, user_id=user.id, db=db)
    return dict(msg="Ваше повідомлення скоро буде надіслано")


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def sign_up(user_model: UserModel, db: AsyncSession = Depends(get_db)):
    user = User(**user_model.model_dump())
    db.add(user)
    await db.commit()


@app.get("/mail/", status_code=status.HTTP_202_ACCEPTED, response_model=List[MessageModel])
async def get_messages(login: str, db: AsyncSession = Depends(get_db)):
    query = select(User).filter_by(login=login)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    query = select(Message).filter_by(user_id=user.id)
    result = await db.execute(query)
    messages = result.scalars().all()
    return messages


async def resized_image(file_name: str, max_size: tuple = (100, 200)):
    with Image.open(ORIGINAL_PATH / file_name) as image:
        image.load()

    image.thumbnail(max_size)
    image.save(RESIZED_PATH / file_name)


@app.post("/files/", status_code=status.HTTP_201_CREATED)
async def add_file(backgroud_task: BackgroundTasks, file: UploadFile = File(...)):
    if file.content_type not in ALLOW_TYPE:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="Не підтримуваний тип файлу")

    type_file = file.filename.split(".")[-1]
    new_file_name = ORIGINAL_PATH / (uuid4().hex + f".{type_file}")

    async with aiofiles.open(new_file_name, "wb") as fh:
        content = await file.read()
        await fh.write(content)

    backgroud_task.add_task(resized_image, file.filename)

    return dict(msg="Файл успішно завантажено і почався процес обробки файлу")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
