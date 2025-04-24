from typing import Optional, Union, List

from fastapi import FastAPI
import uvicorn

from models import Country, City, Address, Product, People


app = FastAPI()


@app.post("/country/", response_model=Country)
async def add_country(country: Country):
    return country


@app.post("/city/", response_model=City)
async def add_city(city: City):
    return city


@app.post("/address", response_model=Address)
async def add_address(address: Address):
    return address


@app.post("/product/", response_model=Product)
async def add_product(product: Product):
    return product


@app.post("/people/", response_model=People)
async def add_people(people: People):
    return people


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)