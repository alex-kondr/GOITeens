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


def sold_product(products: list, products_sold: list) -> tuple[list, list]:
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


def find_palindrome(products: list) -> None:
    palin_prod = [product for product in products if product.lower() == product.lower()[::-1]]
    print(f"Слова-паліндроми:\n{palin_prod}")
