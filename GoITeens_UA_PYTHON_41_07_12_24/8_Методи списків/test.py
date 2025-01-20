products = ["Хліб", "Кава", "Цукор", "Юрта", "Африка", "Цукор", "Кава"]

for i, product in enumerate(products, start=1):
    print(f"Товар під номером {i} - {product}")

for i in range(1, len(products)+1):
    print(f"Товар під номером {i} - {products[i-1]}")

# print(products)
# count = len(products)
# print(count)

# products_2 = products.copy()
# products_2.remove("Кава")
# print(f"{products_2 = }")
# print(f"{products = }")





# products.sort(reverse=True)
# products_sort = sorted(products, reverse=True)
# print(products)
# print(products_sort)
# products.reverse()
# products_reverse = products[::-1]
# print(products)
# print(products_reverse)


# index = products.index("Кава", 3, 4)
# print(index)
# count = products.count("Кава")
# print(count)



# products.append("Цибуля")
# print(products)

# product = products.pop(1)
# del products[1]
# product = products.remove("Кава")

# print(f"{ product = }")
# products_2 = ["Печиво", "Кола", "Картопля"]
# products_2.extend(products)
# products = products + products_2
# products += products_2
# products.clear()
# products = []
# print(f"{products = }")
# print(f"{products_2 = }")

