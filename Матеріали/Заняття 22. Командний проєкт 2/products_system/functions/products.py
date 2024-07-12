from log.log import bot_log

from functions import save_files, open_files


def add_prod(products: list) -> list:
    product = input("Введіть новий товар для додавання до списку: ")

    if product not in products:
        products.append(product)
        print(f"\nТовар '{product}' доданий до списку")
    else:
        print("\nТакий товар вже є у списку")

    # save_products((products))


def del_prod_by_name(product: list) -> None:
    products = open_files.products

    if product in products:
        products.remove(product)
        bot_log(f"\nТовар '{product}' видалено зі списку")
    else:
        bot_log("\nТакого товару немає у списку")

    save_files.save_products((products))


def sold_prod(product) -> None:
    products = open_files.products
    products_sold = open_files.products_sold

    if product in products:
        products.remove(product)
        products_sold.append(product)
        bot_log(f"\nТовар '{product}' продано. Натисніть 'Enter' для продовження ")
    else:
        bot_log("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")

    save_files.save_products(products)
    save_files.save_products_sold(products_sold)


def show_sold_prods(products_sold: list) -> None:
    if not products_sold:
        print("Список проданих товарів пустий")

    for product in products_sold:
        print(product)


def show_sales_history(products_sold: list) -> None:
    prods_sold = products_sold[::-1]
    for product in prods_sold:
        print(product)


def find_palidrome(products: list) -> None:
    palin_prod = []
    for product in products:
        if product.lower() == product[::-1].lower():
            palin_prod.append(product)

    message = f"В списку товарів є такі слова-паліндроми:\n{palin_prod}" if palin_prod else "В списку товарів відсутні слова паліндроми."
    print(message)
