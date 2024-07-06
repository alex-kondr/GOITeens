from datetime import datetime
from pprint import pprint

from functions.products import (
    show_prods,
    add_prod,
    add_prods,
    del_prod_by_name,
    del_prod_by_num,
    sort,
    sold_prod,
    find_prod_by_name,
    show_history,
    palindrome
)
from functions.reviews import add_review, find_dublicate_char
from functions.employees import (
    add_employee,
    del_employee,
    show_employees,
    change_salary,
    change_position
)
from functions.password import is_verify_password, generate_password
from files import list_files
from functions import open_files, close_files


def exit() -> None:
    print("До побачення")
    quit()


def help() -> None:
    print(open_files.help)


def show_log(log: list) -> None:
    pprint(log)


def show_using_commands(using_commands: dict) -> None:
    pprint(using_commands)


def unknown_command() -> None:
    print("\nНевідома команда. Спробуйте іншу команду.\n")


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
    products = open_files.products
    products_sold = []
    log = open_files.log
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
                close_files.save_progres(products, log)
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