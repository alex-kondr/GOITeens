from typing import Optional, List, Dict, Annotated, Union
import random

from fastapi import FastAPI, status, HTTPException, Path, Query
import uvicorn
from pydantic import BaseModel, field_validator, Field


class ProductModel(BaseModel):
    name: str = Field(description="Назва товару", examples=["Хліб", "Сіль"], min_length=3, title="Товар", alias="new_name")
    count: int = Field(default=1, description="К-ть товару", examples=[1, 5, 9], gt=0, le=100, title="Кількість")

    @field_validator("count", mode="before")
    @classmethod
    def count_validator(cls, value: Union[int, str]):
        if isinstance(value, str):
            value = int(float(value))
        return value

    model_config = {
        "json_schema_extra" : {
            "examples" : [
                {
                    "name": "Хліб",
                    "count": 5
                },
                {
                    "name": "Сіль",
                    "count" : 10
                }
            ]
        }
    }


class ProductResponse(BaseModel):
    id: int = Field(..., description="ID номер товару")
    name: str
    count: int


PRODUCTS: List[ProductResponse] = []


app = FastAPI(title="Новий супер застосунок", description="Застосунок для обліку товарів", version="0.0.1")


@app.post(
    "/products/",
    summary="Додати новий товар",
    description="Тут Ви зможете додати товар",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductResponse
)
async def add_product(product: ProductModel):
    product_response = ProductResponse(**product.model_dump(), id=random.randint(1, 1000))
    PRODUCTS.append(product_response)
    return product_response

@app.get("/products/", response_model=List[ProductResponse], tags=["Product"])
async def get_products():
    return PRODUCTS


@app.get("/products/{id}/", response_model=ProductResponse, tags=["Product"])
async def get_product(id: int = Path(..., description="ID товару")):
    product = next((prod for prod in PRODUCTS if prod.id == id), None)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Товару з таким ID не знайдено")
    return product


if __name__ == "__main__":
    uvicorn.run("main:app")
