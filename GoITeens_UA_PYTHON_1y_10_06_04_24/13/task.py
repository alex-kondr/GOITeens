transport = {
    'AA1111AA': 'Іванов Іван',
    'IVANOV'  : 'Іванов Іван',
    'AA0007AA': 'Семенов Андрій',
    'AA007AA' : 'Іванов Іван',
    'AВ1111AВ': 'Вінниця Водоканал',
    'AІ1010КК': 'Семенов Андрій',
}

# for car_numb in transport:
#     print(car_numb)

# for car_numb in transport.keys():
#     print(car_numb)

# for full_name in transport.values():
#     print(full_name)

# for car_num, full_name in transport.items():
#     print(f"Власник Автомобіля з номерним знаком {car_num} - {full_name}")












# Оголосити словник, що має наступну структуру «ключ» — номерний знак транспортного засобу
# (наприклад «АА2565ІН»), значення «власник авто» (наприклад, Іванов Іван)
# Додати в словник два нові авто
# Знайти власника за номером автомобіля
# Обійти словник і вивести прізвища людей, які мають більше одного авто
# from pprint import pprint

# transport = {
#     'AA1111AA': 'Іванов Іван',
#     'IVANOV'  : 'Іванов Іван',
#     'AA0007AA': 'Семенов Андрій',
#     'AA007AA' : 'Іванов Іван',
#     'AВ1111AВ': 'Вінниця Водоканал',
#     'AІ1010КК': 'Семенов Андрій',
#     'AB0212KK': 'Семенов Андрій',
# }


# transport.update({'AA1321AA': 'Іванов Сергій'})
# transport["ВН1560АТ"] = "Пупкін Василь"
# pprint(transport)


# car_numb = input("Введіть номер транспортого засобу для пошуку: ")
# owner = transport.get(car_numb, "Не знайдений")
# print(f"Власник ТЗ з номером '{car_numb}' - {owner}")
# names = list(transport.values())

# full_names = set()

# for owner in names:
#     if names.count(owner) > 1:
#         full_names.add(owner)

# for name in full_names:
#     print(name.split()[0])


# Створіть словник “stock”, який міститиме в собі ключ — назва товару,
# значення — кількість товару на складі.
# Написати програму, яка запитує який товар та кількість, яку хоче купити користувач.
# Вивести на екран True, якщо користувач може купити цей товар, якщо ні — False.

# stock = {"Яблоко": 4, "Банани" : 3, "Груши" : 5}

# product = input("Введіть назву товару для покупки: ")
# count = int(input("Введіть к-ть товару: "))

# if product in stock and count <= stock[product]:
#     print("Даний товар є в наявності")
# else:
#     print("Товар відсутній, або його к-ть менша за запитувану")






# Створіть словник, який містить дані про користувачів вашого веб-сайту.
# Ключами в цьому словнику будуть імена користувачів, а значеннями — інформація про користувачів.
# Попросіть користувача ввести імена користувачів, про яких хоче дізнатися інформацію, через пробіл.
# Вивести інформацію про цих користувачів у форматі (Ім’я, вік, стать, електронна пошта).

# users = {
#     "Алекс": {
#         "username": "alex",
#         "age": 20,
#         "city": "Київ",
#         "sex": "male"
#     },
#     "Дмитро": {
#         "username": "dima",
#         "age": 15,
#         "city": "Одеса",
#         "e-mail": "dima@gmial.com"
#     },
#     "Владислав": {
#         "username": "vlad",
#         "age": 14,
#     },
# }

# names = input("Введіть імена користувачів через пробіл: ").split()

# for name in names:
#     print(
#         f"У користувача з ім'ям '{name}' "
#         f"логін - {users[name].get('username', 'Невідомий')}. "
#         f"Вік користувача: {users[name].get('age', 'Невідомо')}, електронна адреса: {users[name].get('e-mail', 'Невідомо')}"
#     )




# Дано словник, який містить «Прізвище»-«оцінка».
# На його основі створити новий словник, який буде містити лише учнів, які навчаються на 4 та 5.
# from pprint import pprint

# students = {
#     "Артем": 5,
#     "Владислав": 5,
#     "Микола": 5,
#     "Алекс": 2,
#     "Тетяна":4
# }

# new_students = {}

# # for student in students:
# #     if students[student] in [4, 5]:
# #         # new_students.update({student: students[student]})
# #         new_students[student] = students[student]

# for student, grade in students.items():
#     if grade in [4, 5]:
#         # new_students.update({student: grade})
#         new_students[student] = grade

# pprint(new_students, width=50)






# Погода. У словнику збережено інформацію про температуру в різних містах: ключами є назви міст,
# значеннями - температура. Розрахуйте середню температуру за вказаними містами

# temperatures = {"Київ" : 36,
#                 "Львів" : 32,
#                 "Черкаси" : 30,
#                 "Одеса" : 33
# }
# print(list(temperatures.values()))

