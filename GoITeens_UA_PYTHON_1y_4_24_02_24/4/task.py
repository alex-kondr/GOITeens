# a = 0
# b = a or 10

# b = a if a > 5 else 10


# fruit = "apple"

# for char in fruit:
# 	print(char)
# else:
#     print(f"Поза циклом {char=}")


# numbers = [1, 2, 3, 4, 5.5]
# suma = 0

# for number in numbers:
# 	suma += number # suma = suma + number
# else:
#     print(suma)


# for i_ in range(5):
#     print(f"Hello")


# suma = 0

# for x in range(0, 6):
# 	print(x)
# 	suma += x

# print(suma)



# a = 1
# b = 5
# c = 1
# d = 5


# #print header
# print(end = '\t')
# for i in range(c, d + 1) :
#     print(i, end = '\t')
# print("")

# #print table
# for i in range(a, b + 1) :
#     print(i, end = '\t')
#     for j in range(c, d + 1) :
#         print(i * j, end = '\t')
#     print("")


# a = 1

# while a <= 5:
#     print(a)
#     a += 1
# else:
#     print("Done")




# a = int(input())
# b = int(input())

# sum = 0
# count = 0

# for i in range(a, b + 1) :
#     if i % 3 == 0 :
#         sum += i
#         count += 1

# print(sum / count)




# a = 0

# while True:
#     print(a)

#     # if a >= 20:
#     #     break

#     a += 1

# print("Done")



# while True:
#     name = input('Enter name: ')

#     if name == 'stop':
#         print("Bye")
#         break

#     print('Hello', name)



# a = 0

# while a < 60:
#     a += 1

#     if a % 2:
#         continue

#     print(a)



# while True:
#     i = int(input("Введіть ціле число > "))

#     if i > 100 :
#         break

#     if i < 20 :
#         continue

#     print(i)



##################################

# Організувати безперервне введення з клавіатури чисел.
# Якщо число більше 20, то вивести його на екран.
# Якщо число більше 100 — закінчити роботу програми.

# while True:
#     number = float(input("Введіть своє число: "))

#     if number > 100:
#         print("Bye")
#         break

#     elif number > 20:
#         print(number)








# Оператори continue і break працюють тільки всередині одного циклу.
# У ситуації вкладених циклів немає способу вийти з усіх циклів одразу

# while True:
#     number = input("number = ")
#     number = int(number)

#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
#             break
#     break






# Порахувати середнє арифметичне всіх чисел кратних 5 з певного інтервалу
# start = int(input("Початок діапазону > "))
# end = int(input("Кінець діапазону > "))

# sum = 0
# count = 0

# for i in range(start, end + 1):
#     if not i % 5:
#         sum += i
#         count += 1

# result = sum / count

# print(f"Середнє арифметичне чисел від {start} до {end} дорівнює {result}")








# Написати програму, яка буде підраховувати суму всіх парних чисел від 1 до 100. ---------1
# start = 1
# end = 100

# sum = 0

# for i in range(start, end + 1):
#     if i % 2 == 0:
#         sum += i
# else:
#     print(f"Сума парних чисель від {start} до {end} дорівнює {sum}")





# Написати програму, яка приймає на вхід рядок, введений з клавіатури, ---------------2
# і підраховує кількість входження в рядок останньої літери,
# якою закінчується цей рядок.
# string = input("Введіть своє речення: ") # Мене звани Олександр. Проживаю в Одеській області
# last_char = string[-1]

# count = 0

# for char in string:
#     if char == last_char:
#         count += 1

# print(f"Символ '{last_char}' зустрічається {count} р.")

####################




# Дано ціле число, що лежить у діапазоні 1-999.
# Вивести рядок-опис виду «парне двозначне число», «непарне тризначне число» тощо.
# while True:
#     a = int(input("Введіть ціле число: "))

#     is_even = False
#     count_digit = 0

#     if a % 2 == 0:
#         is_even = True

#     if a // 100:
#         count_digit = 3
#     elif a // 10:
#         count_digit = 2
#     else:
#         count_digit = 1

#     print(f"Число {a} {'парне' if is_even else 'непарне'} та має таку кількість цифр: {count_digit}")




# Написати код який буде просити команду і відразу її друкувати
# до поки він його не напише "stop", "exit" aбо "bye".
# while True:
#     command = input("Введіть свою команди: ")

#     if command == "stop" or command == "exit" or command == "bye":
#         print("Bye bye")
#         break

#     print(f"{command = }")








# Написати код який рахує добуток всіх чисел в діапазоні який задав користувач
# start = int(input("Введіть ціле число для початоку діапазону: "))
# end = int(input("Введіть ціле число для кінця діапазону: "))

# result = 1

# for num in range(start, end + 1):
#     result *= num

