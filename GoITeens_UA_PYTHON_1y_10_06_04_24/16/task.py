# def say_hello(name, age):
#     print(f"Hello my friend {name}!")
#     print(f"Your age: {age}")

# say_hello(45, "Dima")
# say_hello("Alex", 13)
# say_hello("Ivan", 21)


# def say_hello(name="Dima", age=20):
#     print(f"Hello my friend {name}!")
#     print(f"Your age: {age}")


# say_hello("Alex")


# def say_hello(name="Dima", age=20):
#     print(f"Hello my friend {name}!")
#     print(f"Your age: {age}")


# say_hello(age=13, name="Alex")


# def say_hello(name, age=20):
#     print(f"Hello my friend {name}!")
#     print(f"Your age: {age}")


# say_hello(13, "Alex")


# def calc(a, b, action="+"):
#     result = 0

#     if action == "+":
#         result = a + b
#     elif action == "-":
#         result = a - b
#     elif action == "*":
#         result = a * b
#     elif action == "/":
#         result = a / b

#     return result


# result1 = calc(-78, 9, "*")
# print(result1)
# result2 = calc(40, 9, "-")
# result3 = calc(-1.2, 1.6, "*")
# result4 = calc(48, -9)

# print(result1 + result2 + result3 + result4)


# bus = {}

# def reserve_bus(name, count=3):
#     # bus.update({name: count})
#     bus[name] = count


# reserve_bus("Alex")
# print(bus)

# reserve_bus("Dima", 5)
# print(bus)

# reserve_bus("Alex", 1)
# print(bus)

# import datetime

# a = 45
# input(f"До функції: {a = }")


# def plus(a, b=5):
#     global c
#     input(f"У функції: {a = }")
#     def plus_2(b=10):
#         nonlocal a
#         a = a + b
#         return a
#     input(f"Після операції: {a = }")
#     return plus_2()

# input(f"Після функції: {a = }")

# c = plus(a=1)

# input(f"a в кінці: {a = }")





# def draw_box(x=10, y=2):
#     print("*" * x)

#     for i in range(y-2):
#         print("*" + " " * (x - 2) + "*")

#     print("*" * x)

# draw_box(50)



# Написати функцію, яка бронює столик у ресторані. В якості аргументів
# функції використати прізвище клієнта та кількість. Для другого параметру передбачити значення за замовчуванням — 2.
# Забронювати два столики (двічі викликати функцію), для 2 і 4 осіб.








# *args

# def plus(a, b, c, d, f):
#     return a + b + c + d + f

# def plus(*args):
#     print(f"{args = }")
#     return sum(args)

# numbers = list(range(1, 51))
# print(numbers)

# print(plus())


# **kwargs

# def plus(a=4, b=5, c=6):
#     print(a, b, c)
#     return a + b + c

# my_dict = {'b': 1, 'a': 5, 'c': 9}
# print(plus())
# from datetime import datetime
# def plus(**kwargs):
#     print(f"{kwargs = }")
#     return sum(kwargs.values())

# my_dict = {'a': 1, 'b': 5, 'c': 9}
# print(plus(**my_dict)) # (a=1, b=5, c=9)


# def plus(*args, **kwargs):
#     # print(f"{a = }")
#     # print(f"{b = }")
#     print(f"{args = }")
#     # print(f"{c = }")
#     # print(f"{d = }")
#     print(f"{kwargs = }")

#     return sum([*args, *kwargs.values()])

# print(plus(4, 8, 9, 1, -8, g=9, d=-5, o=78))



subscribers_list_news = list()
subscribers_list_what_new = list()
subscribers_list_ads = list()

def subscribe(email, is_news = True, is_new = True, is_ads = True):
    global subscribers_list_news, subscribers_list_what_new, subscribers_list_ads
    if is_news:
        subscribers_list_news.append(email)
    if is_new:
        subscribers_list_what_new.append(email)
    if is_ads:
        subscribers_list_ads.append(email)

def print_subscribers(subscribers_list, list_name) :
    delimiter = '---------------------------'
    print('На розсилку {} підписалися {} користувачі'.format(list_name, len(subscribers_list)))
    for user in subscribers_list:
        print(user)
        print(delimiter)
        print()

subscribe('ivanov@gmail.com')
subscribe('petrov@gmail.com', True, False, False)
subscribe('ivanova1@gmail.com', is_ads = False)

print_subscribers(subscribers_list_news, '"Новини"')
print_subscribers(subscribers_list_what_new, '"Що нового ?"')
print_subscribers(subscribers_list_ads, '"Рекламні пропозиції"')














# Написати функцію, яка приймає рядок і повертає кількість голосних букв у цьому рядку.




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