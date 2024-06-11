# def say_hello():
#     print("Hi there!!!!!")

# say_hello()

# def summ(x, y=8):
#     print(x + y)

# # x = int(input("Введіть число 'x': ")) # 5
# # y = int(input("Введіть число 'y': ")) # 9
# summ()

# def draw_box(w=10, h=14):
#     print("*" * w)
#     for _ in range(h - 2):
#         print("*" + (" " * (w - 2)) + "*")

#     print("*" * w)

# draw_box(h=50, w=8)
# print(end="")



# Написати функцію, яка бронює столик у ресторані.
# В якості аргументів функції використати прізвище клієнта та кількість.
# Для другого параметру передбачити значення за замовчуванням — 2.

# Забронювати два столики (двічі викликати функцію), для 2 і 4 осіб.

# reserve = {}

# def reserve_table(last_name, count=2):
#     reserve.update({last_name: count})

# reserve_table("Kondr")
# print(reserve)

# reserve_table("Абабагамалга", 4)

# print(reserve)


# def mul(a, b=1, c=7):
#     return a * b * c

# mulltiple = mul(4, 9, 2)
# print(mulltiple)

# def my_func(a, b, c):
#     return mul(a, b, c) + a + b + c

# result = my_func(4, 9, 2)
# print(result)

# print(my_func(4, 1, 0))


# def my_func(*args):
#     print(args)

#     for arg in args:
#         print(arg)

# my_func(1, 5, 8, -7)
# my_func()

# def my_func(x, *args):
#     print(f"{x = }")
#     print(f"{args = }")

# my_func(4, 8, 9, -9)


# def my_func(x, *args, y=8, **kwargs):
#     print(f"{x = }")
#     print(f"{y = }")
#     print(f"{args = }")
#     print(f"{kwargs = }")

# my_func(4, 1, 3, 9, 0, y=4, a=9, k=0)

# a = 8

# def my_fuc():
#     a = 9
#     print(f"{a = }")

# print(f"Буква 'a' до функції: {a = }")
# my_fuc()
# print(f"Буква 'a' після фінкції: {a = }")


# a = 8

# def my_fuc():
#     global a

#     print(f"До {a = }")
#     a = 9
#     print(f"Після {a = }")

# print(f"Буква 'a' до функції: {a = }")
# my_fuc()
# print(f"Буква 'a' після фінкції: {a = }")









# subscribers_list_news = list()
# subscribers_list_what_new = list()
# subscribers_list_ads = list()

# def subscribe(email, is_news = True, is_new = True, is_ads = True):
#     global subscribers_list_news, subscribers_list_what_new, subscribers_list_ads
#     if(is_news):
#         subscribers_list_news.append(email)
#     if(is_new):
#         subscribers_list_what_new.append(email)
#     if(is_ads):
#         subscribers_list_ads.append(email)

# def print_subscribers(subscribers_list, list_name) :
#     delimiter = '---------------------------'
#     print('На розсилку {} підписалися {} користувачі'.format(list_name, len(list_name)))
#     for user in subscribers_list:
#         print(user)
#         print(delimiter)
#         print()

# subscribe('ivanov@gmail.com')
# subscribe('petrov@gmail.com', True, False, False)
# subscribe('ivanova@gmail.com', is_ads = False)

# print_subscribers(subscribers_list_news, '"Новини"')
# print_subscribers(subscribers_list_what_new, '"Що нового ?"')
# print_subscribers(subscribers_list_ads, '"Рекламні пропозиції"')














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






# Написати функцію, яка приймає словник та повертає список ключів, які відповідають максимальному значенню в словнику.