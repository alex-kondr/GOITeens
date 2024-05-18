# Видалити слово "Банани" зі списку.
products = ["Хліб", "Банани", "Риба", "Банани", "Насіння", "Майонез", "Кетчуп", "Банани", "Соус"]
product = "Банани"
while product in products:
    products.remove(product)
print(products)