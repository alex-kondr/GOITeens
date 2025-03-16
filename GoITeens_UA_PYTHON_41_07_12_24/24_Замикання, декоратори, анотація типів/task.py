# Розглянемо функцію, яка створює і повертає іншу функцію.
# Внутрішня функція є замиканням, оскільки вона захоплює
# та використовує змінну зі свого лексичного контексту

# def out_func(x):
#     def in_func(y):
#         return x + y
#     return in_func

# sum_5 = out_func(5)
# sum_6 = out_func(6)
# # print(sum_5)
# print(sum_5(60))
# print(sum_6(60))



# Створимо замикання як лічильник

# def counter():
#     count = 0
#     def in_func():
#         nonlocal count
#         # count_1 = 0
#         count += 1
#         return count
#     return in_func

# my_couter = counter()
# print(my_couter())
# my_couter()
# my_couter()
# my_couter()
# my_couter()
# my_couter()
# my_couter()
# my_couter()
# my_couter()
# # print(my_couter())
# # print(my_couter())
# # print(my_couter())
# # print(my_couter())
# print(my_couter())






# Замикання для емуляції приватності
# Функції get_balance та add_funds можуть взаємодіяти з балансом
# balance = 0
# def init_bank(init_balance=0):
#     balance = init_balance
#     def show_balance():
#         # balance = 1
#         return balance
#     def add_balance(new_balace):
#         global balance
#         balance += new_balace
#         return balance
#     return show_balance, add_balance


# show_balance, add_balance = init_bank(100)
# print(show_balance())
# print(add_balance(250))
# print(show_balance())






# Функція для вимірювання часу виконання
# import time

# def timer(msg):
#     def param_decor(func):
#         def wraper(*args, **kwargs):
#             print(msg)
#             start = time.time()
#             result = func(*args, **kwargs)
#             end = time.time()
#             print(f"Час виконання програми {int(end - start)} с")
#             return result
#         return wraper
#     return param_decor


# @timer(msg="Тестую першу функцію")
# def my_func():
#     print("Старт програми...")
#     time.sleep(5)
#     print("Програма завершила свою роботу")


# my_func()





# Декоратор, що логує виклик функції

# def my_decorator(func):
#     def in_func(*args, **kwargs):
#         print(f"Функція отримала такі параметри: {args}, {kwargs}")
#         print(f"Запускаємо таку функцію: {func.__name__}")
#         result = func(*args, **kwargs)
#         print("Функція завершила свою роботу")
#         return result
#     return in_func


# @my_decorator
# def add_numbers(*numbers):
#     return sum(numbers)


# print(add_numbers(1, 5, 6, 8, 10))







# Декоратор для вимірювання часу виконання функції





# Анотації

number: int = 5

number

from typing import Optional, Union, List

def add_numbers(a: int, b: Optional[int] = None) -> int:
    return a + b

def minus(a: Union[int, float]) -> Union[int, float]:
    return a


def print_list(my_list: List[str]) -> List[str]:
    return my_list