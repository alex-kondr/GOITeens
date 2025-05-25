from fastapi import FastAPI, Query, status

from data import get_data_bs4, get_data_xpath


app = FastAPI()


@app.get("/get_text_bs4/", status_code=status.HTTP_302_FOUND)
async def get_text_bs4(url: str = Query(...), text: str = Query(...)):
    return await get_data_bs4(url, text)

