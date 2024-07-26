import string
import random
from datetime import datetime
from pprint import pprint


PRODUCTS = [
    "Гречка",
    "Макарони",
    "Спагеті",
    "Картопля",
    "Буряк",
    "Морква",
    "Капуста",
    "Цибуля",
    "Часник",
    "Борошно",
    "Яйця",
    "Соняшникова олія",
    "Вершкове масло",
    "Сіль",
    "Перець",
    "Цукор",
    "Оцет",
    "Сода",
    "Чай",
    "Кава"
]
PRODUCTS_SOLD = []
COMMANDS = {
    "show all": "Показати список наявних товарів",
    "add prod": "Додати новий товар до списку",
    "add prods": "Додати список товарів",
    "del prod for name": "Видалити товар за ім'ям",
    "del prod for num": "Видалити товар за номер",
    "sort": "Показати відсортований список товарів за ім'ям",
    "sold prod": "Продати товар",
    "find prod for name": "Знайти номер товару за ім'ям",
    "show sold prods": "Показати список проданих товарів",
    "show history": "Показати історію продажів",
    "exit": "Вийти з програми",
    "add review": "Написати відгук",
    "find dublicate char": "Знайти групи символів, які повторюються (використовуючи всі відгуки)",
    "palindrome": "Знайти продукти, які є паліндромами",
    "add employee": "Додати нового працівника",                            #######################
    "del employee": "Видалити працівника",                                 #######################
    "show employees": "Переглянути список працівників",                      #######################
    "change salary": "Змінити заробітну плату працівника",                  #######################
    "change position": "Змінити посаду працівника",                           #######################
    "show log": "Показати лог",                                        #######################
    "show using commands": "Показати список команд та їх частоту використання",    #######################
    "help": "Показати список доступних команд"                                  ###############
}
LOGIN = ""
PASSWORD = ""
REVIEWS = []
DELIMETER = "-" * 93
TEMPLATE = "|{:<20}|{:<70}|"

EMPLOYEES = {                    #############################
    "andrew": {
        "position": "Менеджер",
        "salary": 30000,
        "start_date": "22.02.2024",
        "name": "Андрій",
        "password": "1234567a"
    },
    "dima": {
        "position": "Продавець",
        "salary": 14000,
        "start_date": "10.03.2024",
        "name": "Дмитро",
        "password": "1234567b"
    }
}
LOG = []              ###############
USING_COMMANDS = {}

while not PASSWORD:
    LOGIN = input("Введіть свій логін: ")         ###################
    if LOGIN in EMPLOYEES:
        PASSWORD = EMPLOYEES[LOGIN]["password"]
        break

    position = input("Введіть посаду працівника: ")
    salary = input("Введіть ЗП: ")
    name = input("Введіть ім'я працівника: ")

    EMPLOYEES[LOGIN] = {
        "position": position,
        "salary": salary,
        "name" : name,
        "start_date": datetime.now().strftime("%d.%m.%Y")
    }

    command = input("\nВведіть 1 для введення свого паролю.\n"
                    "Введіть 2 для автоматичного створення паролю.\n"
                    "Введіть будь який інший символ для виходу з програми: ")

    if command == "1":
        password = input("Введіть свій пароль. Пароль повинен містити не менше 8 символів, містити принаймні одну літеру та одну цифру\n-> ")

        pass_len = True if len(password) >= 8 else False
        pass_alpha = False
        pass_digit = False

        for char in password:
            if char.isalpha():
                pass_alpha = True
            elif char.isdigit():
                pass_digit = True

        if pass_len and pass_alpha and pass_digit:
            PASSWORD = password
            EMPLOYEES[LOGIN]["password"] = PASSWORD
        else:
            input("\nПароль не пройшов перевірку. Спробуйте ще раз")

    elif command == "2":
        chars_for_pass = string.ascii_lowercase + string.digits

        len_password = input("Введіть довжину пароль не меншу 8, або залиште за замовчуванням (8 символів): ")
        len_password = int(len_password) if len_password.isdigit() and int(len_password) >= 8 else 8

        is_upper = input("Чи використовути великі літери? Введіть 1 - так, будь який інший символ ні: ")
        chars_for_pass += string.ascii_uppercase if is_upper == "1" else ""

        is_punctuation = input("Чи використовути спецсимволи? Введіть 1 - так, будь який інший символ ні: ")
        chars_for_pass += string.punctuation if is_punctuation == "1" else ""

        is_repeate = input("Чи можуть символи паролю повторюватись? 1 - так, будь який інший символ - ні: ")
        password = [] if is_repeate == "1" else set()
        pass_alpha = False
        pass_digit = False

        while len(password) < len_password or not pass_alpha or not pass_digit:
            char = random.choice(chars_for_pass)
            if char.isalpha():
                pass_alpha = True
            elif char.isdigit():
                pass_digit = True

            if isinstance(password, list):
                password.append(char)
            elif isinstance(password, set):
                password.add(char)
        else:
            PASSWORD = "".join(password)
            EMPLOYEES[LOGIN]["password"] = PASSWORD

    else:
        print("Ви вийшли з програми")
        break
