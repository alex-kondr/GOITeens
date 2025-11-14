import io
from fastapi import FastAPI
from PIL import Image, ImageFilter
from pathlib import Path
import concurrent.futures
import zipfile
from fastapi.responses import FileResponse
import requests

app = FastAPI()

def process_image(url, count):
    """
    Функція для завантаження та обробки зображення (наприклад, застосування фільтра розмиття).
    Це CPU-bound завдання.
    """
    try:
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        # Застосування розмиття - CPU-інтенсивна операція
        image = image.filter(ImageFilter.GaussianBlur(1))
        temp_image_path = Path(f"temp_{count}.jpg")
        image.save(temp_image_path)
    except Exception as e:
        print(e)

def add_images_to_zip(zipf):
    """
    Додавання оброблених зображень до ZIP-файлу.
    """
    try:
        for i in range(10):
            image_path = Path(f"temp_{i}.jpg")
            zipf.write(image_path)
            image_path.unlink() # Видалення тимчасового файлу
    except Exception as e:
        print(e)

@app.get("/download-processed-images")
async def download_processed_images():
    try:
        url = "https://picsum.photos/200/300" # URL для отримання випадкового зображення
        futures_list = []
        zip_file_path = Path("processed_images.zip")

        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Використання ProcessPoolExecutor для паралельної обробки зображень
            with concurrent.futures.ProcessPoolExecutor() as executor:
                for i in range(10):
                    # Подача завдання на обробку зображення в пул процесів
                    future = executor.submit(process_image, url, i)
                    futures_list.append(future)
                # Очікування завершення всіх завдань
                concurrent.futures.wait(futures_list)

            # Додавання оброблених зображень до ZIP-файлу
            add_images_to_zip(zipf)

            return FileResponse(zip_file_path, headers={"Content-Disposition": "attachment; filename=processed_images.zip"})
    except Exception as e:
        print(e)
        return {"message": str(e)}

# Щоб запустити: uvicorn your_file_name:app --reload
# Потім відкрийте http://127.0.0.1:8000/download-processed-images