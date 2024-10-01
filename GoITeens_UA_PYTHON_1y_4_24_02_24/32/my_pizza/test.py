import requests


respponse = requests.put("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")
print(respponse.json())
usd = [cours for cours in respponse.json() if cours.get("ccy") == "USD"][0]
print(usd.get("buy"))