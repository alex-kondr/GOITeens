# LOGIN = "alex"
# _LO123GIN_TEST = "test"
# PASS = "123456"
# print(LOGIN)

# print(LOGIN)


# money = 0

# if not money:
#     print("no money")


# user_name = input("Enter your name: ")
# print(type(user_name))
# if user_name:
# 	print(f"Hello {user_name}")
# else:
# 	print("Hi Anonym!")


# some_data = "Alex"
# msg = some_data or "Дані відсутні"
# print(msg)



X = input("Введіть координату X > ")
X = float(X)
Y = input("Введіть координату Y > ")
Y = float(Y)

if X > 0 and Y > 0:
    print(1)

elif X < 0 and Y > 0:
    print(2)

elif X < 0 and Y < 0:
    print(3)

else:
    print(4)



# a = 5
# b = 6
# a = 1
# b = 2

# if a > b:
#     print()

# if a > b:
#     print(a)

# if a > b:
#     print(b)

# if a >= b:
#     print()

# else: # a=b
#     print("Тут нічого немає")

# if a == b:
#     print("a = b")


# user_name = input("Enter your name: ")
# print(user_name)
# if user_name:
# 	print(f"Hello {user_name}")
# else:
# 	print("Hi Anonym!")




# name = "Alex"
# age = 22
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")
# else:
#     print("No name - no car")


# a = 6

# abs_number = a if a >=0 else -a
# print(abs_number)

# a = 0
# b = ""

# number = a or b or "Ви не введи число"
# print(number)





# a = False or False
# print(a)




# a = True or False
# print(a)



# a = not 2 < 0
# print(a)


# is_nice = "0"
# state = "nice" if float(is_nice) else "not nice"
# print(state)

# some_data = 123
# msg = "" or some_data
# print(msg)


# score = 5
# grade = "Pass" if score >= 60 else "Fail"
# print(grade)


# Оголосити змінні х, у, z  (числа).
# За допомогою умовного оператора перевірити яке число більше.

# x = 800
# y = 6000
# z = 105

# if x > y:
#     if x > z:
#         print(f"{x = }")
#     else:
#         print(f"{z = }")
# elif y > z:
#     print(f"{y = }")
# else:
#     print(f"||{z = }")





# Прийняти на вхід число — вік користувача.
# Перевірити чи може користувач самостійно відкрити рахунок у банку (вік >= 18)
# bank_name = "Privat"
# age = int(input(f"Введіть свій вік для банку {bank_name} > "))

# if age >= 18:
#     print("Запрошуємо Вас в банк")
# else:
#     print("Приходьте з батьками")

################################################




# Створити програму-помічник, яка приймає на вхід температуру води (float).
# Після цього програма проведе аналіз та підкаже, який стан води. (Принаймі 2 умови)
# temp = float(input("Введіть температуру води > "))

# if temp >= 100:
#     print("Вода знаходиться у газоподібному стані")
# elif temp <= 0: # temp > 0 and temp < 100:
#     print("Лід")
# else:
#     print("Рідина")




# Прийняти на вхід число, перевірити, чи закінчується число на 0.
# a = 4501
# if not a % 10:
#     print("Дане число не закінчується на нуль")
# else:
#     print("Дане число закінчується на нуль")







# Дано ціле число. Якщо воно негативне, додати до нього 20; інакше відняти 5.
# Вивести отримане число.
# a = -45

# a -= 5
# a += 5
# a *= 5
# a /= 5
# a **= 5

# if a > 0:
#     a -= 5 # a = a - 5
# else:
#     a += 20

# print(a)




# Дано ціле число. Якщо воно є позитивним, помножити його на 5;
# інакше піднести до степеня 3. Вивести отримане число.
# a = 5

# if a > 0:
#     a *= 5
# else:
#     a **= 3 # a = a ** 3

# print(a)





# Дано чотири числа. Знайти кількість чисел, які діляться на 5.
# a = 40
# b = 75
# c = -130
# d = 105

# count = 0

# if a % 5 == 0:
#     count += 1

# if b % 5 == 0:
#     count += 1

# if c % 5 == 0:
#     count += 1

# if d % 5 == 0:
#     count += 1

# print(f"Кількість чисел, що діляться на 5: {count}")





# Дано п'ять чисел.
# Знайти кількість чисел, які ділять на 2 та к-ть чисел які діляться на 3 у даному наборі.
# a = 78
# b = 13
# c = 96
# d = -5
# e = 27

# count_2 = 0
# count_3 = 0

# if a % 2 == 0:
#     count_2 += 1

# if a % 3 == 0:
#     count_3 += 1

# print(f"К-ть чисель, які діляться на 2: {count_2}")
# print(f"К-ть чисель, які діляться на 3: {count_3}")



# Дано дві змінні дійсного типу: A, B.
# Перерозподілити значення даних змінних так, щоб в A опинилось більше значення, а B — менше.
# Вивести нові значення змінних A та B.
# A = float(input("Введіть число 1 > "))
# B = float(input("Введіть число 2 > "))

