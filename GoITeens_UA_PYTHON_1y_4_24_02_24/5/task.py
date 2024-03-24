# Створіть програму, яка приймає список товарів та повертає список,
# в якому кожен елемент дорівнює кількості букв, з яких складається товар.
# products = []
# count_char = []

# while True:
#     product = input("Введіть товар для додавання у список товарів або введіть 'stop': ")

#     if product == "stop":
#         break

#     products.append(product)

#     count = 0

    # for char in product:
    #     count += 1

    # count_char.append(len(product))

# for i, product in enumerate(products):
#     print(f"{i + 1}. Товар '{product}' має таку кількість символів: {count_char[i]}")

# while True:
#     product = input("Введіть товар для видалення або введіть 'stop': ")

#     if product == "stop":
#         break

#     if product in products:
#         products.remove(product)
#     else:
#         print("Такого товару немає у списку\n")

# for i, product in enumerate(products):
#             print(f"{i + 1}. Товар '{product}' має таку кількість символів: {count_char[i]}")









# Написати програму, що перевірить чи є щось в списку, і якщо є, то виведе кількість елементів у ньому.
# my_list = ["Хліб", "Масло"]

# if my_list:
#     print(f"Список my_list не пустий")
#     print(len(my_list))









# Написати програму, яка видалить зі списку 1-й, 3-й і 6-й елементи
# my_list = [1, 2, 3, 4, 5, 6]

# my_list.pop(5)
# print(my_list)

# my_list.pop(2)
# print(my_list)

# my_list.pop(0)
# print(my_list)


















# Піднести кожен із елементів списку до четвертого степеня
# my_list = [1, 2, 3, 4, 5, 6]
# my_list_2 = []

# for i in my_list:
#     my_list_2.append(i ** 4)

# print(my_list_2)








# Видалити слово "Банани" зі списку.
# products = ["Хліб", "Банани", "Риба", "Банани", "Насіння", "Майонез", "Кетчуп", "Банани", "Соус"]
# product = "Банани"

# while product in products:
#     products.remove("Банани")

# print(products)



# products = ["Хліб", "Банани", "Риба", "Банани", "Насіння", "Майонез", "Кетчуп", "Банани", "Соус"]
# products_2 = products

# print(products[::3])











# Написати програму, що прибере дублікати зі списку.
# products = ["Хліб", "Банани", "Риба", "Банани", "Насіння", "Майонез", "Кетчуп", "Банани", "Соус", "Кетчуп"]
# products_copy = products.copy()
# products_clear = []

# for product in products:
#     while product in products_copy:
#         products_copy.remove(product)

#     if product not in products_clear:
#         products_clear.append(product)

# print(products_clear)






# Дано дійсне число - ціна 3 кг сала. Вивести вартість 1.2, 1.4, ..., 2 кг сала.
# price = 450
# a = 3

# price_one = price / a
# price_list = []

# b = 1.2

# while b <= 2:
#     new_price = round(price_one * b, 0)
#     price_list.append(new_price)
#     b += 0.2

# print(f"{price_list = }")






# Написати програму, що порахує кількість додатніх елементів у списку та кількість від’ємних
# list_numbers = []
# for i in range(-10, 20, 3):
#     list_numbers.append(i**3)

# list_numbers = [i for i in range(-10, 20, 3)]
# count = 0
# pos = [count+1 for i in range(-10, 20, 3) if i > 0]
# print(sum(pos))
# neg = [count+1 for i in list_numbers if i < 0]
# print(sum(neg))
# for i in list_numbers:
#     if i > 0:
#         count_pos += 1
#     elif i < 0:
#         count_neg += 1

# print(f"Кількість додатніх чисел: {count_pos}\nК-ть негативних: {count_neg}")


# products = ["Хліб", "Банани", "Риба", "Банани", "Насіння", "Майонез", "Кетчуп", "Банани", "Соус", "Кетчуп"]
# products_2 = [product for product in products if product == "Банани"]

# products_2 = []
# for product in products:
#     if product == "Банани":
#         products.append(product)


# print(products_2)





# Дано діапазон чисел від -100 до 0. Вивести на екран лише числа, які закінчуються на нуль
# list_numbers = [i for i in range(-100, 1) if i % 10 == 0]
# print(list_numbers)

# for i in range(-100, 1):
#     if i % 10 == 0:
#         print(i)







# Написати програму, що порахує кількість унікальних елементів у списку.
# products = ["Хліб", "Банани", "Риба", "Банани", "Насіння", "Майонез", "Кетчуп", "Банани", "Соус", "Кетчуп"]
# products_new = []

# for product in products:
#     if product not in products_new:
#         products_new.append(product)

# print(len(products_new))





# Написати програму, яка зчитає 3 числа (a, b, c) та порахує скільки чисел лежить між “a” i “b”, які діляться на “с”
# a = int(input("Введіть початок діапаону: "))
# b = int(input("Введіть кінець діапазону: "))
# c = int(input("Введіть число на яке потрібно ділити: "))
# count = sum([1 for i in range(a, b+1) if i % c == 0])

# # count = 0

# # for i in range(a, b + 1):
# #     if i % 4 == 0:
# #         count += 1

# print(f"Кількість чисел, які діляться на {c} в діапазоні від {a} до {b} дорівнює {count}")

# my_list = [2, 8.9, -5, 9.7, 15]
# sum_my_list = sum(my_list)
# print(round(sum_my_list, 9))






# Написати програму, що виведе список, після видалення із нього парних елементів
# list_numbers = []
# for i in range(-1000, 1000):
#     if i % 2:
#         list_numbers.append(i)


# list_numbers = [i for i in range(-1000, 1000) if i % 2]











# Створіть програму, яка приймає список чисел та виводить на екран кожне третє число у списку.
# list_numbers = []

# while True:
#     number = input("Введіть число або 0: ")

#     if number == "0":
#         break

#     if number.isdigit():
#         list_numbers.append(float(number))
#     else:
#         print("Це не число")

# for i in range(0, len(list_numbers), 3):
#     print(list_numbers[i])






# Написати програму, що виведе список, після видалення із нього чисел, які закінчуються на нуль
# list_numbers = [i for i in range(100)]

# list_numbers_new = [i for i in list_numbers if i % 10]
# print(list_numbers_new)






# Створити програму, яка приймає список слів та повертає список слів у зворотньому порядку.






# Створити програму, яка приймає список чисел та повертає список елементів, які є менші за середнє значення списку.







# Написати програму, яка знайде список слів, які мають 5 і більше символів







# З'єднати два списки







# До одного списку додати інший у зворотньому напрямку