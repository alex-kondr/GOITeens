# import random
# import math
# import datetime
# import time

# import matplotlib.pyplot as plt

# import my_module


# print(random.sample([1, 2, 6]))
# print(random.choices([1, 2, 6]))



# from random import sample, choice, choices


# sample([], k=1)



# from random import *
# from my_module_1 import *
# from my_module_2 import *

# shuffle([1, 2], k=1)



# def add(a, b):
#     return a + b



# # import math_
# from math_ import add, subtrac

# # print(math_.add(5, 9))
# # print(math_.subtrac(1, 8))

# summ_1 = add(2, 8)
# print(f"{summ_1 = }")
# summ_2 = add(5, -9)
# print(f"{summ_2 = }")

# print(subtrac(9, 4))


# Matplotlib
# import matplotlib





# Створити модуль, що містить функцію, яка повертає набір даних Х та Y
# Імпортувати цей модуль в основний скрипт і побудувати графік Х від Y,
# використовуючи бібліотеку Matplotlib.



# import matplotlib.pyplot as plt

# import my_data


# plt.plot(my_data.x_coordination(), my_data.y_coordination())
# plt.show()

# import numpy as np

# x = np.linspace(0, 2, 100)

# plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
# plt.plot(x, x**2, label='quadratic')  # etc.
# plt.plot(x, x**3, label='cubic')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("Simple Plot")
# plt.legend()
# plt.show()





# Створити власний модуль my_module.py, який містить функцію print_message(msg),
# що приймає один аргумент msg та виводить його на екран.
# Потім імпортувати функцію print_message() в головний файл програми та викликати її.








# Створити власний модуль my_math.py, який містить функції add(x, y) та subtract(x, y).
# # Імпортувати модуль та використати ці функції для додавання та віднімання чисел.
# import my_math


# if __name__ == "__main__":
#     result_add = my_math.add(41, 5)
#     print(f"{result_add = }")
#     result_sub = my_math.subtract(41, 5)
#     print(f"{result_sub = }")







# Створити власний модуль my_geometry.py, який містить функції circle_area(radius)
# та rectangle_area(width, height).
# Імпортувати модуль та використати ці функції для обчислення площі круга та прямокутника.
import my_geometry


circle_area = my_geometry.circle_area(12)
print(f"{circle_area = }")

rectangle_area = my_geometry.rectangle_area(4, 5)
print(f"{rectangle_area = }")







# Створити власний модуль my_data.py, який містить список даних (наприклад, список чисел).
# Імпортувати модуль та вивести список даних на екран.










# Створити власний модуль my_statistics.py, який містить функції для обчислення
# статистичних показників (наприклад, середнього значення, медіани, дисперсії) для списку даних.
# Імпортувати модуль та використати ці функції для обробки списку даних.
# D(X)= E(X^2) − μ^2









# Створити графік лінійної функції y = 2x + 1 за допомогою бібліотеки matplotlib.







# Створити графік квадратичної функції y = x^2 за допомогою бібліотеки matplotlib.







# Створити гістограму для списку даних за допомогою бібліотеки matplotlib.





# Створити діаграму розділу для списку даних за допомогою бібліотеки matplotlib.








# Створити графік функції sin(x) за допомогою бібліотеки matplotlib.
