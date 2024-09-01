import os
import json

from files import list_files


if not os.path.exists(list_files.PRODUCTS):
    with open(list_files.PRODUCTS, "w", encoding="utf-8"):
        pass

if not os.path.exists(list_files.PRODUCTS_SOLD):
    with open(list_files.PRODUCTS_SOLD, "w", encoding="utf-8"):
        pass

if not os.path.exists(list_files.REVIEWS):
    with open(list_files.REVIEWS, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.EMPLOYEES):
    with open(list_files.EMPLOYEES, "w", encoding="utf-8") as file:
        json.dump({}, file)

if not os.path.exists(list_files.LOG):
    with open(list_files.LOG, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.USING_COMMANDS):
    with open(list_files.USING_COMMANDS, "w", encoding="utf-8") as file:
        json.dump({}, file)


def open_products(path: str = list_files.PRODUCTS) -> list:
    with open(path, "r", encoding="utf-8") as file:
        products = file.readlines()

    products = [product.strip() for product in products]
    return products


def save_products(products: list, path: str = list_files.PRODUCTS) -> None:
    products = [f"{product}\n" for product in products]

    with open(path, "w", encoding="utf-8") as file:
        file.writelines(products)


def open_products_sold(path: str = list_files.PRODUCTS_SOLD) -> list:
    with open(path, "r", encoding="utf-8") as file:
        products_sold = file.readlines()

    products_sold = [product_sold.strip() for product_sold in products_sold]
    return products_sold


def save_products_sold(products_sold: list, path: str = list_files.PRODUCTS_SOLD) -> None:
    products_sold = [f"{product_sold}\n" for product_sold in products_sold]

    with open(path, "w", encoding="utf-8") as file:
        file.writelines(products_sold)



def open_reviews(path: str = list_files.REVIEWS) -> list:
    with open(path, "r", encoding="utf-8") as file:
        reviews = json.load(file)

    return reviews


def save_reviews(reviews: list, path: str = list_files.REVIEWS) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(reviews, file, ensure_ascii=False, indent=4)


def open_employees(path: str = list_files.EMPLOYEES) -> dict[dict]:
    with open(path, "r", encoding="utf-8") as file:
        employees = json.load(file)

    return employees


def save_employees(employees: dict[dict], path: str = list_files.EMPLOYEES) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(employees, file, ensure_ascii=False, indent=4)


def open_log(path: str = list_files.LOG) -> list:
    with open(path, "r", encoding="utf-8") as file:
        log = json.load(file)

    return log


def save_log(log: list, path: str = list_files.LOG) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(log, file, ensure_ascii=False, indent=4)


def open_using_commands(path: str = list_files.USING_COMMANDS) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        using_commands = json.load(file)

    return using_commands


def save_using_commands(using_commands: dict, path: str = list_files.USING_COMMANDS) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(using_commands, file, ensure_ascii=False, indent=4)
