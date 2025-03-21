# Query
# Path (add, subtract, multiply, divide, sqrt, square)

from typing import List

from fastapi import FastAPI, Query
import uvicorn


app = FastAPI()


@app.get("/calculator/?num_1=5&action=")
async def calc(action: str, number_1: float, number_2: float):
    if action == "add":
        result = number_1 + number_2
    elif action == "subtract":
        result = number_1 - number_2
    elif action == "square":
        result = [number_1 ** 2, number_2 ** 2]

    return dict(result=result)

# /calc/add/4/2.5
@app.get("/calc/{action}/{number_1}/{number_2}/")
async def calc2(action: str, number_1: float, number_2: float, name: str):
    if action == "add":
        result = number_1 + number_2
    elif action == "subtract":
        result = number_1 - number_2
    elif action == "square":
        result = [number_1 ** 2, number_2 ** 2]

    return dict(result=result)


if __name__ == "__main__":
    uvicorn.run("calculator:app")