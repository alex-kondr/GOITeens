import string
import random
from datetime import datetime
from pprint import pprint


def is_verify_password(password: str) -> bool:
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
        return True
    else:
        return False


def generate_password() -> str:
    while True:
        command = input("Потрібно створити пароль для можливості працювати в системі.\n"
                    "Введіть 1 - для введення свого паролю.\n"
                    "Введіть 2 - для автоматичної генерації паролю\n-> ")

        if command == "1":
            password = input("Введіть свій пароль. Довжина паролю має бути не менше 8 символіd, містити мінім одна буква та одну цифру.\n-> ")

            if is_verify_password(password):
                return password
            else:
                input("Ваш пароль не пройшов перевірку. Спробуйте ще раз. 'Enter' для продовження ")

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

            return "".join(password)


def show_all_products(products: list) -> None:
    delimiter = "-" * 28
    template = "|{:<5}|{:<20}|"

    print(delimiter)
    for i, product in enumerate(products, start=1):
        print(template.format(i, product))
    else:
        print(delimiter)


def add_product(products: list) -> list:
    product = input("\nВведіть новий товар для додавання до списку: ")

    if product in products:
        print("\nТакий товар вже доданий")
    else:
        products.append(product)
        print("\nНовий товар доданий до списку")

    return products


def add_products(products: list) -> list:
    prods = input("\nВведіть список товарів через пробіл:\n").split()
    products.extend(prods)
    print("\nСписок продуктів розширено")
    return products


def del_prod_by_name(products: list) -> list:
    product = input("Введіть назву товару для видалення: ")

    if product in products:
        products.remove(product)
        print(f"\nТовар '{product}' видалено зі списку")
    else:
        print(f"\nТовар '{product}' відсутній у списку")

    return products


def del_prod_by_numb(products: list) -> list:
    number = input("Введіть номер товару для видалення: ")

    if number.isdigit() and 0 < int(number) <= len(products):
        product = products.pop(int(number) - 1)
        print(f"\nТовар '{product}' видалено зі списку")
    else:
        print("\nВвели невірний номер")

    return products


def sort_prod_by_name(products: list) -> None:
    prods = sorted(products)

    for i, prod in enumerate(prods, start=1):
        print(f"{i}: {prod}")

    print("\nСписок товарі відсортовано")


def sold_product(products: list, products_sold: list) -> tuple[list]:
    product = input("Введіть товар для продажу: ")

    if product in products:
        products.remove(product)
        products_sold.append(product)
        print(f"Товар '{product}' продано")
    else:
        print(f"Товар '{product}' відсутній у списку")

    return products, products_sold


def find_numb_prod_by_name(products: list) -> None:
    product = input("Введіть назву товару для пошуку: ")

    if product in products:
        index = products.index(product)
        print(f"\nТовар '{product}' знаходить під номер '{index + 1}'")
    else:
        print(f"\nТовар '{product}' відсутній у списку")


def show_sold_product(products_sold: list) -> None:
    print("\nСписок проданий товарів\n")
    for i, product in enumerate(products_sold, start=1):
        print(f"{i}: {product}")


def history_sold(products_sold: list) -> None:
    prods_sold = products_sold[::-1]

    if not prods_sold:
        print("\nСписок проданих товарів порожній\n")

    print("\nІсторія продажу\n")
    for product in prods_sold:
        print(product)


def exit():
    print("\nДякую що були з нами. Чекаємо наступної зустрічі.\n")
    quit()


def add_review(reviews: list) -> list:
    review = input("Введіть свій відгук: ")
    reviews.append(review)
    print("\nВаш відгук додано до системи.")
    return reviews


def find_repeated_groups(reviews: list) -> None:
    reviews = " ".join(reviews).lower()

    repeated_chars = set()
    for i in range(len(reviews)):
        for j in range(i+1, len(reviews)):
            if reviews.count(reviews[i:j]) >= 2:
                repeated_chars.add(reviews[i:j])

    print(f"\nГрупи символів, які повторююьюся не менше 2-х разів:\n{repeated_chars}")


def find_palindrome(products: list) -> None:
    palin_prod = [product for product in products if product.lower() == product.lower()[::-1]]
    print(f"Слова-паліндроми:\n{palin_prod}")


def show_reviews(reviews: list) -> None:
    for review in reviews:
        print(review)


def add_employee(employees: dict) -> dict:
    login = input("Введіть логін для користувача: ")
    position = input("Введіть посаду працівника: ")
    salary = input("Введіть ЗП для користувача: ")
    start_date = input("Введіть дату старту роботи у форматі '01.01.2024': ")
    name = input("Введіть ім'я працівника: ")
    password = input("Введіть пароль для користувача: ")

    employees[login] = {
        "posititon": position,
        "salary": salary,
        "start_date": start_date,
        "name": name,
        "password": password
    }
    print("Користуча успішно додано.")
    return employees


def del_employee(employees: dict) -> dict:
    login = input("Введіть логін користувача для видалення співробітника: ")

    if login in employees:
        del employees[login]
        print(f"Користувача '{login}' успішно видалено")
    else:
        print("Такого користувача не знайдено")

    return employees


def show_employees(employees: dict) -> None:
    for employee in employees:
        print(f"Інформація про користувача з логіном {employee}\n")
        for key, value in employees[employee].items():
            print(f"{key}: {value}")
        print("\n")


def change_salary(employees: dict) -> dict:
    login = input("Введіть логін користувача: ")

    if login in employees:
        salary = input("Введіть нове значення ЗП: ")
        employees[login]["salary"] = salary
        print("Суму ЗП успішно змінено")
    else:
        print("Такого користувача не знайдено")

    return employees


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
        "Кава",
        "Око",
        "Зараз"
    ]
    products_sold = []
    reviews = ["Чудове обслуговування", "Такий собі продуктовий магазин", "свіжі товари", "не свіжі товари", "Чудовий магазин,не один раз вже тут купую продукти"]
    commands = {
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
        "add employee": "Додати нового працівника",
        "del employee": "Видалити працівника",
        "show employees": "Переглянути список працівників",
        "change salary": "Змінити заробітну плату працівника",
        "change position": "Змінити посаду працівника",
        "show log": "Показати лог",
        "show using commands": "Показати список команд та їх частоту використання",
        "help": "Показати список доступних команд"
    }
    log = []
    using_commands = {}
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

    login_global = input("Введіть свій логін користувача: ")
    password = employees.get(login_global, {}).get("password")

    if not password:
        position = input("Введіть свою посаду: ")
        salary = input("Введіть свою зарплату: ")
        name = input("Введіть своє ім'я: ")
        start_date = datetime.now().strftime("%d.%m.%Y")

        employees[login_global] = {
            "position": position,
            "salary": salary,
            "start_date": start_date,
            "name": name,
        }

        password = generate_password()
        employees[login_global]["password"] = password

    else:
        input(f"\nПароль успішно створено: '{password}'. Запам'ятайте його. 'Enter' для продовження ")

    password_input = input("\nВведіть пароль для входу у систему: ")

    command = ""
    while password_input == password:
        if not command:
            log.append(f"Користувач з логіном '{login_global}' ввішов у систему: {datetime.now()}")
            print("Доброго дня. Вітаємо в нашій інформаційній системі")

        command = input("\nВведіть команду або введіть 'help' для допомоги: ")
        log.append(f"Корисчувач з логіном '{login_global}' ввів команду '{command}': {datetime.now()}")
        using_commands[command] = using_commands.get(command, 0) + 1

