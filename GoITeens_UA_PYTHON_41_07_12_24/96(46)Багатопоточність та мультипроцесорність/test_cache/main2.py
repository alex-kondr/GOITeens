import asyncio
from datetime import datetime
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, Query, Path
import redis.asyncio as async_redis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis_client = async_redis.from_url(
        url="redis://redis-16374.crce175.eu-north-1-1.ec2.cloud.redislabs.com:16374/database-MI0KUVVE",
        decode_responses=True,
        username="default",
        password="V2IgDD0VXip7HA8Fu8szYZh83M5tdy3I"
    )

    FastAPICache.init(RedisBackend(redis_client), prefix="Fastapi_cache", expire=60)
    yield
    await FastAPICache.clear(namespace="Fastapi_cache")


app = FastAPI(lifespan=lifespan)


@app.get("/cache_test/{user_id}/")
@cache(expire=10)
async def get_user(user_id: int = Path(...)):
    await asyncio.sleep(5)
    return {
        "user_id": user_id,
        "now": datetime.now()
    }


@app.get("/products/{prod_id}/")
@cache()
async def get_product(prod_id: int = Path(...)):
    await asyncio.sleep(5)
    return {
        "product_id": prod_id,
        "now": datetime.now()
    }


if __name__ == "__main__":
    uvicorn.run("main2:app")
