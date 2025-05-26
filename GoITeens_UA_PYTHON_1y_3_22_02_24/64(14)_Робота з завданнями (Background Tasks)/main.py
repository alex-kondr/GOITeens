import asyncio
from email import message
import logging
from turtle import back
from typing import Annotated

from fastapi import FastAPI, BackgroundTasks, UploadFile, File
import uvicorn
from queue import Queue


app = FastAPI()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("test_logger")


async def send_mail(email: str):
    await asyncio.sleep(2)
    logger.info(f"Email sended to {email}")


async def add_file(file: UploadFile):
    await asyncio.sleep(2)
    logger.info(f"Файлік '{file.filename}' завантажено")


@app.post("/send_email/")
async def send_email(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_mail, email)
    return {"message": "Email sending in the background"}


@app.post("/uploadfile/")
async def create_upload_file(file: Annotated[UploadFile, File(...)], background_tasks: BackgroundTasks):
    background_tasks.add_task(add_file, file)
    return {"filename": file.filename}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)

