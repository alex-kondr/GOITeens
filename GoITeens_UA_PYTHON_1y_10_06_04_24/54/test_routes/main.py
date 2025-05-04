from typing import List, Optional

from fastapi import FastAPI, HTTPException, status, Query
from pydantic import BaseModel
import uvicorn


class Product(BaseModel):
    id: int
    name: str
    quantity: int
    category: str


app = FastAPI()
products: List[Product] = []


# @app.post("/products/", status_code=status.HTTP_201_CREATED)
# async def add_product(id: int, name: str, quantity: int, category: str):
#     product = Product(id=id, name=name, quantity=quantity, category=category)
#     products.append(product)
#     return dict(msg="OK")


# @app.post("/products/{id}/{name}/{quantity}/{category}/", status_code=status.HTTP_201_CREATED)
# async def add_product(id: int, name: str, quantity: int, category: str):
#     product = Product(id=id, name=name, quantity=quantity, category=category)
#     products.append(product)
#     return dict(msg="OK")


@app.post("/products/", status_code=status.HTTP_201_CREATED)
async def add_product(product: Product):
    products.append(product)
    return dict(msg="OK")


@app.get("/products/", response_model=List[Product])
async def get_products():
    return products


@app.get("/products/{product_id}/", response_model=Product, status_code=status.HTTP_200_OK)
async def get_product(product_id: int):
    product = next((product for product in products if product.id==product_id), None)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Товар з таким ID не знайдено")
    return product


@app.delete("/products/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int):
    product = next((product for product in products if product.id==product_id), None)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Товар з таким ID не знайдено")
    products.remove(product)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
