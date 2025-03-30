# all

# a = 5
# b = 10
# c = 6

# if a > 2 and b > 1 and c > 0:
# if all((a > 2, b > 1, c > 0)):
#     print("Все ОК")







# Перевірка, чи всі елементи списку позитивні
# Це зручно використовувати для перевірки, чи всі числа в списку
# є позитивними, що може бути корисно у фінансових аналізах або при обробці даних.
# numbers = [1, 2, 3, 4, 5]

# if all(number > 0 for number in numbers):
#     print("Все ОК")
# else:
#     print("Тут є від'ємне число")

# print(all(number > 0 for number in numbers))





# Перевірка, чи всі рядки у списку мають значення
# words = ["apple", "banana", "cherry", ""]

# # words = ["apple", "banana", "cherry", ""]
# # if all(word != "" for word in words):
# if all(words):
#     print("Все ок")
# else:
#     print("Є пусте значення")

# print(all(words))









# any

# Перевірка на наявність позитивних чисел у списку
# numbers = [0, False, "", {}, []]
# print(any(numbers))

# my_bool = bool(numbers)
# print(my_bool)
# for number in numbers:
#     if number > 0:
#         print("OK")
#         break
# else:
#     print("У списку тільки від'ємні числа")

# if numbers[0] > 0 or numbers[1] > 0 or numbers[2] > 0:
# if any(number > 0 for number in numbers):
#     print("OK")
# else:
#     print("У списку тільки від'ємні числа")


# numbers = [1, -5, 8, 9, 6]
# if any(num < 0 for num in numbers):
#     print("Є від'ємні числа")
# else:
#     print("Від'ємних чисел немає")


# Перевірка на наявність слів, що починаються з великої літери








# sorted
# sorted(iterable, key=None, reverse=False)

# Відсортувати список чисел за зростанням

# numbers = [5, -9, 0, 8, 100, -45, 12.3]

# sorted_list = sorted(numbers)
# print(sorted_list)


# words = ["apple", "banana", "cherry", ""]
# my_sorted_words = sorted(words, reverse=True)
# print(my_sorted_words)











# Сортування списку кортежів другим елементом
# tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]

# sorted_tuples = sorted(tuples, key=lambda x: x[1])
# print(sorted_tuples)

students = {"Alex": 45, "Banana": 98, "BonBon": 61, "Oleh": 100}

# sorted_students = sorted(students, key=students.get, reverse=True)
sorted_students = sorted(students)
print(sorted_students)





# сортування в порядку спадання
# words = ["banana", "apple", "cherry"]





# data = [("apple", 2), ("banana", 1), ("cherry", 3)]







# Створіть скрипт, який зчитує список цілих чисел
# (можна використовувати генератор випадкових чисел),
# використовує all() для перевірки, чи всі числа позитивні,
# а потім застосовує sorted() для сортування цих чисел за зростанням.







# Напишіть програму, яка дозволяє користувачеві
# ввести рядок символів та використати any() для
# перевірки, чи містить рядок будь-які голосні букви.
# Виведіть результат перевірки.