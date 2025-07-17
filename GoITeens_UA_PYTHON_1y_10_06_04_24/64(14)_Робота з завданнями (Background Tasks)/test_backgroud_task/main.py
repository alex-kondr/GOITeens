import logging
import asyncio
import time
import random

from fastapi import FastAPI, HTTPException, status, BackgroundTasks, File, UploadFile
import uvicorn


app = FastAPI()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(funcName)s(%(filename)s) - %(message)s")
my_log = logging.getLogger(name="test_backgroud")


async def send_mail(text: str):
    time_start = time.time()
    my_log.info(f"Початок відправки повідомлення: {text}")
    await asyncio.sleep(random.randint(1, 8))
    time_end = time.time()
    my_log.info(f"Повідомлення успішно надіслано за {time_end - time_start} с")


async def resize_file(file: UploadFile):
    time_start = time.time()
    my_log.info(f"Початок обробки файлу: {file.filename}")
    await asyncio.sleep(random.randint(1, 8))
    time_stop = time.time()
    my_log.info(f"Файл '{file.filename}' успішно оброблено: {time_stop - time_start} с")


@app.post("/send-mail/")
async def test_send_mail(backgroud_task: BackgroundTasks, text: str):
    backgroud_task.add_task(send_mail, text)
    return f"Ваше повідомлення '{text}' буде надіслано найближчим часом"


@app.post("/resize-file/", status_code=status.HTTP_202_ACCEPTED)
async def test_resize_file(backgroud_task: BackgroundTasks, file: UploadFile = File(...)):
    backgroud_task.add_task(resize_file, file)
    return f"Файл '{file.filename}' скоро буде оброблено."


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
