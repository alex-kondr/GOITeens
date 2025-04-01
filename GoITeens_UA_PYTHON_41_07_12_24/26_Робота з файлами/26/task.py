# file = open("test")
# text_file = file.read()
# print(text_file)
# file.close()

# fh = open("file_write.txt", "w", encoding="utf-8")
# fh.write("Щось нове")
# fh.close()

# file = open("file_write.txt")
# print(file.read())
# file.close()

# fd = open("text.bin", "wb")
# fd.write("\nЦей текст буде з нового рядка")
# fd.close()

# with open("test.txt") as fh:
#     text = fh.read(4)
#     text1 = fh.read()

# print(text)
# print(text1)

# with open("new.txt", "a", encoding="utf-8") as file:
#     strings = ["Hello", "world!", "Привіт", "світ!"]
#     for string in strings:
#         file.write(string)

with open("new.txt", "a", encoding="utf-8") as file:
    strings = ["Hello", " ",  "world!\n", "Привіт", " ", "світ!"]
    file.writelines(strings)

# with open("new.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines(10)

# print(lines)

# with open("new.txt", encoding="utf-8") as file:
#     file.seek(10)
#     text = file.read()

# print(text)

with open("input.txt", "w", encoding="utf-8") as file:
    file.write("Яка чудова сьогодні погода.")


with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

text = text[::-1]

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text)


with open("input.txt", "r", encoding="utf-8") as file_1:
    with open("output.txt", "w", encoding="utf-8") as file_2:
        file_2.write(file_1.read()[::-1])