# C = A
# A = A if A > B else B
# B = C if C < B else B
# print(A, B)







# Магазин дає знижку 5%, якщо покупець здійснить покупку більше ніж на 500 грн, 10% - більше 1000 грн.
# Доставка коштує 150 грн, але при покупці більше ніж на 1300 грн доставка безкоштовна.
# Завдання: Запитати у користувача кількість купленого товару. Нехай одна одиниця товару коштує 85 грн.
# Перевірити та порахувати загальну суму для користувача.
# count_pen = int(input("Введіть кількість ручок > "))
# cost = count_pen * 85
# delivery = 150

# if cost > 1300:
#     print("Доставка безкоштовна")
#     delivery = 0

# if cost > 1000:
#     print("Діє знижка 10%")
#     cost *= 0.9
# elif cost > 500:
#     print("Діє знижка 5%")
#     cost *= 0.95

# print(f"До сплати: {cost + delivery}")






# Дано три числа.
# Знайти середнє з них (тобто число, розташоване між найменшим та найбільшим).
# a = 500
# b = 13
# c = 1

# if a > b > c or c > b > a:
#     print(b)
# elif b > a > c or c > a > b:
#     print(a)
# elif a > c > b or b > c > a:
#     print(c)



# Арифметичні дії над числами пронумеровані таким чином:
# 1 — ділення на ціло, 2 — залишок від ділення, 3 — піднесення до 2 степення, 4 — піднесення до 3 степеня.
# Дано номер дії N (ціле число в діапазоні 1–4) та дійсні числа A та B (B не дорівнює 0).
# Виконати над числами вказану дію та вивести результат.
# number = int(input("Введіть номер дії > "))
# A = float(input("Введіть число А > "))
# B = float(input("Введіть число В > "))

# result = 0

# if number == 1:
#     result = A // B
# elif number == 2:
#     result = A % B
# elif number == 3:
#     result = A ** 2 + B ** 2
# elif number == 4:
#     result = A ** 3 - B ** 3
# else:
#     print("Дана дія не визначена")

# print(result)




# Одиниці вимірювання довжини пронумеровані так:
# 1 — дециметр, 2 — кілометр, 3 — метр, 4 — міліметр, 5 — сантиметр.
# Дано номер одиниці вимірювання довжини (ціле число в діапазоні 1–5) та довжина відрізка в цих одиницях(дійсне ціле).
# Знайти довжину відрізка в метрах.
# lenght = float(input("Введіть довжину відрізка > "))
# number = int(input("Введіть номер одиниці вимірювання > "))

# # result = 0

# if number == 1:
#     lenght /= 10
# elif number == 2:
#     lenght *= 1000
# elif number == 4:
#     lenght /= 1000
# elif number == 5:
#     lenght /= 100
# elif number == 3:
#     pass
# else:
#     print("Дана одиниця вимірювання не відома")

# print(lenght, "метрів")




# На технічній співбесіді претенденти на посаду одержують оцінку за тест.
# У наступний тур співбесіди проходять кандидати, які склали тест на 83 бали включно або вище.
# Реалізуйте оператор контролю виконання так, щоб він привласнив логічній змінній is_next значення True,
# якщо кількість набраних балів буде більшою або дорівнює 83.
# В іншому випадку значення змінної дорівнює False.
a = 81
is_next = True if a >= 83 else False

# if a >= 83:
#     is_next = True






# Дано ціле число, що лежить у діапазоні 1-999.
# Вивести рядок-опис виду «парне двозначне число», «непарне тризначне число» тощо.



# У нас є три логічні змінні.
# Перша визначає статус користувача is_active, яка дорівнює True або False.
# Друга is_admin визначає, чи є у користувача права адміністратора теж булевого типу.
# Третя is_permission — чи дозволено доступ, теж булевого типу.
# Приведіть змінні is_active, is_admin та is_permission до булевого вигляду.
# Надайте змінній access значення, яке покаже, чи є доступ у користувача. Використовуйте логічні оператори.
# Адміністратор завжди має доступ, незалежно від значень змінних is_permission та is_active.
# Користувач має доступ, тільки якщо is_permission дорівнює True та is_active також дорівнює True.





# Як відомо, зазвичай розробників заведено поділяти на три категорії:
# Джун (Junior), Мідл ( Middle) — основний розробник у компанії та Сеньйор (Senior) — старший розробник.
# Орієнтовно можна вважати, що до 1 року роботи включно — це Джуніор,
# понад 5 років — це Сеньйор розробник, а від одного року до 5 включно — мідл.
# Є змінна work_experience, що визначає стаж роботи програміста.
# Залежно від стажу роботи, присвоїти змінній developer_type значення "Junior", "Middle" або "Senior".






# Необхідно обчислити корінь квадратного рівняння.
# a · x2 + b · x + c = 0
# Дискримінант рівняння помістіть у змінну D
# D = b2 - 4 · a · c
# Корінь рівняння помістіть у змінні x1 та x2
# x1 = (-b + D ** 0.5) / (2 · a)
# x2 = (-b - D ** 0.5) / (2 · a)

