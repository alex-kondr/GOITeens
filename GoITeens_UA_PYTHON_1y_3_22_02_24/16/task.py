# def print_message(name, last_name):
#     print(f"Привіт {name}, {last_name}")

# print_message("Дмитро!!!!!!!!", "Абабагаламага")

# def print_message(name, last_name="Kondr"):
#     print(f"Привіт {name}, {last_name}")

# print_message(None, "Абабагаламага")
# print_message(True, "Абабагаламага")
# print_message(None, "Абабагаламага")
# print_message(last_name="Абабагаламага")

# def draw_box(x=10, y=14):
#     print("*" * x)

#     for i in range(y-2):
#         print("*" + " " * (x - 2) + "*")

#     print("*" * x)

# draw_box(50)



# Написати функцію, яка бронює столик у ресторані. В якості аргументів
# функції використати прізвище клієнта та кількість. Для другого параметру передбачити значення за замовчуванням — 2.
# Забронювати два столики (двічі викликати функцію), для 2 і 4 осіб.

# my_dict = {}
# def reserve(last_name, count=2):
#     my_dict.update({
#         last_name: count
#     })

# reserve("Kondr")
# reserve("Абабагаламага", 4)
# print(my_dict)



# def my_func(a, b=5):
#     print(f"{a = }, {b = }")
#     return a + b

# b = 123
# a = 6
# result = my_func(b=a, a=b)
# print(result)

# def summ(*args):
#     print(args)
#     for i in args:
#         print(f"{i = }")

# string = "Hello word"
# summ(*string)


# def my_func(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(f"{k = }, {v = }")

# my_dict = {'a': 5, 'b': 10, 'ababagalamaga': 456}
# # my_func(a=5, b=10, ababagalamaga=456)
# my_func(**my_dict)


# def my_func(a, b, *args, c=5, d=8, e=9, **kwargs):
#     print(f"{a = }, {b = }, {args = }, {c = }, {d = }, {e = }, {kwargs = }")

# my_func(1, 5, 6, 8, 6, k=10, l=11, c=13)

# a = 41

# def my_func():
#     print(f"До {a = }")
#     a = 45
#     print(f"Після {a = }")

#     def my_func2():
#         print(a)
#     # global a

# print(f"До функції {a = }")
# my_func()
# print(f"Після функції {a = }")


# subscribers_list_news = list()
# subscribers_list_what_new = list()
# subscribers_list_ads = list()

# def subscribe(email, is_news = True, is_new = True, is_ads = True):
#     global subscribers_list_news, subscribers_list_what_new, subscribers_list_ads
#     if(is_news):
        # subscribers_list_news.append(email)
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

# # subscribe('ivanov@gmail.com')
# subscribe('petrov@gmail.com', True, False, False)
# # subscribe('ivanova@gmail.com', is_ads = False)

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