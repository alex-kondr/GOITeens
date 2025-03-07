from fastapi import FastAPI, HTTPException, Query
import uvicorn

from database import database, users, create_db


app = FastAPI()

# create_db()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/add_user/")
async def add_user(name: str = Query(), age: int = Query(None)):
    query = users.select().where(users.c.name == name)
    user = await database.fetch_one(query)
    if user:
        raise HTTPException(status_code=400, detail="User exists")

    query = users.insert().values(name=name, age=age)
    await database.execute(query)
    return dict(name=name)


@app.get("/users/")
async def get_users():
    query = users.select()
    all_users = await database.fetch_all(query)
    return dict(users=all_users)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)