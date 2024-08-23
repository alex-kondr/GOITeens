# file = open("input.txt", "r", encoding="utf-8")
# print(file.read())
# file.close()

# file = open("sub_dir/test_file.txt")
# text = file.read()
# file.close()

# print(text)

# file = open("text.txt", "w", encoding="utf-8")
# file.write("Який чудовий день!!!!!")
# file.close()

# file = open("text.txt", "a", encoding="utf-8")
# file.write("\nЗавтра буде чудовий день!!!")
# file.close()

# file = open("text.txt", "r")
# file = open("text.txt", "w")
# file = open("text.txt", "r+")
# file = open("text.txt", "w+")
# file = open("text.txt", "a")
# file = open("text.txt", "a+")


# file = open("text.txt", "r", encoding="utf-8")
# text = file.readlines()
# file.close()

# for t in text:
#     print(t, end="")

# text = 'Реалізуйте програму, яка зчитує вміст файла "input.txt"'
# strings = ["Hello\n", "world\n", "!!!!!!!!!!!\n"]


# # file = open("text1.txt", "w", encoding="utf-8")
# # file.writelines(strings)
# # file.close()

# file = open("text1.txt", "a", encoding="utf-8")

# for text in strings:
#     file.write(text)

# file.close()


# with open("text.txt", "r", encoding="utf-8") as file:
#     string = file.read()

# print("Hello")

# print(f"{string = }")





# fh = open("my_file")
# # fh = open("test/test.txt")
# text = fh.read()
# fh.close()

# print(text)

# fh = open("my_file", "r", encoding="utf-8")
# fh = open("my_file1.txt", "w", encoding="utf-8")
# fh = open("my_file1.txt", "r+", encoding="utf-8")
# fh = open("my_file1.txt", "w+", encoding="utf-8")
# fh = open("my_file1.txt", "a", encoding="utf-8")
# fh = open("my_file1.txt", "a+", encoding="utf-8")

# fh = open("text_1.txt", "w", encoding="utf-8")
# fh.write("Привіт світ!")
# fh.close()

# fh_1 = open("text_1.txt", "r", encoding="utf-8")
# fh_2 = open("text_2.txt", "r", encoding="utf-8")

# string = fh_1.read() + fh_2.read()

# fh_1.close()
# fh_2.close()


# fh = open("my_file.txt", "r", encoding="utf-8")
# for line in fh.readline():
#     print(line)

# fh.close()
# # print(string)
# string = 'fh\open("my_file.txt\n"'

# fh = open("text_1.txt", "w", encoding="utf-8")
# fh.writelines(strings)
# fh.close()

# fh = open("text_1.txt", "a", encoding="utf-8")
# fh.write(string)
# fh.close()

# with open("new_file.txt", "w", encoding="utf-8") as fh1:
#     fh1.write("Абабагаламага")

#     with open("my_file.txt", "r", encoding="utf-8") as fh2:
#         string = fh2.read()

#         fh1 + fh2

# print(string)



# Реалізуйте програму, яка зчитує вміст файла "input.txt"
# і зберігає його у файлі "output.txt" у зворотньому порядку.


# string = "Hello"
# print(string[::-1])














# Напишіть програму, яка зчитує вміст файлу "input.txt"
# і записує його у файл "output.txt" з виключенням повторюваних рядків.

# with open("input.txt", "r", encoding="utf-8") as file:
#     strings = file.readlines()

# my_set = set(strings)
# string = "".join(my_set)

# with open("output.txt", "w", encoding="utf-8") as fh:
#     # fh.writelines(my_set)
#     fh.write(string)





# Напишіть функцію, яка приймає шлях до файла як аргумент і повертає кількість рядків у файлі.

# def count_lines(path: str) -> int:
#     with open(path, "r", encoding="utf-8") as fd:
#         strings = fd.readlines()

#     return len(strings)


# print(count_lines("input.txt"))












# Реалізуйте програму, яка зчитує вміст файла "data.txt" і виводить кількість слів у цьому файлі.

# with open("input.txt", "r", encoding="utf-8") as file:
#     my_file = file.read()

# words = my_file.split()
# print(len(words))












# Напишіть функцію, яка отримує шлях до файла і слово як аргументи.
# Функція повинна перевіряти, скільки разів слово зустрічається у файлі.

# def count_word(path: str, word: str) -> int:
#     with open(path, "r", encoding="utf-8") as file:
#         string = file.read()

#     return string.count(word)

# print(count_word(word="програму", path="input.txt"))
# print(count_word("input.txt", "записує"))
# print(count_word("input.txt", "hello"))











# Реалізуйте програму, яка зчитує вміст кількох файлів і об'єднує їх у новий файл "combined.txt".







# Напишіть функцію, яка перевіряє, чи є файл "data.txt" порожнім.







# Напишіть функцію, яка отримує шлях до файла і перевіряє, чи містить файл лише числа.
# Поверніть True, якщо так, і False — у протилежному випадку.







# Реалізуйте програму, яка знаходить найдовший рядок у файлі "data.txt" і виводить його разом із його довжиною.









# Реалізуйте програму, яка видаляє всі порожні рядки з файла "data.txt".