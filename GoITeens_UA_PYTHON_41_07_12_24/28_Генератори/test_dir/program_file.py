with open("test_dir/films.txt", "r", encoding="utf-8") as file:
    text = file.read()


with open("outpu.txt", "w", encoding="utf-8") as file:
    file.write(text[::-1])

print(text)