from typing import Optional

from fastapi import FastAPI, Depends
import redis.asyncio as redis
import uvicorn


app = FastAPI()
redis_client: Optional[redis.Redis] = None


@app.on_event("startup")
async def startup_event():
    global redis_client
    redis_client = redis.from_url(
        url="redis://local:15541/database",
        decode_responses=True,
        username="default",
        password="pass",
        )


@app.on_event("shutdown")
async def shutdows_event():
    await redis_client.close()


async def get_redis_client():
    return redis_client


@app.get("/cached_data")
async def get_data(key_db: str, redis: redis.Redis = Depends(get_redis_client)):
    cached_value = await redis.get(key_db)
    print(f"{cached_value = }")
    if cached_value:
        return {"message": "From cache", "data": cached_value}
    # ... fetch from database if not in cache ...
    await redis.set(key_db, "some_data", ex=300) # Cache for 5 minutes
    return {"message": "From DB", "data": "some_data"}


if __name__ == "__main__":
    uvicorn.run("main:app")
