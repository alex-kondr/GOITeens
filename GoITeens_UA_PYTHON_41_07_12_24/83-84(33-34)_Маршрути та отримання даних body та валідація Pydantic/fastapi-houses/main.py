from typing import Optional, List, Dict

from fastapi import FastAPI, HTTPException, status, Path, Query, Body
import requests
import uvicorn
from pydantic import BaseModel, Field, field_validator


class House(BaseModel):
    index: int = Field(..., ge=0, examples=[1, 2, 5])
    house: str = Field(..., min_length=3, max_length=50)
    emoji: Optional[str] = Field(None)
    founder: str = Field(..., description="Староста")
    colors: List = []
    animal: Optional[str] = None

    @field_validator("house")
    def validate_house(cls, value: str):
        if value.count(" ") != 0:
            raise ValueError("Назва не повинна містити пробіли")

        return value

    @field_validator("founder")
    def validate_founder(cls, value: str):
        if value.count(" ") != 1:
            raise ValueError("Дане поле повинно містити один пробіл")

        return value


HOUSES: List[Dict] = requests.get("https://potterapi-fedeperin.vercel.app/uk/houses").json()

app = FastAPI()


@app.get("/houses/", status_code=status.HTTP_202_ACCEPTED, response_model=List[House])
async def get_houses():
    return HOUSES


@app.post("/houses/", status_code=status.HTTP_201_CREATED, response_model=House)
async def add_house(house: House = Body(..., description="Заповніть поля")):
    HOUSES.append(house)
    return house


if __name__ == "__main__":
    uvicorn.run("main:app")
