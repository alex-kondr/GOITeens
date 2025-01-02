from requests_html import HTMLSession, AsyncHTMLSession
import json
import asyncio
import logging
import sys

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
# log.info("Hi")


# session = HTMLSession()
# response = session.get("https://rozetka.com.ua/ua/mobile-phones/c80003/")


def save_prod(name, description, img_url):
    with open("prods.json", "r" , encoding="utf-8") as file:
        prods = json.load(file)

    prods.append({
        "name": name,
        "description": description,
        "img_url": img_url
    })

    with open("prods.json", "w", encoding="utf-8") as file:
        json.dump(prods, file, ensure_ascii=False, indent=2)
        log.info(f"Saved {name}")


async def get_product(url):
    session = AsyncHTMLSession()
    response = await session.get(url)
    name = response.html.xpath('.//p[contains(@class, "title__font")]/text()')[0]
    description = "\n".join(response.html.xpath('.//div[contains(@class, "ng-star-inserted")]//text()'))
    img_url = response.html.xpath('.//img[@class="image"]/@src')[0]
    log.info(f"Save {name}")
    save_prod(name, description, img_url)


async def get_prods(url):
    session = AsyncHTMLSession()
    response = await session.get(url)
    prods = response.html.xpath('//div[@class="goods-tile__inner"]')
    for i, prod in enumerate(prods, start=1):
        prod_url = prod.xpath('.//a[@class="ng-star-inserted"]/@href')[0]
        log.info(f"Get product № {i}")
        await get_product(prod_url)


async def main():
    await get_prods("https://rozetka.com.ua/ua/mobile-phones/c80003/")



if __name__ == "__main__":
    asyncio.run(main())

# prods = response.html.xpath('//div[@class="goods-tile__inner"]')
# for prod in prods:
#     name = prod.xpath('(.//a[@class="ng-star-inserted"]/@href)[last()]')
#     print(name)
#     input()
# for html in response.html:
#     print(html)

# with open("test.html", "w", encoding="utf-8") as file:
#     file.write(response.html)