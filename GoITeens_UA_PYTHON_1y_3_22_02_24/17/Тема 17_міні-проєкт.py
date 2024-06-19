import string
import random
from datetime import datetime
from pprint import pprint


HELP = """
"show all prods": "Показати список наявних товарів",
"add prod": "Додати новий товар до списку",
"add prods": "Додати список товарів",
"del prod by name": "Видалити товар за ім'ям",
"del prod by numb": "Видалити товар за номер",
"show sorted prods": "Показати відсортований список товарів за ім'ям",
"sold prod": "Продати товар",
"find numb prod by name": "Знайти номер товару за ім'ям",
"show sold prods": "Показати список проданих товарів",
"show sales history": "Показати історію продажів",
"exit": "Вийти з програми",
"add review": "Написати відгук",
"find repeated chars": "Знайти групи символів, які повторюються (використовуючи всі відгуки)",
"find palidrome": "Знайти продукти, які є паліндромами",
"add employee": "Додати нового працівника",
"del employee": "Видалити працівника",
"show employees": "Переглянути список працівників",
"change salary": "Змінити заробітну плату працівника",
"change position": "Змінити посаду працівника",
"show log": "Показати лог",
"show most using commands": "Показати список команд та їх частоту використання"
"""
TEMPLATE = "|{:^5}|{:<30}|"
DELIMITER = "—" * 38
HEAD = TEMPLATE.format("№", "Назва товару")


def is_verify_password(password: str) -> bool:
    pass_len = False if len(password) < 8 else True
    pass_digit = False
    pass_char = False

    for char in password:
        if char.isdigit():
            pass_digit = True
        if char.isalpha():
            pass_char = True

    return True if all([pass_len, pass_digit, pass_char]) else False


def generate_password(
    len_password: int = 8,
    is_punctuation: bool = False,
    is_upper: bool = False,
    is_repeate : bool = True
) -> str:

    pass_chars = string.ascii_lowercase + string.digits
    pass_chars += string.ascii_uppercase if is_upper else ""
    pass_chars += string.punctuation if is_punctuation else ""
    password = random.choices(pass_chars, k=len_password) if is_repeate else random.sample(pass_chars, k=len_password)
    return "".join(password)


def help():
    print(HELP)


def show_all_prods(products: list) -> None:
    print(DELIMITER)
    print(HEAD)
    print(DELIMITER)
    for i, product in enumerate(products, start=1):
        print(TEMPLATE.format(i, product))

    print(DELIMITER)


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


def del_prod_by_numb(products: list) -> list:
    index = input("Введіть номер товару для видалення: ")

    if index and index.isdigit() and 0 < int(index) <= len(products):
        product = products.pop(int(index) - 1)
        print(f"Товар '{product}' видалено")
    else:
        print("Ви ввели не вірний номер товару")

    return products


def show_sorted_prods(products: list) -> None:
    prods = sorted(products)
    for product in prods:
        print(product)


def sold_prod(products: list, products_sold: list) -> tuple[list, list]:
    product = input("Введіть назву товару для продажу: ")

    if product in products:
        products.remove(product)
        products_sold.append(product)
        print(f"\nТовар '{product}' продано. Натисніть 'Enter' для продовження ")
    else:
        print("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")

    return products, products_sold


def find_numb_prod_by_name(products: list) -> None:
    product = input("Введіть назву товару для пошуку: ")

    if product in products:
        index = products.index(product)
        print(f"Товар '{product}' знаходиться під номером {index + 1}.")
    else:
        print("\nТакого товару немає у списку.")


def show_sold_prods(products_sold: list) -> None:
    if not products_sold:
        print("Список проданих товарів пустий")

    for product in products_sold:
        print(product)


def show_sales_history(products_sold: list) -> None:
    prods_sold = products_sold[::-1]
    for product in prods_sold:
        print(product)


def exit() -> None:
    print("До побачення")
    quit()


