# Оголосити змінні х, у, z  (числа). За допомогою умовного оператора перевірити яке число більше.

# a = int(input("Введіть число a: "))
# b = int(input("Введіть число b: "))
# c = int(input("Введіть число c: "))

# if a > b and a > c:
#     print(f"Найбільше число {a}")
# elif b > a and b > c:
#     print(f"Найбільше число {b}")
# else:
#     print(f"Найбільше число {c}")

# Прийняти на вхід число — вік користувача. Перевірити чи може користувач самостійно відкрити рахунок у банку (вік >= 18)

# age = int(input("Введіть свій вік: "))
# if age >= 18:
#     print("Ви можете відкрити власний рахунок.")
# else:
#     print("Ви ще не можете відкрити власний рахунок.")


# name = "Олексій"
# age = 19
# has_score = True
# message = "ви можете мати рахунок" if name and has_score and age >= 18 and has_score else  "ви не можете мати рахунок"


# Створити програму-помічник, яка приймає на вхід температуру води (float).
# Після цього програма проведе аналіз та підкаже, який стан води. (Принаймі 2 умови)

# temperature = float(input("Введіть температуру води в градусах : "))
# if temperature <= 0:
#     print("Вода в твердому стані")
# elif temperature >= 100:
#     print("Вода в газоподібному стані")
# else:
#     print("Вода в рідкому стані")





# Прийняти на вхід число, перевірити, чи закінчується число на 0.
# a = input("Введіть число:")
# a = float(a)
# if not a % 10:
#     print("число закінчується на 0")
# else:
#     print("число не закінчується на 0")



# Дано ціле число. Якщо воно від'ємне, додати до нього 20; інакше відняти 5.
# Вивести отримане число.
# a = int(input("Введіть ціле число: "))
# if a < 0:
#     a += 20 # a = a + 20
# else:
#     a -= 5

# a += 5
# a -= 10
# a /= 20
# a *= 6
# a **= 2

# print(a)

# number = float(input("введіть ціле число"))
# if number < 0 :
#     second_number = number + 20
#     print(second_number)
# elif number >= 0 :
#     third_number = number - 5
#     print(third_number)


# Дано ціле число. Якщо воно є позитивним, помножити його на 5; інакше піднести до степеня 3.
# Вивести отримане число.
# number = int(input("Введіть число: "))
# if number > 0:
#     number *= 5
# else:
#     number **= 3
# print(number)


# number = float(input("Введіть ціле число "))
# if number > 0:
#     number *= 5
# else:
#     number **= 3
# print(number)

# a = int(input("Введіть число"))
# if a >= 0:
#     a *= 5
# else:
#     a **= 3
# print(a)

# Дано чотири числа. Знайти кількість чисел, які діляться на 5.
a = float(input("Перше число: "))
b = float(input("Друге число: "))
c = float(input("Третє число: "))
d = float(input("Четверте число: "))

count = 0
if a % 5 == 0:
    count += 1

if b % 5 == 0:
    count += 1

if c % 5 == 0:
    count += 1

if d % 5 == 0:
    count += 1

print(f"Всього чисел 4, з них діляться на 5 - {count}")