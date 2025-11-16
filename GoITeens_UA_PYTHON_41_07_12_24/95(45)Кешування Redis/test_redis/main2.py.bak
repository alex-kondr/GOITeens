import asyncio
import time
from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import FastAPI
from fastapi_cache import FastAPICache  # fastapi-cache2 redis
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis # Використовуємо асинхронний клієнт Redis

# --- Конфігурація FastAPI Lifespan ---

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Підключення до Redis та ініціалізація кешу
    # Замініть 'redis://localhost:6379' на ваш фактичний URL Redis
    redis = aioredis.from_url("redis://localhost:6379", encoding="utf8", decode_responses=True)

    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    print("FastAPICache ініціалізовано з Redis бекендом.")

    yield # Додаток працює

    # 2. Очищення ресурсів (опціонально)
    # FastAPICache.clear()
    print("FastAPI завершує роботу.")


app = FastAPI(lifespan=lifespan)

# --- Маршрути з кешуванням ---

@app.get("/items/{item_id}")
@cache(expire=30) # Кешувати результат цього роуту на 30 секунд
async def get_item(item_id: int):
    """
    Приклад маршруту, який кешується.
    Імітуємо повільну роботу (наприклад, запит до бази даних).
    """

    # Імітація тривалої операції
    await asyncio.sleep(2)

    # Коли запит обслуговується кешем (Cache HIT), ця частина не виконується
    current_time = datetime.now()

    return {
        "item_id": item_id,
        "name": f"Item Name {item_id}",
        "data_source": "DATABASE_OR_SLOW_SERVICE",
        "generated_at": current_time
    }

@app.get("/status")
async def status():
    """
    Маршрут для перевірки, що додаток працює.
    """
    return {"status": "ok", "cache_backend": str(FastAPICache.get_backend())}

# --- Запуск додатка (У командному рядку) ---

# uvicorn main:app --reload