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
"find prod by name": "Знайти номер товару за ім'ям",
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
DELIMETER = "-" * 28
TEMPLATE = "|{:<5}|{:<20}|"


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


def palindrome(products: list) -> None:
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


def is_verify_password(password: str) -> bool:
    pass_len = True if len(password) >= 8 else False
    pass_alpha = False
    pass_digit = False

    for char in password:
        if char.isalpha():
            pass_alpha = True
        elif char.isdigit():
            pass_digit = True

    return True if all(pass_len, pass_alpha, pass_digit) else False


def generate_password(
    len_password: int = 8,
    is_upper: bool = False,
    is_punctuation: bool = False,
    is_repeate: bool = True
) -> str:

    chars_for_pass = string.ascii_lowercase + string.digits
    chars_for_pass += string.ascii_uppercase if is_upper else ""
    chars_for_pass += string.punctuation if is_punctuation else ""

    password = random.choices(chars_for_pass, k=len_password) if is_repeate else random.sample(chars_for_pass, k=len_password)
    return "".join(password)


def main():
    login = input("Введіть свій логін: ")
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
    password = employees.get(login, {}).get("password", "")

    while not password:
        position = input("Введіть посаду працівника: ")
        salary = input("Введіть ЗП: ")
        name = input("Введіть ім'я працівника: ")

        employees[login] = {
            "position": position,
            "salary": salary,
            "name" : name,
            "start_date": datetime.now().strftime("%d.%m.%Y")
        }

        command = input("\nВведіть 'create' для введення свого паролю.\n"
                        "Введіть 'generate' для автоматичного створення паролю.\n"
                        "Введіть будь який інший символ для виходу з програми: ")

        if command == "create":
            password = input("Введіть свій пароль. Пароль повинен містити не менше 8 символів, містити принаймні одну літеру та одну цифру\n-> ")

        elif command == "generate":
            len_password = input("Введіть довжину пароль не меншу 8, або залиште за замовчуванням (8 символів): ")
            len_password = int(len_password) if len_password.isdigit() and int(len_password) >= 8 else 8

            is_upper = True if input("Чи використовути великі літери? Введіть 1 - так, будь який інший символ ні: ") == "1" else False
            is_punctuation = True if input("Чи використовути спецсимволи? Введіть 1 - так, будь який інший символ ні: ") == "1" else False
            is_repeate = True if input("Чи можуть символи паролю повторюватись? 1 - так, будь який інший символ - ні: ") == "1" else False


            password = generate_password(
                len_password=len_password,
                is_punctuation=is_punctuation,
                is_upper=is_upper,
                is_repeate=is_repeate
            )

        else:
            print("Ви вийшли з програми")
            break

        if is_verify_password(password):
            employees[login]["password"] = password
            break
        else:
            input("\nПароль не пройшов перевірку. Спробуйте ще раз")

    input(f"Ваш пароль '{password}'. Запам'ятайте його. Натисніть 'enter' для продовження\n")
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
    log = []
    using_commands = {}
    reviews = []

    password_input = input("Введіть пароль для входу в систему: ")

    command = None
    while password == password_input:
        if not command:
            log.append(f"Користувач '{login}' увійшов у систему: {datetime.now()}")
            input("\nПароль введено вірно. Вітаємо нашій інформаційній системі.\n")

        command = input("Введіть команду або введіть 'help' для отримання списку доступних команд: ")
        log.append(f"Користувач '{login}' ввів команду '{command}': {datetime.now()}")
        using_commands[command] = using_commands.get(command, 0) + 1

        match command:
            case "show prods":
                show_prods(products)
            case "add prod":
                products = add_prod(products)
            case "add prods":
                products = add_prods(products)
            case "del prod by name":
                products = del_prod_by_name(products)
            case "del prod by num":
                products = del_prod_by_num(products)
            case "sort":
                sort(products)
            case "sold prod":
                products, products_sold = sold_prod(products, products_sold)
            case "find prod by name":
                find_prod_by_name(products)
            case "show sold prods":
                show_prods(products_sold)
            case "show history":
                show_history(products_sold)
            case "exit":
                exit()
            case "add review":
                reviews = add_review(reviews)
            case "find dublicate char":
                find_dublicate_char(reviews)
            case "palindrome":
                palindrome(products)
            case "add employee":
                employees = add_employee(employees)
            case "del employee":
                employees = del_employee(employees)
            case "show employees":
                show_employees(employees)
            case "change salary":
                employees = change_salary(employees)
            case "change position":
                employees = change_position(employees)
            case "show log":
                show_log(log)
            case "show using commands":
                show_using_commands(using_commands)
            case "help":
                help()
            case _:
                unknown_command()
    else:
        print("Не вірний пароль. Доступ заборонено. До побачення")


if __name__ == "__main__":
    main()