import asyncio
import re

from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
from aiohttp import ClientSession


URL = "https://uk.wikipedia.org/wiki/%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%B8%D0%B9_%D0%B0%D0%B4%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D0%B9_%D0%BA%D0%BE%D0%BB%D0%B0%D0%B9%D0%B4%D0%B5%D1%80"
TEXT = "Фінансування та розробку проєкту здійснюють понад 10"


async def fetch_data_by_aiohttp(url: str):
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def fetch_data_by_requests(url: str):
    session = AsyncHTMLSession()
    response = await session.get(url)
    return response.html


async def get_data_bs4(url: str = URL, text: str = TEXT):
    html = await fetch_data_by_aiohttp(url)
    soup = BeautifulSoup(html, "lxml")
    data = soup.find(string=re.compile(text))
    if data:
        return data.find_previous("p").get_text()

async def get_data_xpath(url: str = URL, text: str = TEXT):
    html = await fetch_data_by_requests(url)
    data = html.xpath(f'//p[contains(text(), "{text}")]//text()')
    return "".join(data)


if __name__ == "__main__":
    text_bs4 = asyncio.run(get_data_bs4())
    text_html = asyncio.run(get_data_xpath())
    print(f"{text_bs4 = }")
    print(f"{text_html = }")
