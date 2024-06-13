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
REVIEWS = ["Дуже гарний товар", "ПРОДУКТИ НЕ ДУЖЕ", "дуже погане ставлення від працівників", "Якість товарів просто супер", "Дуже погана як", "Великий асортимент", "Я БІЛЬШЕ СЮДИ НЕ ПОВЕРНУСЬ!!!", "Мені сподобався Ваш магазин", "Якість Во👍", "Боже, яке кчне...💅"]
TEMPLATE = "|{:^5}|{:<100}|"
DELIMITER = "—" * 108
HEAD = TEMPLATE.format("№", "Назва товару")
TEMPLATE_BY_COMMANDS = "|{:<30}|{:<100}|"
HEAD_BY_COMMANDS = TEMPLATE_BY_COMMANDS.format("Command", "Discription")

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

    return True if all(pass_len, pass_digit, pass_char) else False


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

    if index and index.isdigit() and 0 < int(index) <= len(PRODUCTS):
        product = products.pop(int(index) - 1)
        print(f"Товар '{product}' видалено")
    else:
        print("Ви ввели не вірний номер товару")

    return products


while not PASSWORD:
    user_name = input("Введіть свій логін: ")
    if user_name in EMPLOYEES:
        PASSWORD = EMPLOYEES[user_name]["password"]
        break

    position = input("Введіть свою посаду: ")
    salary = input("Введіть свою ЗП: ")
    name = input("Введіть своє ім'я: ")
    EMPLOYEES[user_name] = {
        "position": position,
        "salary": salary,
        "name": name,
        "start_date": datetime.now().strftime("%d.%m.%Y")
    }

    command = input("Введіть 'create' для введення свого паролю;\nВведіть 'generate' для автоматичної генерації паролю.\nАбо будь який символ для виходу з програми\n-> ")
    if command == "create":
        password = input("Введіть пароль 8 і більше символів, цифра і буква: ")

        if is_verify_password(password):
            PASSWORD = password
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
            PASSWORD = password
        else:
            print("Пароль не пройшов перевірку")

else:
    print(f"\nВаш пароль '{PASSWORD}' успішно створено. Запам'ятайте його для входу в систему.\n")

pass_word = input("Введіть свій пароль для входу в систему: ")

command = None
while pass_word == PASSWORD:
    if not command:
        LOG.append(f"Користувач з логіном '{user_name}' увійшов у систему: {datetime.now()}")
        print("Доброго дня. Вітаємо в нашій інформаційній системі")


    command = input("Введіть номер команди: ")
    LOG.append(f"Користувач з логіном '{user_name}' ввів команду {command}: {datetime.now()}")

    if command in MOST_USING_COMMAND:
        MOST_USING_COMMAND[command] += 1
    else:
        MOST_USING_COMMAND[command] = 1









    def show sorted prods":
        print()
        prods = sorted(PRODUCTS)
        for product in prods:
            print(product)

        input("\nНатисніть 'Enter' для продовження ")

    def sold prod":
        product = input("Введіть назву товару для продажу: ")

        if product in PRODUCTS:
            PRODUCTS.remove(product)
            PRODUCTS_SOLD.append(product)
            input(f"\nТовар '{product}' продано. Натисніть 'Enter' для продовження ")
        else:
            input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")

    elif command == "find numb prod by name":
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

    elif command == "show sales history":
        prods_sold = PRODUCTS_SOLD[::-1]
        for product in prods_sold:
            print(product)

        input("\nНатисніть 'Enter' для продовження ")

    elif command == "exit":
        LOG.append(f"Користувач з логіном '{user_name}' увійшов у систему: {datetime.now()}")
        print("До побачення")
        break

    elif command == "add review":
        review = input("Залиште свій відгук:\n")
        REVIEWS.append(review)

    elif command == "find repeated chars":
        reviews = " ".join(REVIEWS)

        repeated_groups = set()
        for i in range(len(reviews)):
            for j in range(i+1, len(reviews)):
                slice = reviews[i:j]
                if reviews.count(slice) >= 2:
                    repeated_groups.add(slice)

        input(f"Список груп символів, які повторюються не менше 2 разів:\n{repeated_groups}")

    elif command == "find palidrome":
        palin_prod = []
        for product in PRODUCTS:
            if product.lower() == product[::-1].lower():
                palin_prod.append(product)

        input(f"В списку товарів є такі слова-паліндроми:\n{palin_prod}") if palin_prod else input("В списку товарів відсутні слова паліндроми.")

    elif command == "add employee":
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

    elif command == "del employee":
        username = input("Введіть логін працівника для видалення: ")
        if username in EMPLOYEES:
            del EMPLOYEES[username]
            # EMPLOYEES.pop(username)
            input(f"Користувача з логіном '{username}' успішно видалено.\nНатисніть 'Enter' для продовження ")
        else:
            input("Такого користувача немає в системі.\nНатисніть 'Enter' для продовження ")

    elif command == "show employees":
        for username in EMPLOYEES:
            # print(username, EMPLOYEES[username])
            print(f"Користувач з логіном '{username}' має ім'я {EMPLOYEES[username]['name']} почав свою роботу '{EMPLOYEES[username]['start_date']}'")
        input("\nНатисніть 'Enter' для продовження ")

    elif command == "change salary":
        username = input("Введіть логін працівника: ")
        salary = input("Введіть нове значення ЗП: ")
        if username in EMPLOYEES:
            EMPLOYEES[username]["salary"] = salary
            input(f"ЗП для користувача з логіном '{username}' змінено.\nНатисніть 'Enter' для продовження ")
        else:
            input("Такого користувача немає в системі.\nНатисніть 'Enter' для продовження ")

    elif command == "change position":
        username = input("Введіть логін працівника: ")
        position = input("Введіть нову посаду: ")
        if username in EMPLOYEES:
            EMPLOYEES[username]["position"] = position
            input(f"Посаду для користувача з логіном '{username}' змінено.\nНатисніть 'Enter' для продовження ")
        else:
            input("Такого користувача немає в системі.\nНатисніть 'Enter' для продовження ")

    elif command == "show log":
        pprint(LOG)
        input("\nНатисніть 'Enter' для продовження ")

    elif command == "show most using commands":
        pprint(MOST_USING_COMMAND)
        input("\nНатисніть 'Enter' для продовження ")

else:
    print("Пароль невірний, доступ заборонено")
