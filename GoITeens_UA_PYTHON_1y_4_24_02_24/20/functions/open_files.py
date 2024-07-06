import os

from files import list_files


with open(list_files.HELP, "r", encoding="utf-8") as fh:
    help = fh.read()

if not os.path.exists(list_files.PRODUCTS):
    with open(list_files.PRODUCTS, "w", encoding="utf-8"):
        pass

with open(list_files.PRODUCTS, "r", encoding="utf-8") as fh:
    products = [prod.strip() for prod in fh.readlines()]

if not os.path.exists(list_files.LOG):
    with open(list_files.LOG, "w", encoding="utf-8"):
        pass

with open(list_files.LOG, "r", encoding="utf-8") as fh:
    log = [loging.strip() for loging in fh.readlines()]