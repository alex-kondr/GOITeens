import os
import json

import files


if not os.path.exists(files.products):
    with open(files.products, "w", encoding="utf-8"):
        pass

with open(files.products, "r", encoding="utf-8") as fh:
    products = fh.readlines()

if not os.path.exists(files.products_sold):
    with open(files.products_sold, "w", encoding="utf-8"):
        pass

with open(files.products_sold, "r", encoding="utf-8") as fh:
    products_sold = fh.readlines()

if not os.path.exists(files.reviews):
    with open(files.reviews, "w", encoding="utf-8"):
        pass

with open(files.reviews, "r", encoding="utf-8") as fh:
    reviews = fh.readlines()

if not os.path.exists(files.employees):
    with open(files.employees, "w", encoding="utf-8") as fh:
        json.dump({}, fh)

with open(files.employees, "r", encoding="utf-8") as fh:
    employees = json.load(fh)

if not os.path.exists(files.log):
    with open(files.log, "w", encoding="utf-8"):
        pass

with open(files.log, "r", encoding="utf-8") as fh:
    log = fh.readlines()
