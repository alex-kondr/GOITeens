from datetime import datetime
import json
import os

import files
import products

def exit():
    print("До побачення")
    quit()


def help() -> None:
    print(HELP)


def unknown_command() -> None:
    print("Невідома команда. Спробуйте ще раз")


def main() -> None:

    if not os.path.exists(files.using_commands):
        with open(files.using_commands, "w", encoding="utf-8") as fh:
            json.dump({}, fh)

    with open(files.using_commands, "r", encoding="utf-8") as fh:
        most_using_commands = {}

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

        if command in most_using_commands:
            most_using_commands[command] += 1
        else:
            most_using_commands[command] = 1

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
                show_most_using_commands(most_using_commands)
            case "help":
                help()
            case _:
                unknown_command()

        input("\nНатисніть 'Enter' для продовження ")

    else:
        print("Пароль невірний, доступ заборонено")


if __name__ == "__main__":
    main()