else:
    input(f"Пароль успіщно створено '{PASSWORD}'. Запам'ятайте його. Натисніть 'enter' для продовження\n")

password_input = input("Введіть пароль для входу в систему: ")    ###########

command = None
while password_input == PASSWORD:        #############
    if not command:
        LOG.append(f"Користувач '{LOGIN}' увійшов у систему: {datetime.now()}")
        input("\nПароль введено вірно. Вітаємо нашій інформаційній системі.\n")

    command = input("Введіть номер команди або введіть 'help' для отримання списку доступних команд: ")
    LOG.append(f"Користувач '{LOGIN}' ввів команду '{command}': {datetime.now()}")

    if command in USING_COMMANDS:
        USING_COMMANDS[command] += 1
    else:
        USING_COMMANDS[command] = 1

    if command == "show all":
        print(DELIMETER)
        print(TEMPLATE.format("№", "Назва товару"))
        print(DELIMETER)
        for i, product in enumerate(PRODUCTS, start=1):
            print(TEMPLATE.format(i, product))
        print(DELIMETER)

        input("\nНатисніть 'Enter' для продовження ")

    elif command == "add prod":
        product = input("Введіть новий товар для додавання до списку: ")

        if product not in PRODUCTS:
            PRODUCTS.append(product)
            input(f"\nТовар '{product}' доданий до списку. Натисніть 'Enter' для продовження ")
        else:
            input("\nТакий товар вже є у списку. Натисніть 'Enter' для продовження ")

    elif command == "add prods":
        prods = input("Введіть список товар для додавання через пробіл\n-> ")
        prods = prods.split()
        PRODUCTS.extend(prods)
        input("\nСписок товарів розширено. Натисніть 'Enter' для продовження ")

    elif command == "del prod for name":
        product = input("Введіть назву товару для видалення зі списку товарів: ")

        if product in PRODUCTS:
            PRODUCTS.remove(product)
            input(f"\nТовар '{product}' видалено зі списку. Натисніть 'Enter' для продовження ")
        else:
            input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")

    elif command == "del prod for num":
        index = input("Введіть номер товару для видалення: ")

        if index and index.isdigit() and 0 < int(index) <= len(PRODUCTS):
            product = PRODUCTS.pop(int(index) - 1)
            input(f"Товар '{product}' видалено. Натисніть 'Enter' для продовження ")
        else:
            input("Ви ввели не вірний номер товару. Натисніть 'Enter' для продовження ")

    elif command == "sort":
        print()
        prods = sorted(PRODUCTS)
        for product in prods:
            print(product)

        input("\nНатисніть 'Enter' для продовження ")

    elif command == "sold prod":
        product = input("Введіть назву товару для продажу: ")

        if product in PRODUCTS:
            PRODUCTS.remove(product)
            PRODUCTS_SOLD.append(product)
            input(f"\nТовар '{product}' продано. Натисніть 'Enter' для продовження ")
        else:
            input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")

    elif command == "show prod for name":
        product = input("Введіть назву товару для пошуку: ")

        if product in PRODUCTS:
            index = PRODUCTS.index(product)
            input(f"Товар '{product}' знаходиться під номером {index + 1}. Натисніть 'Enter' для продовження ")
        else:
            input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")

    elif command == "show sold prods":
        if not PRODUCTS_SOLD:
            print("Список проданих товарів пустий")

        for product in PRODUCTS_SOLD:
            print(product)

        input("\nНатисніть 'Enter' для продовження ")

    elif command == "shwo history":
        prods_sold = PRODUCTS_SOLD[::-1]
        for product in prods_sold:
            print(product)

        input("\nНатисніть 'Enter' для продовження ")

    elif command == "exit":
        print("До побачення")
        break

    elif command == "add review":
        review = input("Залиште свій відгук\n->")
        REVIEWS.append(review)
        input("Ваш відгук успішно збережено.\nНатисніть 'Enter' для продовження ")

    elif command == "find dublicate char":
        reviews = " ".join(REVIEWS).lower()

        # repeated_groups = {reviews[i:j] for i in range(len(reviews)) for j in range(i+1, len(reviews)) if reviews.count(reviews[i:j]) >= 2}

        repeated_groups = set()
        for i in range(len(reviews)):
            for j in range(i+1, len(reviews)):
                if reviews.count(reviews[i:j]) >= 2:
                    repeated_groups.add(reviews[i:j])

        input(f"Групи символів, які повторюються не менше двох разів у відгуках:\n{repeated_groups}\n")

    elif command == "palindrome":
        palin_prods = [product for product in PRODUCTS if product.lower() == product[::-1].lower()]
        input(f"\nУ списку з продуктами є такі слова-паліндроми: {palin_prods}\n")

    elif command == "add employee":
        login = input("Введіть логін для користувача: ")
        if login in EMPLOYEES:
            input("\nКористувач із таким логіном вже зареєстрований.\nНатисніть 'enter' для продовження ")
            continue

        position = input("Введіть посаду працівника: ")
        salary = int(input("Введіть ЗП: "))
        name = input("Введіть ім'я працівника: ")
        start_date = input("Введіть дату початку роботи у форматі '01.01.2024': ")
        password = input("Створіть пароль для працівника: ")

        EMPLOYEES[login] = {
            "position": position,
            "salary": salary,
            "name" : name,
            "start_date": start_date,
            "password": password
        }

        input("\nКористувача успішно створено.\nНатисніть 'enter' для продовження ")

    elif command == "del employee":
        login = input("Введіть логін користавача: ")
        if login in EMPLOYEES:
            del EMPLOYEES[login]
            # EMPLOYEES.pop(login)
            input("\nКористувача успішно видалено.\nНатисніть 'enter' для продовження ")
        else:
            input("\nКористувача з таким логіном не знайдено.\nНатисніть 'enter' для продовження ")

    elif command == "show employees":
        for login, employee_info in EMPLOYEES.items():
            print(f"'{employee_info['name']}' зареєстрований під логіном '{login}' почав свою роботу '{employee_info['start_date']}'")
        input("\nНатисніть 'enter' для продовження ")

    elif command == "change salary":
        login = input("Введіть логін користувача: ")
        if login in EMPLOYEES:
            print(f"\nПоточне значення ЗП у користувача з логіном '{login}' {EMPLOYEES[login]['salary']}\n")
            EMPLOYEES[login]["salary"] = input("Введіть нове значення ЗП: ")
            input(f"\nКористувачу з логіном '{login}' успішно змінено ЗП.\nНатисніть 'enter' для продовження ")
        else:
            input("\nКористувача з таким логіном не знайдено.\nНатисніть 'enter' для продовження ")

    elif command == "change position":
        login = input("Введіть логін користувача: ")
        if login in EMPLOYEES:
            print(f"\nПоточна посада працівника '{EMPLOYEES[login]['position']}'")
            EMPLOYEES[login]["position"] = input("Введіть нову посаду: ")
            input("\nПосаду працівника успішно змінено.\nНатисніть 'enter' для продовження ")
        else:
            input("\nКористувача з таким логіном не знайдено.\nНатисніть 'enter' для продовження ")

    elif command == "help":
        print(DELIMETER)
        print(TEMPLATE.format("Command", "Discription"))
        print(DELIMETER)
        for key, value in COMMANDS.items():
            print(TEMPLATE.format(key, value))
        print(DELIMETER)

    elif command == "show log":
        pprint(LOG)

    elif command == "show using commands":
        pprint(USING_COMMANDS)

    else:
        input("\nНевідома команда.\nНатисніть 'enter' для продовження ")

else:
    print("Не вірний пароль. Доступ заборонено. До побачення")