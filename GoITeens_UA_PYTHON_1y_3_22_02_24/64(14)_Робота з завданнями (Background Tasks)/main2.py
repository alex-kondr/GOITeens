import asyncio
import logging
import pytest

import uvicorn
from fastapi import FastAPI, BackgroundTasks


app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def example_task(name: str):
    try:
        await asyncio.sleep(2)
        if name == "error":
            raise ValueError("Помилкове завдання")
        logger.info(f"Завдання {name} успішно виконано")
    except Exception as e:
        logger.error(f"Помилка у завданні {name}: {e}")


@app.post("/add-task/")
async def add_task(background_tasks: BackgroundTasks, name: str):
    background_tasks.add_task(example_task, name)
    return {"message": f"Завдання {name} додано до фонових завдань"}


@app.get("/")
async def read_root():
    return {"message": "Вітаємо у FastAPI з моніторингом фонових завдань"}


async def process_data(data: str):
    await asyncio.sleep(1)
    return f"Оброблено: {data}"


@app.post("/process-data/")
async def process_data_endpoint(background_tasks: BackgroundTasks, data: str):
    background_tasks.add_task(process_data, data)
    return {"message": "Дані відправлені на обробку"}


@pytest.mark.asyncio
async def test_process_data():
    result = await process_data("test")
    assert result == "Оброблено: test"





if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
