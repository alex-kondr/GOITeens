import string
import random
from datetime import datetime
from pprint import pprint


HELP = """
"show prods": "Показати список наявних товарів",
"add prod": "Додати новий товар до списку",
"add prods": "Додати список товарів",
"del prod by name": "Видалити товар за ім'ям",
"del prod by num": "Видалити товар за номер",
"sort": "Показати відсортований список товарів за ім'ям",
"sold prod": "Продати товар",
"find by for name": "Знайти номер товару за ім'ям",
"show sold prods": "Показати список проданих товарів",
"show history": "Показати історію продажів",
"exit": "Вийти з програми",
"add review": "Написати відгук",
"find dublicate char": "Знайти групи символів, які повторюються (використовуючи всі відгуки)",
"palindrome": "Знайти продукти, які є паліндромами",
"add employee": "Додати нового працівника",
"del employee": "Видалити працівника",
"show employees": "Переглянути список працівників",
"change salary": "Змінити заробітну плату працівника",
"change position": "Змінити посаду працівника",
"show log": "Показати лог",
"show using commands": "Показати список команд та їх частоту використання",
"help": "Показати список доступних команд"
"""
DELIMETER = "-" * 93
TEMPLATE = "|{:<20}|{:<70}|"


def show_prods(products: list) -> None:
    print(DELIMETER)
    print(TEMPLATE.format("№", "Назва товару"))
    print(DELIMETER)
    for i, product in enumerate(products, start=1):
        print(TEMPLATE.format(i, product))
    print(DELIMETER)


def add_prod(products: list) -> list:
    product = input("Введіть новий товар для додавання до списку: ")

    if product not in products:
        products.append(product)
        print(f"\nТовар '{product}' доданий до списку")
    else:
        print("\nТакий товар вже є у списку")

    return products


def add_prods(products: list) -> list:
    prods = input("Введіть список товар для додавання через пробіл\n-> ")
    prods = prods.split()
    products.extend(prods)
    print("\nСписок товарів розширено")
    return products


def del_prod_by_name(products: list) -> list:
    product = input("Введіть назву товару для видалення зі списку товарів: ")

    if product in products:
        products.remove(product)
        print(f"\nТовар '{product}' видалено зі списку")
    else:
        print("\nТакого товару немає у списку")

    return products


def del_prod_by_num(products: list[str]) -> list[str]:
    index = input("Введіть номер товару для видалення: ")

    if index and index.isdigit() and 0 < int(index) <= len(products):
        product = products.pop(int(index) - 1)
        print(f"Товар '{product}' видалено ")
    else:
        print("Ви ввели не вірний номер товару")

    return products


def sort(products: list) -> None:
    print()
    prods = sorted(products)
    for product in prods:
        print(product)


def sold_prod(products: list, products_sold: list) -> tuple[list[str]]:
    product = input("Введіть назву товару для продажу: ")

    if product in products:
        products.remove(product)
        products_sold.append(product)
        print(f"\nТовар '{product}' продано")
    else:
        print("\nТакого товару немає у списк")

    return products, products_sold


def find_prod_by_name(products: list) -> None:
    product = input("Введіть назву товару для пошуку: ")

    if product in products:
        index = products.index(product)
        print(f"Товар '{product}' знаходиться під номером {index + 1}")
    else:
        print("\nТакого товару немає у списку")


def show_sold_prods(products_sold: list) -> None:
    if not products_sold:
        print("Список проданих товарів пустий")

    for product in products_sold:
        print(product)


def show_history(products_sold: list) -> None:
    prods_sold = products_sold[::-1]
    for product in prods_sold:
        print(product)


def exit() -> None:
    print("До побачення")
    quit()


def add_review(reviews: list) -> list:
    review = input("Залиште свій відгук\n->")
    reviews.append(review)
    print("Ваш відгук успішно збережено.")
    return reviews


def find_dublicate_char(reviews: list) -> None:
    reviews = " ".join(reviews).lower()

    repeated_groups = set()
    for i in range(len(reviews)):
        for j in range(i+1, len(reviews)):
            if reviews.count(reviews[i:j]) >= 2:
                repeated_groups.add(reviews[i:j])

    print(f"Групи символів, які повторюються не менше двох разів у відгуках:\n{repeated_groups}\n")


def palindrome(products: list):
    palin_prods = [product for product in products if product.lower() == product[::-1].lower()]
    print(f"\nУ списку з продуктами є такі слова-паліндроми: {palin_prods}\n")


def add_employee(employees: dict) -> dict:
    login = input("Введіть логін для користувача: ")
    if login in employees:
        print("\nКористувач із таким логіном вже зареєстрований")

    else:
        position = input("Введіть посаду працівника: ")
        salary = int(input("Введіть ЗП: "))
        name = input("Введіть ім'я працівника: ")
        start_date = input("Введіть дату початку роботи у форматі '01.01.2024': ")
        password = input("Створіть пароль для працівника: ")

        employees[login] = {
            "position": position,
            "salary": salary,
            "name" : name,
            "start_date": start_date,
            "password": password
        }

    return employees


def del_employee(employees: dict) -> dict:
    login = input("Введіть логін користавача: ")
    if login in employees:
        del employees[login]
        print("\nКористувача успішно видалено.")
    else:
        print("\nКористувача з таким логіном не знайдено.")

    return employees


def show_employees(employees: dict) -> None:
    for login, employee_info in employees.items():
        print(f"'{employee_info['name']}' зареєстрований під логіном '{login}' почав свою роботу '{employee_info['start_date']}'")


def change_salary(employees: dict) -> dict:
    login = input("Введіть логін користувача: ")
    if login in employees:
        print(f"\nПоточне значення ЗП у користувача з логіном '{login}' {employees[login]['salary']}\n")
        employees[login]["salary"] = input("Введіть нове значення ЗП: ")
        print(f"\nКористувачу з логіном '{login}' успішно змінено ЗП.")
    else:
        print("\nКористувача з таким логіном не знайдено.")

    return employees


def change_position(employees: dict) -> dict:
    login = input("Введіть логін користувача: ")
    if login in employees:
        print(f"\nПоточна посада працівника '{employees[login]['position']}'")
        employees[login]["position"] = input("Введіть нову посаду: ")
        print("\nПосаду працівника успішно змінено.")
    else:
        print("\nКористувача з таким логіном не знайдено.")

    return employees


def help() -> None:
    print(HELP)


def show_log(log: list) -> None:
    pprint(log)


def show_using_commands(using_commands: dict) -> None:
    pprint(using_commands)


def unknown_command() -> None:
    print("\nНевідома команда. Спробуйте іншу команду.\n")


while not PASSWORD:
    LOGIN = input("Введіть свій логін: ")
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

password_input = input("Введіть пароль для входу в систему: ")


def main():
    products = [
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
    products_sold = []
    login = ""
    log = []
    using_commands = {}
    reviews = []
    employees = {
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

    command = None
    while password:
        if not command:
            log.append(f"Користувач '{login}' увійшов у систему: {datetime.now()}")
            input("\nПароль введено вірно. Вітаємо нашій інформаційній системі.\n")

        command = input("Введіть номер команди або введіть 'help' для отримання списку доступних команд: ")
        log.append(f"Користувач '{login}' ввів команду '{command}': {datetime.now()}")
        using_commands[command] = using_commands.get(command, 0) + 1

        match command:
            case "show prods":
                show_prods(products)

    else:
        print("Не вірний пароль. Доступ заборонено. До побачення")