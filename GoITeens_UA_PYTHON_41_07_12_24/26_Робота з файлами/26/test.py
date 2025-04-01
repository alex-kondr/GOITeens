# Напишіть програму, яка зчитує вміст файлу "input.txt"
# і записує його у файл "output.txt" з виключенням повторюваних рядків.

open_file = open("input.txt", "r", encoding="utf-8")
read_file = []
for line in open_file:
    if line not in read_file:
        read_file.append(line)
open_file.close()
new_file = open("output.txt", "w", encoding="utf-8")
new_file.writelines(read_file)
new_file.close()