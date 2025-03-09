# обчислення факторіалу числа n (n!)

# 5! = 5 * 4 * 3 * 2 * 1
# 4! = 4 * 3 * 2 * 1
# 6! = 6 * 5 * 4 * 3 * 2 * 1
# 0! = 1

# def factorial(n):
#     if n < 0:
#         return "Факторіал визначається лише для додатніх чисел!!!"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result

# num = int(input("Введіть число: "))
# print(f"Факторіал числа {num}: {factorial(num)}")
# 6! = 720
# 5! = 5 * (4 * 3 * 2 * 1) = 120
# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(999))













# Необхідно написати рекурсивну функцію для
# обчислення n-го числа Фібоначчі.
# Послідовність Фібоначчі починається з двох
# чисел 0 та 1, а кожне наступне число є сумою двох попередніх чисел.
# 1 2 3 4 5 6 7 8  9  10
# 0 1 1 2 3 5 8 13 21 34

# def fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(40))










# Створимо рекурсивну функцію, яка шукає
# елемент у списку і повертає True, якщо
# елемент знайдений, та False - в іншому випадку.
# numbers = list(range(21))
# number = 20

# # print(number in numbers)

# def is_number_in_list(numbers: list, number: int, count):
#     if not numbers:
#         return 0

#     elif numbers[0] == number:
#         return True

#     return is_number_in_list(numbers[1:], number)

# [1, 2, 3]
# print(is_number_in_list(numbers, number))




# Завдання 1: Сума чисел від 1 до N
# Вам потрібно написати рекурсивну функцію, яка обчислює суму
# усіх натуральних чисел від 1 до N,
# де N - це невід'ємне ціле число, передане як аргумент функції.


def sum_of_numbers(N):
    if N == 0:
        return 0
    else:
        return N + sum_of_numbers(N - 1)

print(sum_of_numbers(5))












# Завдання 2: Перевернути рядок
# Створіть рекурсивну функцію, що приймає рядок як
# аргумент та повертає цей рядок у зворотньому порядку.
# Спробуйте не використовувати зрізи рядків або цикли.












# Завдання 3: Підрахунок кількості "x" у рядку
# Напишіть рекурсивну функцію, яка підраховує,
# скільки разів символ "x" зустрічається у даному рядку.
# Функція повинна бути чутливою до регістру.
