import asyncio
import logging
from pathlib import Path
import shutil
import io
from PIL import Image

from fastapi import FastAPI, BackgroundTasks, status, Query, Depends, HTTPException, File, UploadFile
import uvicorn
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models import User, Message, get_db


FILES_PATH = "files/"
app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test_backgroud")


async def send_message(text: str, user_id: int, db: AsyncSession = Depends(get_db)):
    message = Message(send_mail=text, user_id=user_id)
    db.add(message)
    await db.commit()
    logging.info(f"Повідомлення '{text}' успішно надіслано від користувача '{user_id}'")

    await asyncio.sleep(5)

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

    backgroud_task.add_task(send_message, text=text, user_id=user.id)
    return dict(msg="Ваше повідомлення скоро буде надіслано")


@app.post("/files/")
async def add_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    file_path = Path(FILES_PATH) / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_path": file_path}


def resize_image(image_data: bytes, max_size: tuple=(100, 200)) -> bytes:
    with Image.open(io.BytesIO(image_data)) as img:
        img.thumbnail(max_size)
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format=img.format)
        return img_byte_array.getvalue()


async def process_image(file_path: str):
    with open(file_path, "rb") as file:
        resized_image = resize_image(file.read())

    with open(file_path, "wb") as file:
        file.write(resized_image)

@app.post("/upload-photo/")
async def upload_photo(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    file_location = f"files/{file.filename}"
    with open(file_location, "wb") as saved_file:
        saved_file.write(file.file.read())

    background_tasks.add_task(process_image, file_location)

    return {"info": "Фотографія завантажена, розпочато обробку."}



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