def add_review(reviews: list) -> list:
    review = input("Залиште свій відгук:\n")
    reviews.append(review)


def find_repeated_chars(reviews: list) -> None:
    reviews = " ".join(reviews)

    repeated_groups = set()
    for i in range(len(reviews)):
        for j in range(i+1, len(reviews)):
            slice = reviews[i:j]
            if reviews.count(slice) >= 2:
                repeated_groups.add(slice)

    print(f"Список груп символів, які повторюються не менше 2 разів:\n{repeated_groups}")


def find_palidrome(products: list) -> None:
    palin_prod = []
    for product in products:
        if product.lower() == product[::-1].lower():
            palin_prod.append(product)

    message = f"В списку товарів є такі слова-паліндроми:\n{palin_prod}" if palin_prod else "В списку товарів відсутні слова паліндроми."
    print(message)


def add_employee(employees: dict) -> dict:
    username = input("Введіть логін користувача: ")
    name = input("Введіть ім'я працівника: ")
    position = input("Введіть посаду працівника: ")
    salary = input("Введіть ЗП: ")
    start_date = input("Введіть дату початку роботи у форматі '01.01.2024': ")
    password = input("Введіть пароль для працівника: ")

    if username not in employees:
        employees[username] = {
            "position": position,
            "salary": salary,
            "name": name,
            "start_date": start_date,
            "password": password
        }
        print("Працівника успішно зареєстровано в системі.")
    else:
        print("Такий логін вже зареєстрований в системі.")

    return employees


def del_employee(employees: dict) -> dict:
    username = input("Введіть логін працівника для видалення: ")
    if username in employees:
        del employees[username]
        print(f"Користувача з логіном '{username}' успішно видалено.")
    else:
        print("Такого користувача немає в системі.")

    return employees


def show_employees(employees: dict) -> None:
    for username in employees:
        print(f"Користувач з логіном '{username}' має ім'я {employees[username]['name']} почав свою роботу '{employees[username]['start_date']}'")


def change_salary(employees: dict) -> dict:
    username = input("Введіть логін працівника: ")
    salary = input("Введіть нове значення ЗП: ")
    if username in employees:
        employees[username]["salary"] = salary
        print(f"ЗП для користувача з логіном '{username}' змінено.")
    else:
        print("Такого користувача немає в системі.")

    return employees


def change_position(employees: dict) -> dict:
    username = input("Введіть логін працівника: ")
    position = input("Введіть нову посаду: ")
    if username in employees:
        employees[username]["position"] = position
        print(f"Посаду для користувача з логіном '{username}' змінено.")
    else:
        print("Такого користувача немає в системі.")

    return employees


def show_log(log: list) -> None:
    pprint(log)


def show_most_using_commands(most_using_command: dict) -> None:
    pprint(most_using_command)


def unknowing_command() -> None:
    print("Невідома команда. Спробуйте ще раз.")


