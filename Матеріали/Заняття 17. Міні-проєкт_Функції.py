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
    is_repeat: bool = True
) -> str:

    pass_chars = string.ascii_lowercase + string.digits
    pass_chars += string.ascii_uppercase if is_upper else ""
    pass_chars += string.punctuation if is_punctuation else ""
    password = random.choices(pass_chars, k=len_password) if is_repeat else random.sample(pass_chars, k=len_password)
    return "".join(password)


def show_all_prods(products: list) -> None:
    template = "|{:^5}|{:<100}|"
    delimiter = "—" * 108
    head = template.format("№", "Назва товару")
    print(template)
    print(head)
    print(delimiter)
    for i, product in enumerate(products, start=1):
        print(template.format(i, product))

    print(delimiter)


def add_prod(products: list) -> list:
    product = input("Введіть новий товар для додавання до списку: ")

    if product not in products:
        products.append(product)
        input(f"\nТовар '{product}' доданий до списку. Натисніть 'Enter' для продовження ")
    else:
        input("\nТакий товар вже є у списку. Натисніть 'Enter' для продовження ")

    return products


def add_prods(products: list) -> list:
    prods = input("Введіть список товар для додавання через пробіл\n-> ")
    prods = prods.split()
    products.extend(prods)
    input("\nСписок товарів розширено. Натисніть 'Enter' для продовження ")
    return products


def del_prod_by_name(products: list) -> list:
    product = input("Введіть назву товару для видалення зі списку товарів: ")

    if product in products:
        products.remove(product)
        input(f"\nТовар '{product}' видалено зі списку. Натисніть 'Enter' для продовження ")
    else:
        input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")

    return products


def del_prod_by_numb(products: list) -> list:
    index = input("Введіть номер товару для видалення: ")

    if index and index.isdigit() and 0 < int(index) <= len(products):
        product = products.pop(int(index) - 1)
        input(f"Товар '{product}' видалено. Натисніть 'Enter' для продовження ")
    else:
        input("Ви ввели не вірний номер товару. Натисніть 'Enter' для продовження ")

    return products


def show_sorted_prods(products: list) -> None:
    print()
    prods = sorted(products)
    for product in prods:
        print(product)


def sold_prod(products: list[str], products_sold: list[str]) -> tuple[list, list]:
    product = input("Введіть назву товару для продажу: ")

    if product in products:
        products.remove(product)
        products_sold.append(product)
        input(f"\nТовар '{product}' продано. Натисніть 'Enter' для продовження ")
    else:
        input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")

    return products, products_sold


def find_numb_prod_by_name(products: list) -> None:
    product = input("Введіть назву товару для пошуку: ")

    if product in products:
        index = products.index(product)
        input(f"Товар '{product}' знаходиться під номером {index + 1}. Натисніть 'Enter' для продовження ")
    else:
        input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")


def show_sold_prods(products_sold: list) -> None:
    if not products_sold:
        print("Список проданих товарів пустий")

    for product in products_sold:
        print(product)

    input("\nНатисніть 'Enter' для продовження ")


def show_sales_history(products_sold: list) -> list:
    prods_sold = products_sold[::-1]
    for product in prods_sold:
        print(product)


def exit():
    print("До побачення")
    quit()


def add_review(reviews: list) -> list:
    review = input("Залиште свій відгук:\n")
    reviews.append(review)
    return reviews


def find_repeated_chars(reviews: list) -> None:
    revs = " ".join(reviews)

    repeated_groups = set()
    for i in range(len(revs)):
        for j in range(i+1, len(revs)):
            slice = revs[i:j]
            if revs.count(slice) >= 2:
                repeated_groups.add(slice)

    print(f"Список груп символів, які повторюються не менше 2 разів:\n{repeated_groups}")


def find_palidrome(products: list) -> None:
    palin_prod = []
    for product in products:
        if product.lower() == product[::-1].lower():
            palin_prod.append(product)

    print(f"В списку товарів є такі слова-паліндроми:\n{palin_prod}") if palin_prod else print("В списку товарів відсутні слова паліндроми.")


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
        input("Працівника успішно зареєстровано в системі.\nНатисніть 'Enter' для продовження ")
    else:
        input("Такий логін вже зареєстрований в системі.\nНатисніть 'Enter' для продовження ")

    return employees


def del_employee(employees: dict) -> dict:
    username = input("Введіть логін працівника для видалення: ")
    if username in employees:
        del employees[username]
        input(f"Користувача з логіном '{username}' успішно видалено.")
    else:
        input("Такого користувача немає в системі.\nНатисніть 'Enter' для продовження ")

    return employees


