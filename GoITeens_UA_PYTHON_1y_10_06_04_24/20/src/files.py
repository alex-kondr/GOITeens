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
        file.write([])


def open_products(path: str = list_files.PRODUCTS) -> list:
    with open(path, "r", encoding="utf-8") as file:
        products = file.readlines()
        products = [product.strip() for product in products]

    return products


def open_products_sold(path: str = list_files.PRODUCTS_SOLD) -> list:
    with open(path, "r", encoding="utf-8") as file:
        products_sold = file.readlines()

    return products_sold


def open_reviews(path: str = list_files.REVIEWS) -> list:
    with open(path, "r", encoding="utf-8") as file:
        reviews = json.load(file)

    return reviews
