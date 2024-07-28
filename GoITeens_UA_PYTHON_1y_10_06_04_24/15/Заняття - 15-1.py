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
    "Кава",
    "Око",
    "Зараз"
]

PRODUCTS_SOLD = []
PASSWORD = ""
REVIEWS = ["Чудове обслуговування", "Такий собі продуктовий магазин", "свіжі товари", "не свіжі товари", "Чудовий магазин,не один раз вже тут купую продукти"]

COMMANDS = {
    "show all products": "Показати список наявних товарів",
    "add product": "Додати новий товар до списку",
    "add products": "Додати список товарів",
    "del prod by name": "Видалити товар за ім'ям",
    "del prod by numb": "Видалити товар за номер",
    "sort prod by name": "Відсортувати список товарів за ім'ям",
    "sold product": "Продати товар",
    "find numb prod ny name": "Знайти номер товару за ім'ям",
    "show sold product": "Показати список проданих товарів",
    "history sold": "Показати історію продажів",
    "exit": "Вийти з програми",
    "add review": "Написати відгук",
    "find repeated groups": "Знайти групи символів, які повторюються (використовуючи всі відгуки)",
    "find palindrome": "Знайти назви продуктів, які є паліндромами",
    "show reviews": "Показати відгуки",
    "add employee": "Додати нового працівника",                            #######################
    "del employee": "Видалити працівника",                                 #######################
    "show employees": "Переглянути список працівників",                      #######################
    "change salary": "Змінити заробітну плату працівника",                  #######################
    "change position": "Змінити посаду працівника",                           #######################
    "show log": "Показати лог",                                        #######################
    "show using commands": "Показати список команд та їх частоту використання",    #######################
    "help": "Показати список доступних команд"                                  ###############
}

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
USING_COMMANDS = {}   ###############

DELIMITER = "-" * 28
TEMPLATE = "|{:<5}|{:<20}|"

while not PASSWORD:
    login_global = input("Введіть свій логін користувача: ")
    if login_global in EMPLOYEES:
        PASSWORD = EMPLOYEES[login_global]["password"]
        break

    position = input("Введіть свою посаду: ")
    salary = input("Введіть свою зарплату: ")
    name = input("Введіть своє ім'я: ")
    start_date = datetime.now().strftime("%d.%m.%Y")

    EMPLOYEES[login_global] = {
        "posiotion": position,
        "salary": salary,
        "start_date": start_date,
        "name": name,
    }

    command = input("Потрібно створити пароль для можливості працювати в системі.\n"
                    "Введіть 1 - для введення свого паролю.\n"
                    "Введіть 2 - для автоматичної генерації паролю\n-> ")

    if command == "1":
        password = input("Введіть свій пароль. Довжина паролю має бути не менше 8 символіd, містити мінім одна буква та одну цифру.\n-> ")

        if len(password) >= 8:
            is_len_pass = True
        else:
            is_len_pass = False

        is_have_digit = False
        is_have_char = False

        for char in password:
            if char.isalpha():
                is_have_char = True
            elif char.isdigit():
                is_have_digit = True

        if is_len_pass and is_have_digit and is_have_char:
            PASSWORD = password
            EMPLOYEES[login_global]["password"] = PASSWORD
        else:
            input("Ваш пароль не пройшов перевірку. Спробуйте ще раз. 'Enter' для проовження ")

    elif command == "2":
        string_password = string.ascii_lowercase + string.digits

        len_password = input("Введіть довжину паролю, мінім 8 символів: ")
        if len_password.isdigit() and int(len_password) > 8:
            len_password = int(len_password)
        else:
            len_password = 8

        is_upper = input("Чи використовувати великі літери для генерації паролю: 1 - так, будь який інший символ - ні -> ")
        if is_upper == "1":
            string_password += string.ascii_uppercase

        is_punctuation = input("Чи використовувати спецсимволи для генерації паролю: 1 - так, будь який інший символ - ні -> ")
        if is_punctuation == "1":
            string_password += string.punctuation

        is_repeat = input("Чи можуть символи у паролю повторюватись. 1 - так, будь який інший символ - ні -> ")
        if is_repeat == "1":
            password = random.choices(string_password, k=len_password)
        else:
            password = random.sample(string_password, k=len_password)

        PASSWORD = "".join(password)
        EMPLOYEES[login_global]["password"] = PASSWORD

