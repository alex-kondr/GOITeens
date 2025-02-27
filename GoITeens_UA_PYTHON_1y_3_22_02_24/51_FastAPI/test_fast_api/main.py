from fastapi import FastAPI, Query


app = FastAPI()


@app.get("/")
def index():
    return {"msg": "Hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!"}


@app.get("/name/")
def read_name(name: str = Query(None, description="Введіть своє ім'я"), number1: int = Query(0)):
    return dict(msg=f"Вітаю {name}")
# timeless - weeknd