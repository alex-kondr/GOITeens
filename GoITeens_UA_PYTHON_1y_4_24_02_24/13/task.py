# transport = {
#     'AA1111AA': 'Іванов Іван',
#     'IVANOV'  : 'Іванов Іван',
#     'AA0007AA': 'Семенов Андрій',
#     'AA007AA' : 'Іванов Іван',
#     'AВ1111AВ': 'Вінниця Водоканал',
#     'AІ1010КК': 'Семенов Андрій',
# }

# for key in transport:
#     print(f"{key = }")

# for number in transport.keys():
#     print(f"{number = }")

# for name in transport.values():
#     print(name)

# for number, name in transport.items():
#     print(f"{number = }, {name = }")

# for item in transport.items():
#     print(f"{item = }")






# Оголосити словник, що має наступну структуру «ключ» — номерний знак транспортного засобу
# (наприклад «АА2565ІН»), значення «власник авто» (наприклад, Іванов Іван)
# Додати в словник два нові авто
# Знайти власника за номером автомобіля
# Обійти словник і вивести прізвища людей, які мають більше одного авто

# transport = {
#     'AA1111AA': 'Іванов Іван',
#     'IVANOV'  : 'Іванов Іван',
#     'AA0007AA': 'Семенов Андрій',
#     'AA007AA' : 'Іванов Іван',
#     'AВ1111AВ': 'Вінниця Водоканал',
#     'AІ1010КК': 'Семенов Андрій',
#     'AB0212KK': 'Семенов Андрій',
# }

# transport["ОО4567ДД"] = "Олександр"
# print(transport["AA007AA"])
# print(transport.get("AA007AЛ", "Такий номерний знак відсутній у нашому словнику"))

# names = [name for name in transport.values()]
# names_ = set()

# for name in names:
#     if names.count(name) > 1:
#         names_.add(name)

# print(names_)




# Створіть словник “stock”, який міститиме в собі ключ — назва товару,
# значення — кількість товару на складі.
# Написати програму, яка запитує який товар та кількість, яку хоче купити користувач.
# Вивести на екран True, якщо користувач може купити цей товар, якщо ні — False.

# stock = {
#     "Яблоко": 50,
#     "Хліб": 10,
#     "Картопля": 150,
#     "Сир": 5
# }

# product = input("Введіть назву товару для покупки: ")
# count_product = float(input("Введіть кількість товару, який бажаєте купити: "))

# if stock.get(product):
#     print("Такий товар присутній")
#     count = stock.get(product)

#     if count_product <= count:
#         print("Є необхідна кількість товару")
#     else:
#         print("Відсутня така кількість товару")
# else:
#     print("Такий товар відсутній")





# Створіть словник, який містить дані про користувачів вашого веб-сайту.
# Ключами в цьому словнику будуть імена користувачів, а значеннями — інформація про користувачів.
# Попросіть користувача ввести імена користувачів, про яких хоче дізнатися інформацію, через пробіл.
# Вивести інформацію про цих користувачів у форматі (Ім’я, вік, стать, електронна пошта).

# users = {
#     "alex": {
#         "Ім'я": "Олександр",
#         "Вік": 17,
#         "Стать": "Чоловіча",
#         "e-mail": "alex@gmail.com"
#     },
#     "user": {
#         "Вік": 25,
#         "e-mail": "user@gmail.com"
#     },
#     "lev": {
#         "Ім'я": "Лев",
#         "Вік": 14,
#         "Стать": "Чоловіча"
#     }
# }

# print(users.get("alex", {}).get("Ім'я", "Дані відсутні"))
# print(users.get("user", {}).get("Ім'я", "Дані відсутні"))
# print(users["alex"]["СТать"])

# users_input = input("Введіть імена користувачів через пробіл:\n").split()
# for user in users_input:
#     print(users.get(user, f"Користувач '{user}' відсутній"))




