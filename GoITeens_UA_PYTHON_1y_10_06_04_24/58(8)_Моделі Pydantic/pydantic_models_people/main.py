from typing import List

from fastapi import FastAPI, Path, status, HTTPException
import uvicorn

import data
from pydantic_models import People


app = FastAPI()


@app.get("/people/", status_code=status.HTTP_200_OK, response_model=List[People])
async def get_people():
    return data.get_data()


@app.get("/people/{index}/", status_code=status.HTTP_200_OK, response_model=People)
async def get_human(index: int = Path(..., ge=0)):
    human = next((human for human in data.get_data() if human.get("index") == index), None)

    if not human:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Такий індекс відсутній у списку")

    return human


@app.post("/people/", status_code=status.HTTP_201_CREATED, response_model=People)
async def add_human(human_model: People):
    data.add_human(human_model.model_dump())
    return human_model


@app.delete("/people/{index}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_human(index: int = Path(..., ge=0)):
    human = next((human for human in data.get_data() if human.get("index") == index), None)

    if not human:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Такий індекс відсутній у списку")

    data.delete_human(human)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
