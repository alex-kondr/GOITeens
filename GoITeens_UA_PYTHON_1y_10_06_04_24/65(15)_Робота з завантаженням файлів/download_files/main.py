from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, HTTPException, UploadFile, File, status, BackgroundTasks, Depends
from PIL import Image
import aiofiles
import uvicorn
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import get_db, DownloadFile


app = FastAPI()
ORIGINAL_PATH = Path("files/original")
RESIZED_PATH = Path("files/resized")
ALLOW_TYPE = ["image/jpeg", "image/png"]


async def resize_img(filename: str, size: tuple = (100, 200)):
    with Image.open(ORIGINAL_PATH / filename) as img:
        img.load()

    img.thumbnail(size=size)
    img.save(RESIZED_PATH / filename)


@app.post("/files/", status_code=status.HTTP_200_OK, summary="Додайте файл для обробки")
async def resize_img_route(backgroud_tasks: BackgroundTasks, file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    if file.content_type not in ALLOW_TYPE:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="Даний тип файлу не підтримується програмою")

    file_type = file.filename.split(".")[-1]
    filename = f"{uuid4().hex}.{file_type}"
    file_path = ORIGINAL_PATH / filename

    download_file = DownloadFile(original_name=file.filename, name=file_path)
    db.add(download_file)
    await db.commit()

    async with aiofiles.open(file_path, "wb") as fh:
        content = await file.read()
        await fh.write(content)

    backgroud_tasks.add_task(resize_img, filename)
    return dict(message="Файл успішно завантажено і буде оброблено найближчим часом")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