# print(f"Добуток чисел від {start} до {end} дорівнює {result}")






# У нас є три логічні змінні.
# Перша визначає статус користувача is_active, яка дорівнює True або False.
# Друга is_admin визначає, чи є у користувача права адміністратора теж булевого типу.
# Третя is_permission — чи дозволено доступ, теж булевого типу.
# Приведіть змінні is_active, is_admin та is_permission до булевого вигляду.
# Надайте змінній access значення, яке покаже, чи є доступ у користувача. Використовуйте логічні оператори.
# Адміністратор завжди має доступ, незалежно від значень змінних is_permission та is_active.
# Користувач має доступ, тільки якщо is_permission дорівнює True та is_active також дорівнює True.
# is_active = True
# is_admin = False
# is_permission = True

# access = "Доступ дозволено" if is_admin or (is_active and is_permission) else "Доступ відхилено"
# print(f"{access}")




# Написати програму, яка виведе список квадратів чисел.
# start = 1
# end = 100

# for i in range(start, end + 1):
#     print(i ** 2)











# Написати програму, яка виведе числа від 7 до 77 використовуючи цикл
# start = 7
# end = 77

# for i in range(start, end + 1):
#     print(f"{i = }")








# Як відомо, зазвичай розробників заведено поділяти на три категорії:
# Джун (Junior), Мідл ( Middle) — основний розробник у компанії та Сеньйор (Senior) — старший розробник.
# Орієнтовно можна вважати, що до 1 року роботи включно — це Джуніор,
# понад 5 років — це Сеньйор розробник, а від одного року до 5 включно — мідл.
# Є змінна work_experience, що визначає стаж роботи програміста.
# Залежно від стажу роботи, присвоїти змінній developer_type значення "Junior", "Middle" або "Senior".
# work_experience = 4

# if work_experience > 5:
#     print("Senior")
# elif work_experience <= 1:
#     print("Junior")
# else:
#     print("Middle")






# Дано змінну a = -56. Виводити a, поки a <= 15, збільшуючи змінну на 3
# a = -56

# while a <= 16:
#     print(f"{a = }")
#     a += 3











# Написати програму, яка на початку додасть “I am glad to see you, ” до кожного із імен в списку
# і виведе привітання на екран.Приклад — I am glad to see you, Alex!

# names = ["Alex", "Petro", "Max", "Andrii", "Lev"]

# for name in names:
#     print(f"\nI am glad to see you, {name}!", end="\n\n")







# Необхідно обчислити корінь квадратного рівняння.
# a · x2 + b · x + c = 0
# Дискримінант рівняння помістіть у змінну D
# D = b2 - 4 · a · c
# Корінь рівняння помістіть у змінні x1 та x2
# x1 = (-b + D ** 0.5) / (2 · a)
# x2 = (-b - D ** 0.5) / (2 · a)
# a = 1
# b = 5
# c = 9

# D = b ** 2 - 4 * a * c
# if D >= 0:
#     x1 = (-b + D ** 0.5) / (2 * a)
#     x2 = (-b - D ** 0.5) / (2 * a)

#     print(f"{x1 = }, {x2 = }")

# else:
#     print("Розв'язку немає")







# Дано слово "Молоко". За допомогою циклу порахувати скільки літер "о" містить в собі це слово.
# string = "Молокоoooooooooooooooooo"

# count = 0

# for char in string:
#     if char == "o":
#         count += 1

# print(f"Кількість букв 'о' в слові {string} дорвінює {count}")






# Зробити попередню програму більш універсальною:
# Запитувати у користувача речення та літеру для пошуку.
# string = input("Введіть своє речення > ")
# find_char = input("Введіть символ для пошуку > ")

# count = 0

# for char in string:
#     if char == find_char:
#         count += 1

# print(f"Кількість символів '{find_char}' в речені '{string}' дорвінює {count}")







# Використати блок “else” щоб вивести повідомлення "Цикл повністю завершився"
# після успішного виходу з циклу (довільний)








# Написати програму, яка порахує і виведе числа у 4 степені від 1 до числа, яке задасть користувач









# Дано дійсне число — ціна 2 л молока. Вивести вартість 1, 2, ..., 10 л молока.








# Дано дійсне число - ціна 3 кг сала. Вивести вартість 1.2, 1.4, ..., 2 кг сала.









# Дано діапазон чисел від -100 до 0. Вивести на екран лише числа, які закінчуються на нуль








# Дано діапазон чисел (Користувач обирає сам (input)).
# Вивести на екран лише числа, які діляться на 3 та закінчуються на нуль







# Написати програму, яка виведе факторіал числа, яке задасть користувач (цикл while)






# Написати програму, яка зчитає 3 числа (a, b, c) та порахує скільки чисел лежить між “a” i “b”, які діляться на “с”



