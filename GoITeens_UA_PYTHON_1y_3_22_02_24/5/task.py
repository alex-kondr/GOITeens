# Створіть програму, яка приймає список товарів та повертає список,
# в якому кожен елемент дорівнює кількості букв, з яких складається товар.

# Створення пустого списку продуктів
# products = []

# while True:
#     # Даємо можливість користувачу ввести назву товару
#     product = input("Введіть товар для покупки, або введіть 'stop' > ")

#     # Якщо користувач ввів "stop" тоді зупиняємо програму
#     if product == "stop":
#         break

#     # Додаємо новий товар
#     products.append(product)

# print(products)    # Виводимо на екран наш список

# # Створюємо пустий список з кількість букв
# chars_count = []

# for i, product in enumerate(products):
#     char_count = len(product)    # Рахує кількість букв в слові
#     chars_count.append(char_count)    # Додаємо кількість до списку chars_count

#     # Виводимо на екран список продуктів та кількість букв
#     print(f"{i + 1}. Товар {product} має таку кількість букв: {char_count}")











# Написати програму, що рахує добуток всіх чисел у списку.
# numbers = [1, 5, -9, -7.1]

# result = 1

# for number in numbers:
#     result *= number

# print(f"Добуток числе дорівнює {result}")







# Написати програму, яка виведе числа від 7 до 77 використовуючи цикл
# start = int(input())
# end = int(input())

# for i in range(7, 78, 78):
#     print(i)


#############################
# другий метод рахунку!!!!!!!!!!!!!!!!!


# my_list = "Python"
# print(my_list)
# print(len(my_list))
# print(my_list[:4])
# print(my_list[1:])
# print(my_list[1:4])
# print(my_list[1:4:])





# На технічній співбесіді претенденти на посаду одержують оцінку за тест.
# У наступний тур співбесіди проходять кандидати, які склали тест на 83 бали включно або вище.
# Реалізуйте оператор контролю виконання так, щоб він привласнив логічній змінній is_next значення True,
# якщо кількість набраних балів буде більшою або дорівнює 83.
# В іншому випадку значення змінної дорівнює False.
# score = 90
# is_next = True if score >= 83 else False
# print(is_next)




# Написати програму, що перевірить чи є щось в списку, і якщо є, то виведе кількість елементів у ньому.
# stop_list = ["stop", "cancel", "exit", "0", "1"]
# stop_world = "stop1"

# is_exist = f"Слово '{stop_world}' входить у список стоп-слів" if stop_world in stop_list else f"Слово '{stop_world}' не входить у список стоп-слів"
# print(is_exist)





# Дано змінну a = -56. Виводити a, поки a <= 15, збільшуючи змінну на 3
# a = -56
# while a <= 15:
#     print(a)
#     a += 3





# Написати програму, яка видалить зі списку 1-й, 3-й і 6-й елементи зі списку
# lst=["Alex", "Petro", "Max", "Andrii", "Lev", "Dmutro", "Lev", "Lev"]
# index_lev = lst.index("Lev")
# lst.pop(index_lev)
# print(index_lev)
# print(lst)
# lst.pop(2)
# print(lst)
# lst.pop(0)
# print(lst)





# Написати програму, яка на початку додасть “I am glad to see you, ” до кожного із імен в списку
# і виведе привітання на екран.
# lst=["Alex", "Petro", "Max", "Andrii", "Lev"]. Приклад — I am glad to see you, Alex!






# Написати програму, що дістає мінімальне число зі списку.







# Запитувати у користувача речення та літеру для пошуку.
# Порахувати скільки даних літер у речені






# Піднести кожен із елементів списку до четвертого степеня






# Видалити слово "Банани" зі списку.
# products = ["Хліб", "Банани", "Риба", "Банани", "Насіння", "Майонез", "Кетчуп", "Банани", "Соус"]
# world = "Банани"

# while world in products:
#     products.remove(world)

# print(products)







# Написати програму, яка порахує і виведе числа у квадраті від 1 до числа, яке задасть користувач







# Написати програму, що прибере дублікати зі списку.






# Дано дійсне число - ціна 3 кг сала. Вивести вартість 1.2, 1.4, ..., 2 кг сала.







# Написати програму, що порахує кількість додатніх елементів у списку та кількість від’ємних
# numbers = []






# Дано діапазон чисел від -100 до 0. Вивести на екран лише числа, які закінчуються на нуль





# Написати програму, що порахує кількість унікальних елементів у списку.









# Написати програму, яка зчитає 3 числа (a, b, c) та порахує скільки чисел лежить між “a” i “b”, які діляться на “с”








# Написати програму, що виведе список, після видалення із нього парних елементів







# Створіть програму, яка приймає список чисел та виводить на екран кожне третє число у списку.











# Написати програму, що виведе список, після видалення із нього чисел, які закінчуються на нуль









# Створити програму, яка приймає список слів та повертає список слів у зворотньому порядку.






# Створити програму, яка приймає список чисел та повертає список елементів, які є менші за середнє значення списку.







# Написати програму, яка знайде список слів, які мають 5 і більше символів







# З'єднати два списки







# До одного списку додати інший у зворотньому напрямку