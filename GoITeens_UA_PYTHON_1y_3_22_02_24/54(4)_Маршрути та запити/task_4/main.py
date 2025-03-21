from typing import Optional, List, Union

from fastapi import FastAPI, HTTPException, status
import uvicorn
from pydantic import BaseModel

from products import products_data


app = FastAPI()


class ProductModel(BaseModel):
    id: int
    name: str
    price: Optional[float] = None


@app.get("/products/{product_id}/", response_model=ProductModel, status_code=status.HTTP_200_OK)
async def get_product(product_id: int):
    product = [product for product in products_data if product.get("id") == product_id]
    if product:
        return product[0]

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")


@app.get("/products/", response_model=List[ProductModel], status_code=status.HTTP_200_OK)
async def get_products():
    return products_data


@app.post("/products/", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductModel):
    products_data.append(product.model_dump())
    return dict(msg="Created")


@app.put("/products/{product_id}/", response_model=ProductModel, status_code=status.HTTP_202_ACCEPTED)
async def update_product(product_id: int, product_model: ProductModel):
    for product in products_data:
        if product.get("id") == product_id:
            product["id"] = product_model.model_dump()["id"]
            product["name"] = product_model.model_dump()["name"]
            product["price"] = product_model.model_dump()["price"]
            return product


@app.patch("/products/{param}/{products_id}/", status_code=status.HTTP_202_ACCEPTED)
async def update_param_product(param: str, product_id: int, value: Union[str, float, int]):
    for product in products_data:
        if product.get("id") == product_id:
            if param in product:
                product[param] = value
                return

            else:
                raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Parametr invalid")


if __name__ == "__main__":
    uvicorn.run("main:app")
