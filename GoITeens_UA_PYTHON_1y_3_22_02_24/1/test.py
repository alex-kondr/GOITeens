# print("Hello")
# print("Hello world")
# print()

# name = input("What is your name? ")

# print("My name is", name)
# print(f"My name is {name}")
# print("My name is {}".format(name))

# name = input("What is your name? ")
# print(name)

print("""
 __      ______  _________   ___ __ __  ______        ________  _________
/_/\\    /_____/\\/________/\\ /__//_//_/\\/_____/\\      /_______/\\/________/\\
\\:\\ \\   \\::::_\\/\\__.::.__\\/ \\::\\| \\| \\ \\::::_\\/_     \\__.::._\\/\\__.::.__\\/
 \\:\\ \\   \\:\\/___/\\ \\::\\ \\    \\:.      \\ \\:\\/___/\\       \\::\\ \\    \\::\\ \\
  \\:\\ \\___\\::___\\/_ \\::\\ \\    \\:.\\-/\\  \\ \\::___\\/_      _\\::\\ \\__  \\::\\ \\
   \\:\\/___/\\:\\____/\\ \\::\\ \\    \\. \\  \\  \\ \\:\\____/\\    /__\\::\\__/\\  \\::\\ \\
    \\_____\\/\\_____\\/  \\__\\/     \\__\\/ \\__\\/\\_____\\/    \\________\\/   \\__\\/
""")

a = 64
b = 11
# print("a + b =", a + b, end=", ")
# print(f"a + b = {a + b}")
# print(a, '+', b, '=', a + b, sep="\t")
# print(1, 2, 3, 4, 5, 6, sep='-')

# Мене-!-звати-!-Микола-!-Олександрович

# first_name = "Микола"
# second_name = "Олександрович"
# print("Мене", "звати", first_name, second_name, sep="-!-")

# name = input("Enter your name: ")
# print(f"My name is {name}")

# age = input("How old are you? ")
# print(type(age))
# age = int(age)
# print(type(age))
# print("Мені {}".format(age))

# city = input("Where do you live? ")
# print(f"Я живу у місті {city}")

# print(f"Мене звати {name}. Мені {age} років. На даний час я проживаю в місті {city}")

# a = int(input("Введіть число 1: "))
# b = int(input("Введіть число 2: "))
# print(a + b)

# cats = int(input("Скільки у тебе котів: "))
# dogs = int(input("Скільки у тебе собак: "))
# cows = int(input("Скільки у тебе корів: "))

# print("Котів: ", cats, ", собак: ", dogs, ", корів: ", cows, ". Всього тварин ", cats + dogs + cows, sep="")
# print(f"Котів: {cats}, собак: {dogs}, корів: {cows}. Всього тварин {cats + dogs + cows}")
# print("Котів: {cats}, собак: {dogs}, корів: {cows}".format(cats=cats, dogs=dogs, cows=cows), ". Всього тварин", cats + dogs + cows, sep="")

# a = int(float(input("Введіть перше ціле число:\n")))
# b = int(float(input("Введіть друге ціле число:\n")))
# print(a, '+', b, '=', a + b)
# print(a, '-', b, '=', a - b)
# print(a, '*', b, '=', a * b)
# print(a, '/', b, '=', a / b)
# print(a, '**', b, '=', a ** b)
# print(a, '//', b, '=', a // b)
# print(a, '%', b, '=', a % b)

# length = input("Введіть довжину поля: ")
# width = input("Введіть ширину поля: ")

# area = float(length) * float(width)
# print(area)


# Напишіть програму для підрахунку дрібних грошей. Вона повинна питати:

# «Скільки у вас монет по 50 копійок?»;
# «Скільки у вас монет по 25 копійок?»;
# «Скільки у вас монет по 10 копійок?»;
# «Скільки у вас монет по 5 копійок?».
# Після цього на екрані повинна з'явитися загальна сума.

count_50 = int(input("Скільки у вас монет по 50 копійок?>"))
count_25 = int(input("Скільки у вас монет по 25 копійок?>"))
count_10 = int(input("Скільки у вас монет по 10 копійок?>"))
count_coint_5 = int(input("Скільки у вас монет по 5 копійок?"))

sum_coin = count_50 * 50 + count_25 * 25 + count_10 * 10 + count_coint_5 * 5

print(f"Гривні: {sum_coin // 100}, копійки: {sum_coin % 100}")