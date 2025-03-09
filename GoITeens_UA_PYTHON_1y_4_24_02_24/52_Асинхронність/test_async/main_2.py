from fastapi import FastAPI
import uvicorn
my_list = []

app = FastAPI()


@app.get("/")
async def index():
    return dict(msg="Все чудово працює!")


if __name__ == "__main__":
    uvicorn.run("main_2:app")