def show_employees(employees: dict) -> None:
    for username in employees:
        print(f"Користувач з логіном '{username}' має ім'я {employees[username]['name']} почав свою роботу '{employees[username]['start_date']}'")


def change_salary(employees: dict) -> dict:
    username = input("Введіть логін працівника: ")
    salary = input("Введіть нове значення ЗП: ")
    if username in employees:
        employees[username]["salary"] = salary
        input(f"ЗП для користувача з логіном '{username}' змінено.")
    else:
        input("Такого користувача немає в системі.")

    return employees


def change_position(employees: dict) -> dict:
    username = input("Введіть логін працівника: ")
    position = input("Введіть нову посаду: ")
    if username in employees:
        employees[username]["position"] = position
        input(f"Посаду для користувача з логіном '{username}' змінено.\nНатисніть 'Enter' для продовження ")
    else:
        input("Такого користувача немає в системі.\nНатисніть 'Enter' для продовження ")

    return products, products_sold, employees, reviews


def show_log() -> None:
    pprint(log)
    input("\nНатисніть 'Enter' для продовження ")


def show_most_using_commands() -> None:
    pprint(most_using_command)
    input("\nНатисніть 'Enter' для продовження ")


def help() -> None:
    print(HELP)


def unknown_command() -> None:
    print("Невідома команда. Спробуйте ще раз")


def create_password() -> str:
    command = input("Введіть 'create' для введення свого паролю будь який символ для автоматичної генерації -> ")
    if command == "create":
        password = input("Введіть свій пароль (повинен містити не менше 8 символів, а також повинен містити хоча б одну букву та одну цифру): ")

    else:
        len_pass = input("Введіть довжину пароля (не менше 8) або залишити за замовчуванням (8 символів): ")
        if len_pass.isdigit() and int(len_pass) > 8:
            len_pass = int(len_pass)
        else:
            len_pass = 8

        is_upper = True if input("Чи використовувати великі букви (1 - так, будь який інший символ - ні)? ") == "1" else False
        is_punctuation = True if input("Чи використовувати спецсимволи (1 - так, будь який інший символ - ні)? ") == "1" else False
        is_repeat = True if input("Чи можуть символи повторюватись (1 - Так, будь який інший символ - Ні)? ") == "1" else False
        password = ""

        password = generate_password(len_password=len_pass, is_punctuation=is_punctuation, is_upper=is_upper, is_repeat=is_repeat)

    return password


def main() -> None:
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
    reviews = [
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
    password = employees.get(user_name, {}).get("password", "")

    position = input("Введіть свою посаду: ")
    salary = input("Введіть свою ЗП: ")
    name = input("Введіть своє ім'я: ")
    employees[user_name] = {
        "position": position,
        "salary": salary,
        "name": name,
        "start_date": datetime.now().strftime("%d.%m.%Y")
    }

    while not is_verify_password(password):
        password = create_password()

    else:
        print(f"\nВаш пароль '{password}'. Запам'ятайте його для входу в систему.\n")
        employees[user_name]["password"] = password

    pass_word = input("Введіть свій пароль для входу в систему: ")

    command = None
    while pass_word == employees[user_name]["password"]:
        if not command:
            log.append(f"Користувач з логіном '{user_name}' увійшов у систему: {datetime.now()}")
            print("Доброго дня. Вітаємо в нашій інформаційній системі")

        command = input("Введіть команду ('help' для довідки): ")
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
                
            case _:
                unknown_command()

        input("\nНатисніть 'Enter' для продовження ")

    else:
        print("Пароль невірний, доступ заборонено")


# COMMANDS = {
#     "show all prods": show_all_prods,
#     "add prod": add_prod,
#     "add prods": add_prods,
#     "del prod by name": del_prod_by_name,
#     "del prod by numb": del_prod_by_numb,
#     "show sorted prods": show_sorted_prods,
#     "sold prod": sold_prod,
#     "find numb prod by name": find_numb_prod_by_name,
#     "show sold prods": show_sold_prods,
#     "show sales history": show_sales_history,
#     "exit": exit,
#     "add review": add_review,
#     "find repeated chars": find_repeated_chars,
#     "find palidrome": find_palidrome,
#     "add employee": add_employee,
#     "del employee": del_employee,
#     "show employees": show_employees,
#     "change salary": change_salary,
#     "change position": change_position,
#     "show log": show_log,
#     "show most using commands": show_most_using_commands,
#     "help": help
# }


if __name__ == "__main__":
    main()
