def show_all_prods(products: list) -> None:
    template = "|{:^5}|{:<100}|"
    delimiter = "—" * 108
    head = template.format("№", "Назва товару")
    print(delimiter)
    print(head)
    print(delimiter)
    for i, product in enumerate(products, start=1):
        print(template.format(i, product))

    print(delimiter)


def add_prod(products: list) -> list:
    product = input("Введіть новий товар для додавання до списку: ")

    if product not in products:
        products.append(product)
        input(f"\nТовар '{product}' доданий до списку. Натисніть 'Enter' для продовження ")
    else:
        input("\nТакий товар вже є у списку. Натисніть 'Enter' для продовження ")

    return products


def add_prods(products: list) -> list:
    prods = input("Введіть список товар для додавання через пробіл\n-> ")
    prods = prods.split()
    products.extend(prods)
    input("\nСписок товарів розширено. Натисніть 'Enter' для продовження ")
    return products


def del_prod_by_name(products: list) -> list:
    product = input("Введіть назву товару для видалення зі списку товарів: ")

    if product in products:
        products.remove(product)
        input(f"\nТовар '{product}' видалено зі списку. Натисніть 'Enter' для продовження ")
    else:
        input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")

    return products


def del_prod_by_numb(products: list) -> list:
    index = input("Введіть номер товару для видалення: ")

    if index and index.isdigit() and 0 < int(index) <= len(products):
        product = products.pop(int(index) - 1)
        input(f"Товар '{product}' видалено. Натисніть 'Enter' для продовження ")
    else:
        input("Ви ввели не вірний номер товару. Натисніть 'Enter' для продовження ")

    return products


def show_sorted_prods(products: list) -> None:
    print()
    prods = sorted(products)
    for product in prods:
        print(product)


def find_numb_prod_by_name(products: list) -> None:
    product = input("Введіть назву товару для пошуку: ")

    if product in products:
        index = products.index(product)
        input(f"Товар '{product}' знаходиться під номером {index + 1}. Натисніть 'Enter' для продовження ")
    else:
        input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")


def show_sold_prods(products_sold: list) -> None:
    if not products_sold:
        print("Список проданих товарів пустий")

    for product in products_sold:
        print(product)


def show_sales_history(products_sold: list) -> None:
    prods_sold = products_sold[::-1]
    for product in prods_sold:
        print(product)


def sold_prod(products: list[str], products_sold: list[str]) -> tuple[list, list]:
    product = input("Введіть назву товару для продажу: ")

    if product in products:
        products.remove(product)
        products_sold.append(product)
        input(f"\nТовар '{product}' продано. Натисніть 'Enter' для продовження ")
    else:
        input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")

    return products, products_sold


def find_palidrome(products: list) -> None:
    palin_prod = []
    for product in products:
        if product.lower() == product[::-1].lower():
            palin_prod.append(product)

    print(f"В списку товарів є такі слова-паліндроми:\n{palin_prod}") if palin_prod else print("В списку товарів відсутні слова паліндроми.")
