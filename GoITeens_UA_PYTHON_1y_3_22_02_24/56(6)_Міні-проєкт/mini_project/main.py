from fastapi import FastAPI, Path, Query, HTTPException, status
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
from aiohttp import ClientSession
import uvicorn
import re


app = FastAPI()


async def requests_fetch(url):
    asession = AsyncHTMLSession()
    response = await asession.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return response.html


async def aiohttp_fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
            return await response.text()


@app.get("/requests/{tag}/")
async def get_requests(
    tag: str = Path(description="html tag"),
    url: str = Query(description="url"),
    find: str = Query(description="find")
):
    html = await requests_fetch(url)
    if "h" in tag:
        text = html.xpath(f'((//{tag}|//div)[contains(., "{find}")]/following-sibling::p)[1]//text()')
    else:
        text = html.xpath(f'//{tag}[contains(., "{find}")]//text()')

    if not text:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    text = "".join(text)
    return dict(text=text)


@app.get("/bs4/{tag}/")
async def get_bs4(
    tag: str = Path(description="html tag"),
    url: str = Query(description="url"),
    find: str = Query(description="find")
):
    html = await aiohttp_fetch(url)
    soup = BeautifulSoup(html, "lxml")

    text = soup.find(string=re.compile(find)).find_previous(tag)

    if not text:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return dict(text=text.get_text())


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

