# fh = open("hello", "r", encoding="utf-8")
# pass
# pass
# fh.close()
# fh = open("hello", "r+")
# fh = open("hello", "w")
# fh = open("hello", "w+")
# fh = open("hello", "a")
# fh = open("hello", "a+")


# print(fh.read())
# fh.write("Bye! World!")
# print(fh.read())
# fh.close()


# fh = open("hello1.txt", "w", encoding="utf-8")
# fh.write("Bye my World!")
# fh.close()

# fh = open("hello.txt")
# file = fh.read()
# fh.close()

# print(file)

# fh = open("hello.txt", "a+", encoding="utf-8")
# file = fh.read()
# print(file)
# fh.writelines(["Другий рядок\n", "Третій рядок\n", "Четвертий рядок\n"])
# fh.close()

# import os


# os.remove("hello1.txt")


# with open("hello.txt", "w", encoding="utf-8") as fh:
#     fh.write("Hello")
#     fh.writelines(["Hello"])

# with open("hello.txt", "r", encoding="utf-8") as fh:
#     # print(fh.read())
#     # print(fh.read(3))
#     # print(fh.readline())
#     # print(fh.readlines())
#     fh.seek(3)
#     fh.read()
# with open("file.txt", "r", encoding="utf-8") as fh:
#     for line in fh.readlines():
#         pass

products = []
with open("dir/file.txt", "a", encoding="utf-8") as fh:
    fh.writelines(products)
    for product in products:
        fh.write(product + "\n")


# with open("file.bin", "rb") as fh:
#     pass

# with open("file.bin", "wb") as fh:
#     pass

# def my_func(1, 2, 3) -> str:
#     pass

# def my_func(1, 2, 3) -> str:
#    return


# Напишіть програму, яка зчитує вміст файлу "input.txt"
# і записує його у файл "output.txt" з виключенням повторюваних рядків.

# with open("hello.txt", "r", encoding="utf-8") as fh:
#     strings = fh.readlines()
#     strings = set(strings)

# with open("output.txt", "w", encoding="utf-8") as fh:
#     fh.writelines(strings)


with open("input.txt", "r", encoding="utf-8") as fh:
    file = fh.read()

with open("output.txt", "w", encoding="utf-8") as fh:
    fh.write(file[::-1])


# Реалізуйте програму, яка зчитує вміст файла "input.txt"
# і зберігає його у файлі "output.txt" у зворотньому порядку.







# Напишіть функцію, яка приймає шлях до файла як аргумент і повертає кількість рядків у файлі.

# def len_lines(path: str) -> int:
#     with open(path, "r", encoding="utf-8") as fh:
#         return len(fh.readlines())


# path = "hello.txt"
# print(len_lines(path))



# Реалізуйте програму, яка зчитує вміст файла "data.txt" і виводить кількість слів у цьому файлі.








# Напишіть функцію, яка отримує шлях до файла і слово як аргументи.
# Функція повинна перевіряти, скільки разів слово зустрічається у файлі.








# Реалізуйте програму, яка зчитує вміст кількох файлів і об'єднує їх у новий файл "combined.txt".







# Напишіть функцію, яка перевіряє, чи є файл "data.txt" порожнім.







# Напишіть функцію, яка отримує шлях до файла і перевіряє, чи містить файл лише числа.
# Поверніть True, якщо так, і False — у протилежному випадку.







# Реалізуйте програму, яка знаходить найдовший рядок у файлі "data.txt" і виводить його разом із його довжиною.









# Реалізуйте програму, яка видаляє всі порожні рядки з файла "data.txt".