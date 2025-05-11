from fastapi import FastAPI, Query, Path, Header, HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.concurrency import asynccontextmanager
import uvicorn
from sqlalchemy import insert, select, delete, update

from data import data
from models import House, database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)


def is_validate_token(token: str) -> bool:
    return token == "Bearer super_token"


@app.get("/houses/", status_code=status.HTTP_200_OK)
async def get_house_by_animal(animal: str = Query(..., description="Вкажіть назву тварини для пошуку", examples=["Лев"], min_length=2)):
    houses = [house for house in data if house.get("animal") == animal]
    if not houses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(houses, status_code=status.HTTP_200_OK)


@app.get("/houses_path/{index}/")
async def get_house_by_id(index: int = Path(..., description="Індекс будинку", examples=[1, 3, 0], gt=-1, le=3)):
    house = next((house for house in data if house.get("index") == index), None)
    if not house:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return HTMLResponse(f"<h1>{house}<h1/>", status_code=status.HTTP_200_OK)


@app.get("/houses_head/", status_code=status.HTTP_200_OK)
async def get_house_by_house(
    house: str = Header(..., description="Назва будинку"),
    Authorization: str = Header(..., description="Bearer token", examples=["Bearer you_token"])
):
    if Authorization == "Bearer 12345678":
        house = next((house for house in data if house.get("house") == house), None)
        if not house:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return house
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="У вас немає відповідних прав")


@app.post("/houses/", status_code=status.HTTP_201_CREATED, summary="Пошук та додавання факультету до бази даних")
async def add_house(
    name: str = Query(..., description="Назва факультету для пошуку"),
    Authorization: str = Header(..., description="Bearer token", examples=["Bearer you_token"]),
):
    if is_validate_token(Authorization):
        house = next((house for house in data if house.get("house") == name), None)
        if not house:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Такого факультету не створено")
        query = insert(House).values(index=house.get("index"), house=house.get("house"), animal=house.get("animal"))
        await database.execute(query)
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="За цим токеном доступ заборонено")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