# sum_temp = sum(temperatures.values())
# avg = sum_temp / len(temperatures)
# print(f"Середня температура по містам дорівнює {avg}")


# Створіть словник, який містить ключ — ім’я студента, значення — список із балами.
# Попросіть користувача ввести ім’я студента.
# Порахувати середній бал студента, ім’я якого ввів користувач.

# students = {"коля" : [3, 5, 4, 5, 5, 4, 4],
#             "василь" : [3, 2, 2, 1, 2, 3, 2],
#             "петро" : [5, 5, 5, 5, 5, 4, 5],
#             "олег" : [3, 3, 3, 2, 4, 4, 3],
#             "ігорь" : [4, 5, 4, 5, 5, 5, 4]
# }

# student = input("Введіть ім'я студента: ")
# grades = students.get(student, [0])

# sum_grades = sum(grades)
# avg = sum_grades / len(grades)
# print(f"Серендній бал студента '{student}' дорівнює {avg} б")





# Створіть словник, який містить ключ — ім’я студента, значення — список із балами.
# Напишіть програму, яка порахує середній бал усіх учнів та виведе його на екран.

# students = {"коля" : [3, 5, 4, 5, 5, 4, 4],
#             "василь" : [3, 2, 2, 1, 2, 3, 2],
#             "петро" : [5, 5, 5, 5, 5, 4, 5],
#             "олег" : [3, 3, 3, 2, 4, 4, 3],
#             "ігорь" : [4, 5, 4, 5, 5, 5, 4]
# }

# sum_all_grades = 0
# grades_count = 0

# for grades in students.values():
#     sum_all_grades += sum(grades)
#     grades_count += len(grades)

# avg = sum_all_grades / grades_count
# print(f"Середня оцінка всіх студентів: {avg} б")






# Напишіть програму, яка дозволяє користувачу зберігати інформацію про товари у словник.
# Ключ — назва товару, а значення — ціна та кількість одиниць на складі.
# Програма повинна мати наступні опції: ✅ Додати новий товар ✅ Видалити товар
# ✅ Змінити ціну або кількість товару ✅ Переглянути список всіх товарів та їх характеристик












# Створіть словник, який містить ключ — назва книги, значення — кількість сторінок у ній.
# Напишіть програму, яка виводить на екран книгу з найбільшою кількістю сторінок.
# Вивести на екран книгу з найменшою кількістю сторінок.
# Порахувати середнє значення сторінок у всіх книгах.
# books = {
#     "Гарі Потер-1": 150,
#     "Гарі Потер-2": 125,
#     "Гарі Потер-3": 170,
#     "Гарі Потер-4": 200
# }






# Потрібно підсумувати числа, виключивши будь-які цифри, які є частиною слова.
# Текст складається з чисел, пробілів та літер з англійського алфавіту.
# my_string = "This picture is an oil on canvas painting 5 by Danish artist Anna Petersen between a1845 and 1910 year"

# words = my_string.split()
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# numbers = [float(word) for word in words if word.isdigit()]
# # print(f"Сума всіх чисел, які знаходяться у речені дорівнює {sum(numbers)}")

O_O

magic




# Створіть словник, який містить дані про ціни на різні товари у різних магазинах.
# Ключами в цьому словнику будуть назви товарів, а значеннями — словники з назвами магазинів та цінами на ці товари у цих магазинах.
# prices = {
#     "яблоко": {"магазин_1": 2.5, "магазин_2": 2.3, "магазин_3": 2.2},
#     "банан": {"магазин_1": 1.5, "магазин_2": 1.3, "магазин_3": 1.2},
#     "апельсин": {"магазин_1": 3, "магазин_2": 2.9, "магазин_3": 3.2},
# }








# Посортувати за спаданням ціни

# products = [
#     {"name": "bread", "price": 100},
#     {"name": "wine", "price": 138},
#     {"name": "meat", "price": 15},
#     {"name": "water", "price": 1},
# ]









# Напишіть програму, яка питає у користувача, що він хоче купити.
# Вивести на екран номер магазину, в якому можна купити:
# ✅ найдешевше
# ✅ найдорожче










# Порахувати кількість входження слів у речені за записати їх у словник {"що", 3}
# my_string = "Напишіть програму, яка питає у користувача, що він хоче купити. Вивести на екран номер магазину, в якому можна купити"










# Порахувати середню ціну по всіх магазинах.











# Ваша задача - знайти кут підйому сонця над горизонтом, знаючи час доби.
# Вхідні дані: сонце сходить на сході о 6:00 ранку, що відповідає куту 0 градусів.
# О 12:00 дня сонце досягає зеніту, що означає, що кут дорівнює 90 градусів. 18:00 - час заходу сонця,
# тому кут дорівнює 180 градусам.
# Якщо на вхід буде подано час ночі (до 6:00 ранку або після 6:00 вечора),
# ваша програма повинна повернути - "I don't see the sun!".