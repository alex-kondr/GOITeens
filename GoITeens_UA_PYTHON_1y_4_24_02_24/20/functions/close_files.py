from files import list_files

def save_progres(products: list, log: list) -> None:
    with open(list_files.PRODUCTS, "w", encoding="utf-8") as fh:
        products = [f"{prod}\n" for prod in products]
        fh.writelines(products)

    with open(list_files.LOG, "w", encoding="utf-8") as fh:
        log = [f"{loging}\n" for loging in log]
        fh.writelines(log)