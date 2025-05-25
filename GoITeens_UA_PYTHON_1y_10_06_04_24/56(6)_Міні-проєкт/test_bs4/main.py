import asyncio
import re

from aiohttp import ClientSession
from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup


URL = "https://uk.wikipedia.org/wiki/%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%B8%D0%B9_%D0%B0%D0%B4%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D0%B9_%D0%BA%D0%BE%D0%BB%D0%B0%D0%B9%D0%B4%D0%B5%D1%80"
SEARCH_TEXT = "Перших зіткнень вдалось досягти"

async def fetch_html_aiohtt(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def fetch_html_requests(url):
    session = AsyncHTMLSession()
    response = await session.get(url)
    return response.html


async def get_data_aiohttp_bs4(url, text):
    html = await fetch_html_aiohtt(url)
    soup = BeautifulSoup(html, "lxml")
    data = soup.find(string=re.compile(text)).find_previous("p")
    print(data.get_text())


async def get_data_requests_html(url, text):
    html = await fetch_html_requests(url)
    data = html.xpath(f"//p[contains(., '{text}')]//text()")
    data = " ".join(data)
    print(data)


if __name__ == "__main__":
    # asyncio.run(get_data_aiohttp_bs4(URL, SEARCH_TEXT))
    asyncio.run(get_data_requests_html(URL, SEARCH_TEXT))

