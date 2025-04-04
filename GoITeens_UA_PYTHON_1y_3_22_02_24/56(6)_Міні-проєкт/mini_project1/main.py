import re

from bs4 import BeautifulSoup
from aiohttp import ClientSession
import asyncio
from requests_html import HTMLSession, AsyncHTMLSession
from fastapi import FastAPI, Path, Query, HTTPException, status
from fastapi.responses import JSONResponse
import asyncio


async def fetch_url_with_aiohttp(url: str) -> str:
    async with ClientSession() as session:
        response = await session.get(url)
        if response.status == 200:
            return await response.text(encoding="utf-8")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


async def fetch_url_with_requests_html(url: str) -> str:
    session = AsyncHTMLSession()
    response = await session.get(url)
    if response.status_code == 200:
        return response.html
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


# def fetch_url_with_requests_html(url: str) -> str:
#     session = HTMLSession()
#     response = session.get(url)
#     if response.status_code == 200:
#         return response.html
#     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


url = "https://uk.wikipedia.org/wiki/%D0%A0%D0%BE%D1%81%D1%96%D0%B9%D1%81%D1%8C%D0%BA%D0%BE-%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%B0_%D0%B2%D1%96%D0%B9%D0%BD%D0%B0_(%D0%B7_2014)"
tag = "p"
found_text = "До цього числа входять"

# -----------------------------------------------------------------
html = asyncio.run(fetch_url_with_aiohttp(url))

soup = BeautifulSoup(html, "lxml")
text = soup.find(string=re.compile(found_text)).find_parent(tag)

if text:
    print("text=", text.text)
    print("get_text=", text.get_text())
else:
    print("Not found")
# ------------------------------------------------------------------

html = asyncio.run(fetch_url_with_requests_html(url))

strings = html.xpath(f'//{tag}[contains(., "{found_text}")]//text()')

if strings:
    text = "".join(strings).replace("\n", "")
    print(f"{text=}")
else:
    print("Not found")
# ----------------------------------------------------------------