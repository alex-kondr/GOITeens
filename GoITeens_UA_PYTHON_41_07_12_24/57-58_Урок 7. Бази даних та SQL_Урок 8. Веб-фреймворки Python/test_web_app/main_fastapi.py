from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def index():
    return "Стартова сторінка"


@app.post("/")
def post_test():
    return "Тестовий POST маршрут"


@app.delete("/")
def delete_test():
    return "Тестовий DELETE маршрут"


if __name__ == "__main__":
    uvicorn.run("main_fastapi:app")