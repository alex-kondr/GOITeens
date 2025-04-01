from ctypes.wintypes import tagRECT
from re import S
from reprlib import recursive_repr
from urllib import request
from aiohttp import ClientSession
import bs4
from fastapi import FastAPI, Path, Query, HTTPException, status
from fastapi.responses import JSONResponse
import uvicorn
import requests


app = FastAPI()


async def fetch(url: str) -> str:
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

def sync_fetch(url: str) -> str:
    html = requests.get(url).text
    print(html)


# sync_fetch("https://en.wikipedia.org/wiki/Python_(programming_language)")



@app.get("/url/")
async def get_url(
    url: str = Query(description="your url"),
    find_text: str = Query(..., description="what you want to find"),
    # find_elem: str = Query(..., description="html tag of what you want to find")
) -> JSONResponse:
    html = await fetch(url)

    # with open("index.html", "w", encoding= "utf-8") as f:
    #     f.write(html)
    # html = sync_fetch(url)
    # print(url)


    soup = bs4.BeautifulSoup(html, "lxml")
    text = soup(string=find_text)
    
    # text = soup.find_all(string=find_text)
    # for t in text:
    #     t = t.find_parent('tr')
    #     if t:
    #         t = t.find_next('td')
    #         if t:
    #             print(t)
    #             print('-----------------------')
                # return JSONResponse(t.text)
    # print(text)
    # if text:
    #     return JSONResponse(text.text)
    # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)


# with open("index.html", "r", encoding= "utf-8") as f:
#     html = f.read()

# soup = bs4.BeautifulSoup(html, "lxml")
# # # tr = soup.tr.find_all_next(string="Paradigm")[0].parent
# # # tr = soup.select(':-soup-contains-own("Paradigm")')[0].find_parent('tr').td.text
# tr = soup.find(string="Paradigm").find_parent('tr').find_next('td').text
# # tr = soup.find(string="Paradigm").parent.parent.parent.td.text
# print(tr)