def main():
    products = [
    "Гречка",
    "леонід",
    "Цукорій",
    "Макарони",
    "Йогурт",
    "Спагеті",
    "Картопля",
    "Буряк",
    "Морква",
    "Локшина",
    "Дмитро",
    "Айзен",
    "Петух",
    "російське немовля",
    "Капуста",
    "Капуста",
    "Дондон",
    "Цибуля",
    "Часник",
    "Борошно",
    "Яйця",
    "Бульба",
    "Соняшникова олія",
    "Вершкове масло",
    "Сіль",
    "Додод",
    "Перець",
    "Цукор",
    "Оцет",
    "Сода",
    "Чай",
    "Кава",
    "Око",
    "Зараз"
]
    products_sold = []
    reviews = ["Дуже гарний товар", "ПРОДУКТИ НЕ ДУЖЕ", "дуже погане ставлення від працівників", "Якість товарів просто супер", "Дуже погана як", "Великий асортимент", "Я БІЛЬШЕ СЮДИ НЕ ПОВЕРНУСЬ!!!", "Мені сподобався Ваш магазин", "Якість Во👍", "Боже, яке кчне...💅"]
    employees = {
        "andrew": {
            "position": "Менеджер",
            "salary": "30000",
            "start_date": "22.02.2024",
            "name": "Андрій",
            "password": "1234567a"
        },
        "dima": {
            "position": "Продавець",
            "salary": "14000",
            "start_date": "10.03.2024",
            "name": "Дмитро",
            "password": "1234567b"
        }
    }
    log = []
    most_using_command = {}

    user_name = input("Введіть свій логін: ")
    pass_word = employees.get(user_name, {}).get("password", "")

    while not pass_word:
        position = input("Введіть свою посаду: ")
        salary = input("Введіть свою ЗП: ")
        name = input("Введіть своє ім'я: ")
        employees[user_name] = {
            "position": position,
            "salary": salary,
            "name": name,
            "start_date": datetime.now().strftime("%d.%m.%Y")
        }

        command = input("Введіть 'create' для введення свого паролю;\nВведіть 'generate' для автоматичної генерації паролю.\nАбо будь який символ для виходу з програми\n-> ")
        if command == "create":
            password = input("Введіть пароль 8 і більше символів, цифра і буква: ")

            if is_verify_password(password):
                pass_word = password
            else:
                print("Пароль не пройшов перевірку")

        elif command == "generate":
            len_password = input("Введіть довжину пароля: ")
            if len_password.isdigit() and int(len_password) > 8:
                len_password = int(len_password)
            else:
                len_password = 8

            is_upper = input("Введіть 1 щоб використати великі букви: ")
            is_upper = True if is_upper == "1" else False
            is_punctuation = input("Введіть 1 щоб використовувати спецсимволи: ")
            is_punctuation = True if is_punctuation == "1" else False
            is_repeate = input("Введіть 1 щоб символи повторювались: ")
            is_repeate = True if is_repeate == "1" else False
            password = generate_password(len_password=len_password, is_upper=is_upper, is_punctuation=is_punctuation, is_repeate=is_repeate)
            if is_verify_password(password):
                pass_word = password
            else:
                print("Пароль не пройшов перевірку")

    else:
        print(f"\nВаш пароль '{pass_word}' успішно створено. Запам'ятайте його для входу в систему.\n")

    password = input("Введіть свій пароль для входу в систему: ")

    command = None
    while pass_word == password:
        if not command:
            log.append(f"Користувач з логіном '{user_name}' увійшов у систему: {datetime.now()}")
            print("Доброго дня. Вітаємо в нашій інформаційній системі")

        command = input("Введіть номер команди: ")
        log.append(f"Користувач з логіном '{user_name}' ввів команду {command}: {datetime.now()}")

        if command in most_using_command:
            most_using_command[command] += 1
        else:
            most_using_command[command] = 1

        match command:
            case "show all prods":
                show_all_prods(products)
            case "add prod":
                products = add_prod(products)
            case "add prods":
                products = add_prods(products)
            case "del prod by name":
                products = del_prod_by_name(products)
            case "del prod by numb":
                products = del_prod_by_numb(products)
            case "show sorted prods":
                show_sorted_prods(products)
            case "sold prod":
                products, products_sold = sold_prod(products, products_sold)
            case "find numb prod by name":
                find_numb_prod_by_name(products)
            case "show sold prods":
                show_sold_prods(products_sold)
            case "show sales history":
                show_sales_history(products_sold)
            case "exit":
                exit()
            case "add review":
                reviews = add_review(reviews)
            case "find repeated chars":
                find_repeated_chars(reviews)
            case "find palidrome":
                find_palidrome(products)
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
            case "show most using commands":
                show_most_using_commands(most_using_command)
            case _:
                unknowing_command()

        input("\nНатисніть 'enter' для продовження\n")
    else:
        print("Пароль невірний, доступ заборонено")


if __name__ == "__main__":
    main()