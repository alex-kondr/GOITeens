import string
import random
from datetime import datetime
from pprint import pprint


PRODUCTS = [
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
PRODUCTS_SOLD = []

###########################
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

PASSWORD = ""
REVIEWS = [
    "Дуже гарний товар",
    "ПРОДУКТИ НЕ ДУЖЕ",
    "дуже погане ставлення від працівників",
    "Якість товарів просто супер",
    "Дуже погана як",
    "Великий асортимент",
    "Я БІЛЬШЕ СЮДИ НЕ ПОВЕРНУСЬ!!!",
    "Мені сподобався Ваш магазин",
    "Якість Во👍",
    "Боже, яке кчне...💅"]

EMPLOYEES = {
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
LOG = []
MOST_USING_COMMAND = {}


def is_verify_password(password: str) -> bool:
    pass_len = False if len(password) < 8 else True
    pass_digit = False
    pass_char = False

    for char in password:
        if char.isdigit():
            pass_digit = True
        if char.isalpha():
            pass_char = True

    return True if pass_len and pass_digit and pass_char else False


def generate_password(
    len_password: int = 8,
    is_upper: bool = False,
    is_punctuation: bool = False,
    is_repeat: bool = False
) -> str:

    pass_chars = string.ascii_lowercase + string.digits
    pass_chars += string.ascii_uppercase if is_upper else ""
    pass_chars += string.punctuation if is_punctuation else ""
    password = random.choices(pass_chars, k=len_password) if is_repeat else random.sample(pass_chars, k=len_password)
    return "".join(password)


def show_all_prods() -> None:
    template = "|{:^5}|{:<100}|"
    delimiter = "—" * 108
    head = template.format("№", "Назва товару")
    print(template)
    print(head)
    print(delimiter)
    for i, product in enumerate(PRODUCTS, start=1):
        print(template.format(i, product))

    print(delimiter)
    input("\nНатисніть 'Enter' для продовження ")


def add_prod() -> None:
    product = input("Введіть новий товар для додавання до списку: ")

    if product not in PRODUCTS:
        PRODUCTS.append(product)
        input(f"\nТовар '{product}' доданий до списку. Натисніть 'Enter' для продовження ")
    else:
        input("\nТакий товар вже є у списку. Натисніть 'Enter' для продовження ")


def add_prods() -> None:
    prods = input("Введіть список товар для додавання через пробіл\n-> ")
    prods = prods.split()
    PRODUCTS.extend(prods)
    input("\nСписок товарів розширено. Натисніть 'Enter' для продовження ")


def del_prod_by_name() -> None:
    product = input("Введіть назву товару для видалення зі списку товарів: ")

    if product in PRODUCTS:
        PRODUCTS.remove(product)
        input(f"\nТовар '{product}' видалено зі списку. Натисніть 'Enter' для продовження ")
    else:
        input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")


def del_prod_by_numb() -> None:
    index = input("Введіть номер товару для видалення: ")

    if index and index.isdigit() and 0 < int(index) <= len(PRODUCTS):
        product = PRODUCTS.pop(int(index) - 1)
        input(f"Товар '{product}' видалено. Натисніть 'Enter' для продовження ")
    else:
        input("Ви ввели не вірний номер товару. Натисніть 'Enter' для продовження ")


def show_sorted_prods() -> None:
    print()
    prods = sorted(PRODUCTS)
    for product in prods:
        print(product)

    input("\nНатисніть 'Enter' для продовження ")


def sold_prod() -> None:
    product = input("Введіть назву товару для продажу: ")

    if product in PRODUCTS:
        PRODUCTS.remove(product)
        PRODUCTS_SOLD.append(product)
        input(f"\nТовар '{product}' продано. Натисніть 'Enter' для продовження ")
    else:
        input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")


def find_numb_prod_by_name() -> None:
    product = input("Введіть назву товару для пошуку: ")

    if product in PRODUCTS:
        index = PRODUCTS.index(product)
        input(f"Товар '{product}' знаходиться під номером {index + 1}. Натисніть 'Enter' для продовження ")
    else:
        input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")


def show_sold_prods() -> None:
    if not PRODUCTS_SOLD:
        print("Список проданих товарів пустий")

    for product in PRODUCTS_SOLD:
        print(product)

    input("\nНатисніть 'Enter' для продовження ")


def show_sales_history() -> None:
    prods_sold = PRODUCTS_SOLD[::-1]
    for product in prods_sold:
        print(product)

    input("\nНатисніть 'Enter' для продовження ")


def exit():
    LOG.append(f"Користувач з логіном '{user_name}' увійшов у систему: {datetime.now()}")
    print("До побачення")
    quit()


def add_review() -> None:
    review = input("Залиште свій відгук:\n")
    REVIEWS.append(review)


def find_repeated_chars() -> None:
    reviews = " ".join(REVIEWS)

    repeated_groups = set()
    for i in range(len(reviews)):
        for j in range(i+1, len(reviews)):
            slice = reviews[i:j]
            if reviews.count(slice) >= 2:
                repeated_groups.add(slice)

    input(f"Список груп символів, які повторюються не менше 2 разів:\n{repeated_groups}")


def find_palidrome() -> None:
    palin_prod = []
    for product in PRODUCTS:
        if product.lower() == product[::-1].lower():
            palin_prod.append(product)

    input(f"В списку товарів є такі слова-паліндроми:\n{palin_prod}") if palin_prod else input("В списку товарів відсутні слова паліндроми.")


def add_employee() -> None:
    username = input("Введіть логін користувача: ")
    name = input("Введіть ім'я працівника: ")
    position = input("Введіть посаду працівника: ")
    salary = input("Введіть ЗП: ")
    start_date = input("Введіть дату початку роботи у форматі '01.01.2024': ")
    password = input("Введіть пароль для працівника: ")

    if username not in EMPLOYEES:
        EMPLOYEES[username] = {
            "position": position,
            "salary": salary,
            "name": name,
            "start_date": start_date,
            "password": password
        }
        input("Працівника успішно зареєстровано в системі.\nНатисніть 'Enter' для продовження ")
    else:
        input("Такий логін вже зареєстрований в системі.\nНатисніть 'Enter' для продовження ")


def del_employee() -> None:
    username = input("Введіть логін працівника для видалення: ")
    if username in EMPLOYEES:
        del EMPLOYEES[username]
        # EMPLOYEES.pop(username)
        input(f"Користувача з логіном '{username}' успішно видалено.\nНатисніть 'Enter' для продовження ")
    else:
        input("Такого користувача немає в системі.\nНатисніть 'Enter' для продовження ")


def show_employees() -> None:
    for username in EMPLOYEES:
        # print(username, EMPLOYEES[username])
        print(f"Користувач з логіном '{username}' має ім'я {EMPLOYEES[username]['name']} почав свою роботу '{EMPLOYEES[username]['start_date']}'")
    input("\nНатисніть 'Enter' для продовження ")


def change_salary() -> None:
    username = input("Введіть логін працівника: ")
    salary = input("Введіть нове значення ЗП: ")
    if username in EMPLOYEES:
        EMPLOYEES[username]["salary"] = salary
        input(f"ЗП для користувача з логіном '{username}' змінено.\nНатисніть 'Enter' для продовження ")
    else:
        input("Такого користувача немає в системі.\nНатисніть 'Enter' для продовження ")


def change_position() -> None:
    username = input("Введіть логін працівника: ")
    position = input("Введіть нову посаду: ")
    if username in EMPLOYEES:
        EMPLOYEES[username]["position"] = position
        input(f"Посаду для користувача з логіном '{username}' змінено.\nНатисніть 'Enter' для продовження ")
    else:
        input("Такого користувача немає в системі.\nНатисніть 'Enter' для продовження ")


def show_log() -> None:
    pprint(LOG)
    input("\nНатисніть 'Enter' для продовження ")


def show_most_using_commands() -> None:
    pprint(MOST_USING_COMMAND)
    input("\nНатисніть 'Enter' для продовження ")


def help() -> None:
    print(HELP)

COMMANDS = {
    "show all prods": show_all_prods,
    "add prod": add_prod,
    "add prods": add_prods,
    "del prod by name": del_prod_by_name,
    "del prod by numb": del_prod_by_numb,
    "show sorted prods": show_sorted_prods,
    "sold prod": sold_prod,
    "find numb prod by name": find_numb_prod_by_name,
    "show sold prods": show_sold_prods,
    "show sales history": show_sales_history,
    "exit": exit,
    "add review": add_review,
    "find repeated chars": find_repeated_chars,
    "find palidrome": find_palidrome,
    "add employee": add_employee,
    "del employee": del_employee,
    "show employees": show_employees,
    "change salary": change_salary,
    "change position": change_position,
    "show log": show_log,
    "show most using commands": show_most_using_commands,
    "help": help
}


if __name__ == "__main__":
    user_name = input("Введіть свій логін: ")
    if user_name in EMPLOYEES:
        PASSWORD = EMPLOYEES[user_name]["password"]

    else:
        position = input("Введіть свою посаду: ")
        salary = input("Введіть свою ЗП: ")
        name = input("Введіть своє ім'я: ")
        EMPLOYEES[user_name] = {
            "position": position,
            "salary": salary,
            "name": name,
            "start_date": datetime.now().strftime("%d.%m.%Y")
        }

    while not PASSWORD:
        command = input("Введіть 'create' для введення свого паролю;\nВведіть 'generate' для автоматичної генерації паролю.\nАбо будь який символ для виходу з програми\n-> ")
        if command == "create":
            password = input("Введіть свій пароль (повинен містити не менше 8 символів, а також повинен містити хоча б одну букву та одну цифру): ")

            if is_verify_password(password):
                PASSWORD = password
                EMPLOYEES[user_name]["password"] = PASSWORD
            else:
                print("Пароль не пройшов перевірку, введіть новий пароль або згенеруйте автоматичний пароль")

        elif command == "generate":
            len_pass = input("Введіть довжину пароля (не менше 8) або залишити за замовчуванням (8 символів): ")
            if len_pass.isdigit() and int(len_pass) > 8:
                len_pass = int(len_pass)
            else:
                len_pass = 8

            is_upper = True if input("Чи використовувати великі букви (1 - так, будь який інший символ - ні)? ") == "1" else False
            is_punctuation = True if input("Чи використовувати спецсимволи (1 - так, будь який інший символ - ні)? ") == "1" else False
            is_repeat = True if input("Чи можуть символи повторюватись (1 - Так, будь який інший символ - Ні)? ") == "1" else False
            password = ""
            while not is_verify_password(password):
                password = generate_password(len_password=len_pass, is_punctuation=is_punctuation, is_upper=is_upper, is_repeat=is_repeat)

            PASSWORD = password
            EMPLOYEES[user_name]["password"] = PASSWORD
    else:
        print(f"\nВаш пароль '{PASSWORD}' успішно створено. Запам'ятайте його для входу в систему.\n")

    pass_word = input("Введіть свій пароль для входу в систему: ")

    command = None
    while pass_word == PASSWORD:
        if not command:
            LOG.append(f"Користувач з логіном '{user_name}' увійшов у систему: {datetime.now()}")
            print("Доброго дня. Вітаємо в нашій інформаційній системі")

        command = input("Введіть номер команди ('help' для довідки): ")
        LOG.append(f"Користувач з логіном '{user_name}' ввів команду {command}: {datetime.now()}")

        if command in MOST_USING_COMMAND:
            MOST_USING_COMMAND[command] += 1
        else:
            MOST_USING_COMMAND[command] = 1

        if command in COMMANDS:
            command = COMMANDS[command]
            command()
        else:
            print("Невідома команда. Спробуйте ще раз")

    else:
        print("Пароль невірний, доступ заборонено")

