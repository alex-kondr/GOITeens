# Піднести кожен із елементів списку до четвертого степеня
#my_list = [1, 2, 3, 4, 5, 6]
#for number in my_list:
#    print(number ** 4)





# Видалити слово "Банани" зі списку.
products = ["Хліб", "Банани", "Риба", "Банани", "Насіння", "Майонез", "Кетчуп", "Банани", "Соус"]
product = "Банани"
while product in products:
    products.remove(product)
print(products)
