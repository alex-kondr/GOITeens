# Написати код який буде просити команду і відразу її друкувати
# до поки він його не напише "stop", "exit" aбо "bye".

# STOP_LIST = ["stop", "exit", "bye"]

# while True:
#     command = input("Введіть команду ('stop', 'exit', 'bye'  для виходу): ")
#     print(f"Ви ввели: '{command}'")
#     # if command.strip().lower() == "exit" or command.strip().lower() == "stop" or command.strip().lower() == "bye":
#     # if command.strip().lower() in {"stop", "exit", "bye"}:
#     if command.strip().lower() in STOP_LIST:
#         print("Програма завершена. До побачення!")
#         break


# Написати код який рахує добуток всіх чисел в діапазоні який задав користувач

# first_num = int(input("введіть перше число"))
# second_num = int(input("введіть друге число"))
# # second_num += 1
# numbers = 1

# for number in range(first_num , second_num + 1):
#     numbers *= number

# print(numbers)

# a = int(input("Введіть перше число діапазону: "))
# b = int(input("Введіть друге число діапазону: "))
# dob = 1
# for number in range(a,b+1):
#     dob *= number

# print(f"добуток заданого діапазону = {dob}")



# У нас є три логічні змінні.
# Перша визначає статус користувача is_active, яка дорівнює True або False.
# Друга is_admin визначає, чи є у користувача права адміністратора теж булевого типу.
# Третя is_permission — чи дозволено доступ, теж булевого типу.
# Приведіть змінні is_active, is_admin та is_permission до булевого вигляду.
# Надайте змінній access значення, яке покаже, чи є доступ у користувача. Використовуйте логічні оператори.
# Адміністратор завжди має доступ, незалежно від значень змінних is_permission та is_active.
# Користувач має доступ, тільки якщо is_permission дорівнює True та is_active також дорівнює True.

# is_active = False
# is_admin = False
# is_permission = False

# if is_admin:
#     print("Доступ дозволено")
# else:
#     print("Доступ заборонено")

# if is_active and is_permission:
#     print("Доступ дозволено")
# else:
#     print("Доступ заборонено")

# if is_admin:
#     access = True
# else:
#     access = is_active and is_permission 

# if is_admin or (is_active and is_permission):
#     print("Доступ дозволено")
# else:
#     print("Доступ заборонено")

# access = is_admin or (is_active and is_permission)
# msg = "Доступ дозволено" if is_admin or (is_active and is_permission) else "Доступ заборонено"


# Написати програму, яка виведе список квадратів чисел.
# a = int(input("Введіть перше число діапазону: "))
# b = int(input("Введіть друге число діапазону: "))
# for number in range(a, b+1):
#     number **= 2
#     print(number)


# for i in range(7, 78):
#     print(i)

# Дано змінну a = -56. Виводити a, поки a <= 15, збільшуючи змінну на 3

# a = -56
# while a <= 15:
#     print(a)
#     a += 3


# Дано слово "Молоко".
# За допомогою циклу порахувати
# скільки літер "о" містить в собі це слово.
# word = "Молоко"
# count = 0
# for letter in word:
#     if letter == "о":
#         count += 1

# print(count)