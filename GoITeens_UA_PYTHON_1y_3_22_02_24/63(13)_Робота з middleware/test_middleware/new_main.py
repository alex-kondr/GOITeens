from fastapi import FastAPI


new_app = FastAPI()


@new_app.get("/")
async def main():
    return dict(msg="Зовсім інший застосунок!!!")
