from fastapi import FastAPI, Query
import uvicorn


app = FastAPI()


@app.get("/message/")
async def say_hello(message: str = Query()):
    return dict(msg=message)


if __name__ == "__main__":
    uvicorn.run(app)