# Створіть словник, який містить ключ — ім’я студента, значення — список із балами.
# Попросіть користувача ввести ім’я студента.
# Порахувати середній бал студента, ім’я якого ввів користувач.
# math_scores = {
#     "Олександр": [8, 9, 7, 9, 6],
#     "Андрій": [10, 7, 9, 10, 10],
#     "Олег": [6, 7, 6, 9, 6]
# }

# name = input("Введіть ім'я студента: ")

# summ = 0
# count = 0
# for score in math_scores.get(name, []):
#     summ += score
#     count += 1

# avg = summ / count
# print(avg)

# scores = math_scores.get(name, [])
# avg = sum(scores) / len(scores) if scores else 0
# print(avg)






# Створіть словник, який містить ключ — ім’я студента, значення — список із балами.
# Напишіть програму, яка порахує середній бал усіх учнів та виведе його на екран.
# math_scores = {
#     "Олександр": [8, 9, 7, 9, 6],
#     "Андрій": [10, 7, 9, 10, 10],
#     "Олег": [6, 7, 6, 9, 6]
# }

# suma = 0
# len_score = 0
# for val in math_scores.values():
#     suma += sum(val)
#     len_score += len(val)

# print(round(suma / len_score, 2))







# Напишіть програму, яка дозволяє користувачу зберігати інформацію про товари у словник.
# Ключ — назва товару, а значення — ціна та кількість одиниць на складі.
# Програма повинна мати наступні опції: ✅ Додати новий товар ✅ Видалити товар
# ✅ Змінити ціну або кількість товару ✅ Переглянути список всіх товарів та їх характеристик

# products = {}

# while True:
#     command = input("Введіть команду:\n'add' - додати новий товар, 'del' - видалити товар\n'change' - змінити інформацію про товар, 'show' - показати всі товари-> ")

#     if command == "add":
#         name = input("Введіть назву товару: ")
#         price, count = input("Введіть ціну товару та кількість через пробіл: ").split()

#         products[name] = {"Ціна": float(price), "Кількість": int(count)}

#     elif command == "del":
#         name = input("Введіть назву товару: ")

#         if name in products:
#             products.pop(name)
#         else:
#             input("Такий товар відсутній")

#     elif command == "change":
#         name = input("Введіть назву товару: ")

#         product = products.get(name)
#         if product:
#             info = input("Введіть 'Ціна' - для зміни ціни товару, 'Кількість' - для зміни кількості: ")
#             value = float(input("Введіть нове значення: "))
#             if info in product:
#                 product[info] = value
#             else:
#                 input("Невідомий параметр")
#         else:
#             input("Такий товар відсутній")

#     elif command == "show":
#         for product, value in products.items():
#             print(f"\nНазва товару: {product}, Інформація про товар: {value}\n")

#         if not products:
#             print("\nСписок товарів пустий\n")








# Створіть словник, який містить ключ — назва книги, значення — кількість сторінок у ній.
# Напишіть програму, яка виводить на екран книгу з найбільшою кількістю сторінок.
# Вивести на екран книгу з найменшою кількістю сторінок.
# Порахувати середнє значення сторінок у всіх книгах.
books = {
    "Гарі Потер-1": 150,
    "Гарі Потер-2": 125,
    "Гарі Потер-3": 170,
    "Гарі Потер-4": 200

}

# book = ""
# count_ = 0
# for name, count in books.items():
#     if count_ < count:
#         book = name
#         count_ = count

# print(f"Книга з найбільшою кількості сторінок має назву {book} та містіть таку кільксть сторінок: {count_}")

# book = max(books, key=books.get)
# print(f"Книга з найбільшою кількості сторінок має назву {book} та містіть таку кільксть сторінок: {books[book]}")

# letters = [books[name] for name in books]
# avg = sum(letters) / len(letters)
# print(f"Середня кількість сторінок дорівнює {avg}")


# Потрібно підсумувати числа, виключивши будь-які цифри, які є частиною слова.
# Текст складається з чисел, пробілів та літер з англійського алфавіту.
# my_string = "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"










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