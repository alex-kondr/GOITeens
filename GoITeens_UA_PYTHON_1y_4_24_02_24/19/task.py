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

# with open("input.txt", "r", encoding="utf-8") as input_file:
#     string = input_file.read()

# with open("output.txt", "w", encoding="utf-8") as output_file:
#     output_file.write(string[::-1])


# output.txt

# fh = open("output.txt", "w", encoding="utf-8")
# fh.write("Абагаламага")
# fh.close()

# fh = open("output.txt", "a", encoding="utf-8")
# fh.write("Абагаламага")
# fh.close()

# with open("output.txt", "w", encoding="utf-8") as fh:
#     fh.write("Абагаламага")

# with open("output.txt", "a", encoding="utf-8") as fh:
#     fh.write("Абагаламага")
















# Напишіть програму, яка зчитує вміст файлу "input.txt"
# і записує його у файл "output.txt" з виключенням повторюваних рядків.

# with open("input.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()

# print(lines)
# print(set(lines))

# with open("output.txt", "w", encoding="utf-8") as file:
#     file.writelines(set(lines))








# Напишіть функцію, яка приймає шлях до файла як аргумент і повертає кількість рядків у файлі.

# def len_lines(path: str) -> int:
#     with open(path, "r", encoding="utf-8") as fh:
#         lines = fh.readlines()
#         print(lines)

#     return len(lines)

# print(len_lines("output.txt"))



# Реалізуйте програму, яка зчитує вміст файла "data.txt" і виводить кількість слів у цьому файлі.

# with open("data.txt", "r", encoding="utf-8") as file:
#     text = file.read()

# words = text.split()
# print(words)
# print(len(words))






# Напишіть функцію, яка отримує шлях до файла і слово як аргументи.
# Функція повинна перевіряти, скільки разів слово зустрічається у файлі.

# def find_word(path: str, word: str) -> int:
#     with open(path, "rb", encoding="utf-8") as file:
#         text = file.read()

#     return text.count(word)


# print(find_word("data.txt", "програму"))


# with open("test.bin", "wb") as file:
#     file.write("Абабагаламага\n".encode(encoding="win-1256"))



# Реалізуйте програму, яка зчитує вміст кількох файлів і об'єднує їх у новий файл "combined.txt".







# Напишіть функцію, яка перевіряє, чи є файл "data.txt" порожнім.







# Напишіть функцію, яка отримує шлях до файла і перевіряє, чи містить файл лише числа.
# Поверніть True, якщо так, і False — у протилежному випадку.







# Реалізуйте програму, яка знаходить найдовший рядок у файлі "data.txt" і виводить його разом із його довжиною.









# Реалізуйте програму, яка видаляє всі порожні рядки з файла "data.txt".