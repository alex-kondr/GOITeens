# empty_list = list()
# empty_list_2 = []b
# print(f"{empty_list = }")
# print(type(empty_list))
# print(f"{empty_list_2 = }")
# print(type(empty_list_2))

# string = "Створіть програму"
# my_list = list(string)
# print(my_list)

# my_list = [1, 2, 5.9, 9, "string", True, False, None]
# first_el = my_list[7]
# print(first_el)
# print(type(first_el))


# L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
# element = L[2][2][2]
# print(element)
# print(type(element))





# Створіть програму, яка приймає список товарів та повертає список,
# в якому кожен елемент дорівнює кількості букв, з яких складається товар.
# products = ["банан", "яблоко", "хліб", "сир"]
# count_char = [len(product) for product in products]

# for product in products:
#     count = 0
#     for char in product:
#         count += 1
#     count_char.append(count)


# for product in products:
#     count_char.append(len(product))

# print(count_char)

# бить или не бить? што делать?



# Написати програму, що перевірить чи є щось в списку, і якщо є, то виведе кількість елементів у ньому.
# my_list = ["Хліб", "Масло"]
# my_list_2 = my_list.copy()
# my_list_2.append("Сир")
# print(f"{my_list_2 = }")
# print(f"{my_list = }")

# if my_list:
#     count_char = len(my_list)
#     print(count_char)
# else:
#     print("Список товарів путий")









# Написати програму, яка видалить зі списку 1-й, 3-й і 6-й елементи
# my_list = [1, 2, 3, 4, 5, 6]

# del my_list[-1]
# print(my_list)

# del my_list[2]
# print(my_list)

# del my_list[0]
# print(my_list)

















# Піднести кожен із елементів списку до четвертого степеня
# my_list = [1, 2, 3, 4, 5, 6]
# for number in my_list:
#     print(number ** 4)








# Видалити слово "Банани" зі списку.
# products = ["Хліб", "Банани", "Риба", "Банани", "Насіння", "Майонез", "Кетчуп", "Банани", "Соус"]
# product = "Банани"

# while product in products:
#     products.remove(product)

# print(products)
































# Написати програму, що прибере дублікати зі списку.
# products = ["Хліб", "Банани", "Риба", "Банани", "Насіння", "Майонез", "Кетчуп", "Банани", "Соус", "Кетчуп"]
# unique_products = []

# for product in products:
#     input(f"Беремо товар: {product}")
#     if product not in unique_products:
#         unique_products.append(product)
#         input(f"Товар '{product}' додано до нового списку")
#         



# Дано дійсне число - ціна 3 кг сала. Вивести вартість 1.2, 1.4, ..., 2 кг сала.
# price = 450
# a = 3

# price1 = price / a 
# print(price1 * 1.2)
# print(price1 * 1.4)

# b = 1.2
# for _ in range(5):
#     print(f"Ціна {round(b, 1)} кілограм сала дорівнює {round(price / a * b, 2)}")
#     b += 0.2

# while b <= 2:
#     print(f"Ціна {round(b, 1)} кілограм сала дорівнює {round(price / a * b, 2)}")
#     b += 0.2






# Написати програму, що порахує кількість додатніх елементів у списку та кількість від’ємних
# list_numbers = [1, 5, -8, 9, -1, 10.5, -25.3]
# positive_number = 0
# negative_number = 0
# for i in list_numbers:
#     if i > 0:
#         positive_number += 1
#     else:
#         negative_number += 1
# print(f"Кількість додатніх чисел {positive_number} і кількість негативних чисел {negative_number}")

# positive_nambers = [number for number in list_numbers if number > 0]
# negative_numbers = [number for number in list_numbers if number < 0]
# print(f"Список додатніх чисел {positive_nambers}, їх кількість дорівнює {len(positive_nambers)}.\nСписок від'ємних чисел {negative_numbers}, їх кількість дорівнює {len(negative_numbers)}")









# products = ["Хліб", "Банани", "Риба", "Банани", "Насіння", "Майонез", "Кетчуп", "Банани", "Соус", "Кетчуп"]
# products_2 = [product for product in products if product == "Банани"]
# print(products_2)






# Дано діапазон чисел від -100 до 0. Вивести на екран лише числа, які закінчуються на нуль
# for number in range(-100, 1):
#     # if str(number).endswith("0"):
#     if number % 10 == 0:
#         print(number)

# numbers_ends_zero = [number for number in range(-100, 1) if number % 10 == 0]
# print(numbers_ends_zero)





# Написати програму, що порахує кількість унікальних елементів у списку.
# products = ["Хліб", "Банани", "Риба", "Банани", "Насіння", "Майонез", "Кетчуп", "Банани", "Соус", "Кетчуп"]
# products_new = []









# Написати програму, яка зчитає 3 числа (a, b, c) та порахує скільки чисел лежить між “a” i “b”, які діляться на “с”
# a = int(input("Введіть початок діапаону: "))
# b = int(input("Введіть кінець діапазону: "))
# c = int(input("Введіть число на яке потрібно ділити: "))







# Написати програму, що виведе список, після видалення із нього парних елементів












# Створіть програму, яка приймає список чисел та виводить на екран кожне третє число у списку.











# Написати програму, що виведе список, після видалення із нього чисел, які закінчуються на нуль







# Створити програму, яка приймає список слів та повертає список слів у зворотньому порядку.






# Створити програму, яка приймає список чисел та повертає список елементів, які є менші за середнє значення списку.







# Написати програму, яка знайде список слів, які мають 5 і більше символів







# З'єднати два списки







# До одного списку додати інший у зворотньому напрямку