import asyncio
from typing import Dict, List, Optional, Annotated
import time
from datetime import datetime
import json

from fastapi import FastAPI, Depends, Path, Query
import uvicorn
import redis.asyncio as asyncredic

redis_client: Optional[asyncredic.Redis] = None
cache: Dict[int, Dict[str, str]] = {}
app = FastAPI()


@app.on_event("startup")
async def on_startup():
    global redis_client
    redis_client = asyncredic.from_url(
        url="redis://",
        decode_responses=True,
        username="default",
        password="pass"
    )


@app.on_event("shutdown")
async def on_shutdown():
    await redis_client.close()


async def get_redis():
    return redis_client


@app.get("/product/{id}/")
async def get_product(id: int = Path(...), client: asyncredic.Redis = Depends(get_redis)):
    # product = cache.get(id)
    product: Dict = await client.get(id)
    if product:
        product = json.loads(product)
        product.update({"cache": True})
        return product

    start_time = time.time()
    await asyncio.sleep(5)

    product = {
        "message": f"Товар з id={id} знайдено",
        "time": time.time() - start_time
    }
    # await client.set(id, None)
    # cache.update({id: product})
    await client.set(id, json.dumps(product), ex=10)

    return product


if __name__ == "__main__":
    uvicorn.run("main:app")
