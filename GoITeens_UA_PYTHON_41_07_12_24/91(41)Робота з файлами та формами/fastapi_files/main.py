import os, logging, shutil, io

from fastapi import FastAPI, File, UploadFile, HTTPException, status, BackgroundTasks, Path
import uvicorn
import asyncio
from PIL import Image


app = FastAPI()
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)


async def send_mail(text: str, recepient: str):
    await asyncio.sleep(5)
    logging.info(f"Повідомлення '{text}' успішно надіслано до '{recepient}'.")


async def resize_img(file_path: str, max_size: tuple = (100, 300)):
    with open(file_path, "rb") as img_data:
        with Image.open(io.BytesIO(img_data.read())) as img:
            img.thumbnail(max_size)
            with open("resized_img/img.jpg", "wb") as file:
                img.save(file, format=img.format)


@app.post("/add_file/", status_code=status.HTTP_201_CREATED)
async def add_file(file: UploadFile = File(...)):
    file_path = os.path.join("files", file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return f"Файл '{file.filename}' успішно збережено!"


@app.get("/file/{file_name}/")
async def get_file(file_name: str = Path(...)):
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()
    return text


@app.post("/send_mail/")
async def mail_service(text: str, recepient: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_mail, text, recepient)
    message = f"Створено завдання відправити повідомлення '{text}'."
    logging.info(message)
    return message


@app.post("/upload_img/")
async def upload_img(background_tasts: BackgroundTasks, file: UploadFile = File(...)):
    file_path = os.path.join("files", file.filename)
    with open(file_path, "wb") as file_obj:
        shutil.copyfileobj(file.file, file_obj)

    background_tasts.add_task(resize_img, file_path)

    return f"Файл '{file.filename}' успішно збережено та оброблено"


if __name__ == "__main__":
    uvicorn.run("main:app")
