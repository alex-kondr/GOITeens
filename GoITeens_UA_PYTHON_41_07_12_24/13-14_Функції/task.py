# my_string = input("Введіть речення: ")

# count = 0
# most_common_char = ""
# for char in my_string:
#     temp_count = my_string.count(char)
#     if count < temp_count:
#         count = temp_count
#         most_common_char = char
# string = "hello"
# string.replace()
# string.isdigit()

# def my_func(s: str):
#     s.replace("", "")
#     s.isdigit()

# my_func(45)

# LOGIN = "my_name"


# def hello():
#     print("Hello!")


# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()

# def say_hello(name):
#     print(f"Hello, {name}!")


# name = input("What is you name? ")
# say_hello(name)

# def plus(a: int, b: int):
#     print(a ** b)


# plus(5, 10)
# plus("Hello", "world")

# reserve = []

# def reserve_vet_clinic(name, count=1):
#     reserve.append([name, count])

# print(f"{reserve = }")
# reserve_vet_clinic("Alex")
# print(f"{reserve = }")
# reserve_vet_clinic("Tomy", 4)
# print(f"{reserve = }")

# def plus(a, b, c, d, e):
#     print(f"{a = }")
#     print(f"{b = }")
#     print(f"{c = }")
#     print(f"{d = }")
#     print(f"{e = }")
#     print(a + b + c + d + e)


# plus(c=1, e=2, d=3, b=4, a=5)


# Написати функцію, яка бронює столик у ресторані. В якості аргументів
# функції використати прізвище клієнта та кількість.
# Для другого параметру передбачити значення за замовчуванням — 2.

# Забронювати два столики (двічі викликати функцію), для 2 і 4 осіб.

# def sum(a, b):
#     return a + b

# # print(sum(1, 5))
# c = sum(1, 5)
# print(c)

# char = "A"
# print(f"Start - {char = }")
# char = "B"

# def my_func(char):
#     print(f"1. {char = }")
#     char = "B"
#     print(f"2. {char = }")


# my_func(char="K")
# print(f"End - {char = }")

# *args
# def my_sum(*args):
#     print(args)
#     return sum(args)


# print(my_sum(1, 2, 5, 20, 50), 2, "hello")






# **kwargs
# def my_func(**kwargs):
#     print(kwargs)

# my_func(a=1, b=5, c=0)


# def my_func(a, b, *args, c=0, d=50, **kwargs):
#     print(f"{a = }, {b = }, {args = }, {c = }, {d = }, {kwargs = }")


# my_func(20, 30, 3, 4, 5, 6, e=90, f=80, d=47)

# char = "A"
# char = "B"
# print(char)



# LEGB

# char = "A"

# def my_func_out():
#     char = "B"

#     def my_func_inner():
#         nonlocal char
#         print(f"{char = }")
#         char = "C"
#         print(f"{char = }")

#     my_func_inner()




# my_func_out()
# print(f"{char = }")

# subscribers_list_news = list()
# subscribers_list_what_new = list()
# subscribers_list_ads = list()

# def subscribe(email, is_news = True, is_new = True, is_ads = True):
#     global subscribers_list_news, subscribers_list_what_new, subscribers_list_ads
#     if is_news:
#         subscribers_list_news.append(email)
#     if is_new:
#         subscribers_list_what_new.append(email)
#     if is_ads:
#         subscribers_list_ads.append(email)

# def print_subscribers(subscribers_list, list_name) :
#     delimiter = '---------------------------'
#     print('На розсилку {} підписалися {} користувачі'.format(list_name, len(subscribers_list)))
#     for user in subscribers_list:
#         print(user)
#         print(delimiter)
#         print()

# subscribe('ivanov@gmail.com')
# subscribe('petrov@gmail.com', True, False, False)
# subscribe('ivanova1@gmail.com', is_ads = False)

# print_subscribers(subscribers_list_news, '"Новини"')
# print_subscribers(subscribers_list_what_new, '"Що нового ?"')
# print_subscribers(subscribers_list_ads, '"Рекламні пропозиції"')














# Написати функцію, яка приймає рядок і повертає кількість голосних букв у цьому рядку.
def count_letter(s: str):
    letters = ["а", "о", "и", "і", "у", "е"]
    return sum([1 for char in s if char in letters])
    # count = 0
    # for char in s:
    #     if char in letters:
    #         count += 1

    # return count


my_string = input("Введіть речення: ")
count = count_letter(my_string)
print(count)







# Написати функцію, яка приймає два числа та повертає їх суму.





# Написати функцію, яка приймає список чисел і повертає найбільше число в цьому списку.





# Написати функцію, яка приймає список і повертає список, який містить тільки унікальні елементи вихідного списку.





# Написати функцію, яка приймає список чисел та повертає суму квадратів цих чисел.






# Написати функцію, яка приймає список і повертає список, який складається з елементів вхідного списку у зворотному порядку.






# Написати функцію, яка приймає список і повертає кількість елементів у цьому списку, що більші за середнє значення списку.





# Написати функцію, яка приймає список рядків і повертає новий список, який містить тільки ті рядки, що містять певний підрядок.





# Написати функцію, яка приймає рядок та повертає його обернений в зворотному порядку.





# Написати функцію, яка приймає список рядків та повертає новий список, який містить тільки ті рядки, що складаються тільки з літер або цифр.





# Написати функцію, яка приймає дві матриці та повертає їх суму.





# Написати функцію, яка приймає список чисел та повертає медіану цього списку.





# Написати функцію, яка приймає рядок та повертає True, якщо цей рядок є паліндромом, та False у протилежному випадку.






# Написати функцію, яка приймає число та повертає його факторіал.







# Написати функцію, яка приймає рядок та повертає True, якщо цей рядок є анаграмою іншого рядку, та False у протилежному випадку.






# Написати функцію, яка приймає словник та повертає список ключів, які відповідають максимальному значенню в словнику