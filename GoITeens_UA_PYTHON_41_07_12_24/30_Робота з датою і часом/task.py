import random
# import string

# print(string.punctuation)
# chars = "abcdf451*&"
# len_ = 50
# password = random.choices(chars, k=len_)
# print("".join(password))
my_list = [5, 2, 7, "u", "jjj"]

random.shuffle(my_list)
print(my_list)
# print(random.choice(my_list))








#  len()
# my_list = [5, 2, "f", False]
# my_string = "Hello world!"
# print(len(my_string))

# if len(my_list) == 2:
#     pass



# max(), min()
# my_list = [5, 0, -80, 9, 100]
# # print(max(my_list, key=abs))
# print(min(my_list, key=abs))





# abs()
# print(abs(-50))




# sum()
# my_list = [5, 0, -80, 9, 100]
# print(sum(my_list, start=-9))



# datetime, strftime, fromtimestamp, locale
# https://acode.com.ua/method-strftime-python/
# from datetime import date, time, datetime, timedelta
# import locale

# from datetime import date, time, datetime, timedelta
# import locale

# locale.setlocale(locale.LC_ALL, "uk-uk")

# my_date_2 = datetime(2000, 6, 2, 10, 0, 54)

# print(my_date_2.strftime("На дворі %Y рік місяць %B день %d %A"))








# my_date = date(month=5, day=25, year=2000)
# print(f"{my_date=}")
# my_time = time(hour=5, minute=24)
# print(f"{my_time=}")

# my_datetime = my_date + my_time
# print(f"{my_datetime}")
# my_date_1 = datetime(2024, 1, 6)
# print(f"{my_date_1}")
# print(f"{my_date_2}")
# # print(my_date_1 + my_date_2)
# # delta = timedelta(minutes=5)
# delta = timedelta(hours=5000)
# print(my_date_1 - delta)



# import os
# import sys

# # print(os.path.exists("test.py"))
# print(sys.argv)



# import time

# start_time = time.time()
# time.sleep(5)
# end_time = time.time()
# print(round(end_time - start_time, ndigits=5))




# time
# import time

# print(time.gmtime())
# print(time.localtime())


# Розробіть скрипт, який запитує у користувача
# дві дати (у форматі рррр-мм-дд) і
# обчислює різницю між ними в днях.







# math, sqrt, log, ceil, floor, sin, asin, degrees






# os, sys, random
# import os
# os.chdir("C:\\Users\\user\\Documents")
# print(os.getcwd())
# print(os.listdir())









# Створіть програму, яка використовує функції len(), max(), min(), і abs()
# для обчислення різних статистичних характеристик списку чисел, введених
# користувачем. Наприклад, програма має знаходити максимальне,
# мінімальне значення, довжину списку та обчислювати модуль різниці
# між максимальним і мінімальним значеннями.






# Використовуючи модуль datetime, розробіть скрипт,
# який дозволяє користувачу вводити важливі дати (наприклад, дні народження)
# та зберігає їх у форматі datetime. Програма повинна вміти показувати скільки
# днів залишилось до кожної з дат.





# Використовуючи модуль time, створіть скрипт, що перетворює
# час з однієї часової зони в іншу, користувач вводить час та вказує
# з якої та в яку часову зону потрібно перевести час.






# Розробіть програму, що використовує функції модуля math,
# такі як sqrt(), log(), ceil(), floor(), а також тригонометричні
# функції для вирішення складних математичних завдань,
# які користувач може задавати у формі рівнянь.


