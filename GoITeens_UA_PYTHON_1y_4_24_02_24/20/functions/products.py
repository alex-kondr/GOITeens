def show_prods(products: list) -> None:
    delimeter = "-" * 28
    template = "|{:<5}|{:<20}|"
    print(delimeter)
    print(template.format("№", "Назва товару"))
    print(delimeter)
    for i, product in enumerate(products, start=1):
        print(template.format(i, product))
    print(delimeter)


def add_prod(products: list) -> list:
    product = input("Введіть новий товар для додавання до списку: ")

    if product not in products:
        products.append(product)
        print(f"\nТовар '{product}' доданий до списку")
    else:
        print("\nТакий товар вже є у списку")

    return products


def add_prods(products: list) -> list:
    prods = input("Введіть список товар для додавання через пробіл\n-> ")
    prods = prods.split()
    products.extend(prods)
    print("\nСписок товарів розширено")
    return products


def del_prod_by_name(products: list) -> list:
    product = input("Введіть назву товару для видалення зі списку товарів: ")

    if product in products:
        products.remove(product)
        print(f"\nТовар '{product}' видалено зі списку")
    else:
        print("\nТакого товару немає у списку")

    return products


def del_prod_by_num(products: list[str]) -> list[str]:
    index = input("Введіть номер товару для видалення: ")

    if index and index.isdigit() and 0 < int(index) <= len(products):
        product = products.pop(int(index) - 1)
        print(f"Товар '{product}' видалено ")
    else:
        print("Ви ввели не вірний номер товару")

    return products


def sort(products: list) -> None:
    print()
    prods = sorted(products)
    for product in prods:
        print(product)


def sold_prod(products: list[str], products_sold: list[str]) -> tuple:
    product = input("Введіть назву товару для продажу: ")

    if product in products:
        products.remove(product)
        products_sold.append(product)
        print(f"\nТовар '{product}' продано")
    else:
        print("\nТакого товару немає у списк")

    return products, products_sold


def find_prod_by_name(products: list) -> None:
    product = input("Введіть назву товару для пошуку: ")

    if product in products:
        index = products.index(product)
        print(f"Товар '{product}' знаходиться під номером {index + 1}")
    else:
        print("\nТакого товару немає у списку")


def show_history(products_sold: list) -> None:
    prods_sold = products_sold[::-1]
    for product in prods_sold:
        print(product)


def palindrome(products: list) -> None:
    palin_prods = [product for product in products if product.lower() == product[::-1].lower()]
    print(f"\nУ списку з продуктами є такі слова-паліндроми: {palin_prods}\n")