else:
    input(f"\nПароль успішно створено: '{PASSWORD}'. Запам'ятайте його. 'Enter' для продовження ")

password_input = input("\nВведіть пароль для входу у систему: ")

command = ""
while password_input == PASSWORD:
    if not command:
        LOG.append(f"Користувач з логіном '{login_global}' ввішов у систему: {datetime.now()}")
        print("Доброго дня. Вітаємо в нашій інформаційній системі")

    command = input("\nВведіть команду або введіть 'help' для допомоги: ")
    LOG.append(f"Корисчувач з логіном '{login_global}' ввів команду '{command}': {datetime.now()}")
    USING_COMMANDS[command] = USING_COMMANDS.get(command, 0) + 1

    if command == "show all products":
        print(DELIMITER)
        for i, product in enumerate(PRODUCTS, start=1):
            print(TEMPLATE.format(i, product))
        else:
            print(DELIMITER)

        input("\nНатисніть 'enter' для продовження\n")

    elif command == "add product":
        product = input("\nВведіть новий товар для додавання до списку: ")

        if product in PRODUCTS:
            input("\nТакий товар вже доданий\nНатисніть 'enter' для продовження\n")
        else:
            PRODUCTS.append(product)
            input("\nНовий товар доданий до списку\nНатисніть 'enter' для продовження\n")

    elif command == "add products":
        prods = input("\nВведіть список товарів через пробіл:\n").split()
        PRODUCTS.extend(prods)
        input("\nСписок продуктів розширено\nНатисніть 'enter' для продовження\n")

    elif command == "del prod by name":
        product = input("Введіть назву товару для видалення: ")

        if product in PRODUCTS:
            PRODUCTS.remove(product)
            input(f"\nТовар '{product}' видалено зі списку\nНатисніть 'enter' для продовження\n")
        else:
            input(f"\nТовар '{product}' відсутній у списку\nНатисніть 'enter' для продовження\n")

    elif command == "del prod by numb":
        number = input("Введіть номер товару для видалення: ")

        if number.isdigit() and 0 < int(number) <= len(PRODUCTS):
            product = PRODUCTS.pop(int(number) - 1)
            input(f"\nТовар '{product}' видалено зі списку\nНатисніть 'enter' для продовження\n")
        else:
            input("\nВвели невірний номер")

    elif command == "sort prod by name":
        prods = sorted(PRODUCTS)

        for i, prod in enumerate(prods, start=1):
            print(f"{i}: {prod}")

        input("\nСписок товарі відсортовано\nНатисніть 'enter' для продовження\n")

    elif command == "sold product":
        product = input("Введіть товар для продажу: ")

        if product in PRODUCTS:
            PRODUCTS.remove(product)
            PRODUCTS_SOLD.append(product)
            input(f"Товар '{product}' продано\nНатисніть 'enter' для продовження\n")
        else:
            input(f"Товар '{product}' відсутній у списку")

    elif command == "find numb prod ny name":
        product = input("Введіть назву товару для пошуку: ")

        if product in PRODUCTS:
            index = PRODUCTS.index(product)
            input(f"\nТовар '{product}' знаходить під номер '{index + 1}'\nНатисніть 'enter' для продовження\n")
        else:
            input(f"\nТовар '{product}' відсутній у списку")

    elif command == "show sold product":
        print("\nСписок проданий товарів\n")
        for i, product in enumerate(PRODUCTS_SOLD, start=1):
            print(f"{i}: {product}")

        input("\nНатисніть 'enter' для продовження\n")

    elif command == "history sold":
        prods_sold = PRODUCTS_SOLD[::-1]

        if not prods_sold:
            input("\nСписок проданих товарів порожній\n")

        print("\nІсторія продажу\n")
        for product in prods_sold:
            print(product)

        input("\nНатисніть 'enter' для продовження\n")

    elif command == "exit":
        print("\nДякую що були з нами. Чекаємо наступної зустрічі.\n")
        break

    elif command == "add review":
        review = input("Введіть свій відгук: ")
        REVIEWS.append(review)
        input("\nВаш відгук додано до системи.\nНатисніть 'enter' для продовження ")

    elif command == "find repeated groups":
        reviews = " ".join(REVIEWS).lower()

        repeated_chars = set()
        for i in range(len(reviews)):
            for j in range(i+1, len(reviews)):
                if reviews.count(reviews[i:j]) >= 2:
                    repeated_chars.add(reviews[i:j])

        input(f"\nГрупи символів, які повторююьюся не менше 2-х разів:\n{repeated_chars}\nНатисніть 'enter' для продовження ")

    elif command == "find palindrome":
        palin_prod = [product for product in PRODUCTS if product.lower() == product.lower()[::-1]]
        input(f"Слова-паліндроми:\n{palin_prod}\nНатисніть 'enter' для продовження ")

    elif command == "show reviews":
        for review in REVIEWS:
            print(review)

    elif command == "add employee":
        login = input("Введіть логін для користувача: ")
        position = input("Введіть посаду працівника: ")
        salary = input("Введіть ЗП для користувача: ")
        start_date = input("Введіть дату старту роботи у форматі '01.01.2024': ")
        name = input("Введіть ім'я працівника: ")
        password = input("Введіть пароль для користувача: ")

        EMPLOYEES[login] = {
            "posititon": position,
            "salary": salary,
            "start_date": start_date,
            "name": name,
            "password": password
        }
        input("Користуча успішно додано.\nНатисніть 'enter' для продовження ")

    elif command == "del employee":
        login = input("Введіть логін користувача для видалення співробітника: ")

        if login in EMPLOYEES:
            # info_user = EMPLOYEES.pop(login)
            del EMPLOYEES[login]
            input(f"Користувача '{login}' успішно видалено\nНатисніть 'enter' для продовження ")
        else:
            input("Такого користувача не знайдено\nНатисніть 'enter' для продовження ")

    elif command == "show employees":
        for employee in EMPLOYEES:
            print(f"Інформація про користувача з логіном {employee}\n")
            for key, value in EMPLOYEES[employee].items():
                print(f"{key}: {value}")
            print("\n")
        input("\nНатисніть 'enter' для продовження ")

    elif command == "change salary":
        login = input("Введіть логін користувача: ")

        if login in EMPLOYEES:
            salary = input("Введіть нове значення ЗП: ")
            EMPLOYEES[login]["salary"] = salary
            input("Суму ЗП успішно змінено\nНатисніть 'enter' для продовження ")
        else:
            input("Такого користувача не знайдено\nНатисніть 'enter' для продовження ")

    elif command == "change position":
        login = input("Введіть логін працівника: ")

        if login in EMPLOYEES:
            position = input("Введіть нову посаду: ")
            EMPLOYEES[login]["position"] = position
            input("Посаду користувача успішно змінено\nНатисніть 'enter' для продовження ")
        else:
            input("Такого користувача не знайдено\nНатисніть 'enter' для продовження ")

    elif command == "help":
        pprint(COMMANDS, width=200)

    elif command == "show log":
        pprint(LOG, width=100)

    elif command == "show using commands":
        for command, count in USING_COMMANDS.items():
            print(f"Команда '{command}' використана таку кількість разів: {count}")

    else:
        input("\nНевідома команда. Спробуйте ще раз\nНатисніть 'enter' для продовження ")

else:
    print("\nПароль введено не вірно. Доступ заборонено.")