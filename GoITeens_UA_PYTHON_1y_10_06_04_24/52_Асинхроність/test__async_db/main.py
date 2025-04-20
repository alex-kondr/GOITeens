from fastapi import FastAPI, Query, HTTPException, status
import uvicorn

from database import database, products_db, create_db


# create_db()

app = FastAPI()
users_db = []


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/products/", status_code=status.HTTP_201_CREATED)
async def add_product(name: str = Query(description="Назва товару")):
    query = products_db.select().where(products_db.c.name==name)
    product = await database.fetch_one(query)
    if product:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Такий товар вже існує")

    product = products_db.insert().values(name=name)
    await database.execute(product)
    return dict(msg=f"Товар '{name}' успішно додано")


@app.get("/products/", status_code=status.HTTP_200_OK)
async def get_products():
    query = products_db.select()
    products = await database.fetch_all(query)
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Товари відсутні")
    return dict(msg="Всі наявні товари", products=products)


@app.get("/products/{product_id}/")
async def get_product(product_id: int):
    query = products_db.select().where(products_db.c.id==product_id)
    product = await database.fetch_one(query)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Товар з id '{product_id}' не знайдено")
    return dict(product=product)


@app.delete("/products/{product_id}/")
async def delete_product(product_id: int):
    query = products_db.select().where(products_db.c.id==product_id)
    product = await database.fetch_one(query)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Товар з id '{product_id}' не знайдено")

    query = products_db.delete().where(products_db.c.id==product_id)
    await database.execute(query)
    return dict(msg=f"Товар з id '{product_id}' успішно видалено")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
