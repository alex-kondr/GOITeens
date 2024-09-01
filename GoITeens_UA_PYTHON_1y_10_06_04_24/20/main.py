from datetime import datetime
from pprint import pprint

from src.password import generate_password
from src.products import (
    show_all_products,
    add_product,
    add_products,
    del_prod_by_name,
    del_prod_by_numb,
    sort_prod_by_name,
    find_numb_prod_by_name,
    sold_product,
    show_sold_product,
    history_sold,
    find_palindrome
)
from src.reviews import (
    add_review,
    find_repeated_groups,
    show_reviews
)
from src.employees import (
    add_employee,
    del_employee,
    show_employees,
    change_salary,
    change_position
)
from src import files_actions
from files.list_files import HELP


def exit():
    print("\nДякую що були з нами. Чекаємо наступної зустрічі.\n")
    quit()


def help(path: str = HELP) -> None:
    with open(path, "r", encoding="utf-8") as file:
        print(file.read())


def show_log(log: list) -> None:
    pprint(log, width=100)


def show_using_commands(using_commands: dict) -> None:
    for command, count in using_commands.items():
        print(f"Команда '{command}' використана таку кількість разів: {count}")


def main():
    products = files_actions.open_products()
    products_sold = files_actions.open_products_sold()
    reviews = files_actions.open_reviews()
    log = files_actions.open_log()
    using_commands = files_actions.open_using_commands()
    employees = files_actions.open_employees()

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

        match command:
            case "show all products":
                show_all_products(products)
            case "add product":
                products = add_product(products)
            case "add products":
                products = add_products(products)
            case "del prod by name":
                products = del_prod_by_name(products)
            case "del prod by numb":
                products = del_prod_by_numb(products)
            case "sort prod by name":
                sort_prod_by_name(products)
            case "sold product":
                products, products_sold = sold_product(products, products_sold)
            case "find numb prod ny name":
                find_numb_prod_by_name(products)
            case "show sold product":
                show_sold_product(products_sold)
            case "history sold":
                history_sold(products_sold)
            case "exit":
                files_actions.save_products(products)
                files_actions.save_products_sold(products_sold)
                files_actions.save_reviews(reviews)
                files_actions.save_employees(employees)
                files_actions.save_log(log)
                files_actions.save_using_commands(using_commands)
                exit()
            case "add review":
                reviews = add_review(reviews)
            case "find repeated groups":
                find_repeated_groups(reviews)
            case "find palindrome":
                find_palindrome(products)
            case "show reviews":
                show_reviews(reviews)
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
                print("Невідома команда. Спробуйте ще раз...")

    else:
        print("Пароль невірний. Доступ заборонено.")


if __name__ == "__main__":
    main()