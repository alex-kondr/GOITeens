# Створіть програму, яка приймає список товарів та повертає список,
# в якому кожен елемент дорівнює кількості букв, з яких складається товар.
products = ["Хліб", "Кава", "Печиво", "Сіль", "Цукор"]
[4, 4, 6, 4, 5]

# counts = []
# for product in products:
#     count = 0
#     for char in product:
#         count += 1

#     counts.append(count)
#     # counts += [count]

# print(counts)


# counts = []
# for product in products:
#     counts.append(len(product))

# print(counts)

# counts = [len(product) for product in products]
# print(counts)


# Написати програму, що перевірить чи є щось в списку,
# і якщо є, то виведе кількість елементів у ньому.
# products = ["Хліб", "Кава", "Печиво", "Сіль", "Цукор"]
# products = []

# print(f"Кількість елементів {len(products)}")
# if products:
#     print(f"Кількість елементів {len(products)}")
# else:
#     print("Список пустий")

# products = input("Введіть список товарів через кому:\n").lower().strip()
# print(products)
# products = products.split(".")[0].split(",")
# print(products)


# Написати програму, яка видалить зі списку 1-й, 3-й і 6-й елементи
# numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers.pop(5)
# numbers.pop(2)
# numbers.pop(0)
# print(numbers)


# numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers.pop(0)
# print(numbers)
# numbers.pop(1)
# print(numbers)
# numbers.pop(3)
# print(numbers)




# numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers.pop(0)
# numbers.pop(2)
# numbers.pop(5)
# print(numbers)


# Піднести кожен із елементів списку до четвертого степеня
# numbers = list(range(1, 11))
# print(numbers)


# numbers = list(range(1, 11))
# for num in numbers :
#     num = num **4
#     print(num)


numbers = list(range(1, 11))
# for number in numbers:
#     numbers = number ** 4
#     print(numbers)

numbers_4 = [number ** 4 for number in numbers]
print(numbers_4)