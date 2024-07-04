import os

from files import list_files


if not os.path.exists(list_files.products):
    with open(list_files.products, "w", encoding="utf-8"):
        pass