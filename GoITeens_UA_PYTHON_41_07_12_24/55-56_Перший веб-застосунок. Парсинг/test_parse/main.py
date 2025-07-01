from requests_html import HTMLSession
from bs4 import BeautifulSoup


session = HTMLSession()
url = "https://cyberpunk.fandom.com/ru/wiki/Samurai#%D0%93%D0%B0%D0%BB%D0%B5%D1%80%D0%B5%D1%8F"
response = session.get(url)

html = response.html

# title = html.xpath('//span[@class="mw-page-title-main"]/text()')
# if title:
#     print(title[0])


# text_list = html.xpath('//div[contains(@class, "mw-content-ltr")]/p//text()')
# print(" ".join(text_list))

soup = BeautifulSoup(response.content, "lxml")
div = soup.find("div", class_="mw-content-ltr").find_all_next("p")
for el in div:
    print(el.get_text())