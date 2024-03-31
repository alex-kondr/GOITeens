products = [
    "Гречка",
    "Макарони",
    "Спагеті",
    "Картопля",
    "Буряк",
    "Морква",
    "Капуста",
    "Цибуля",
    "Часник",
    "Борошно",
    "Яйця",
    "Соняшникова олія",
    "Вершкове масло",
    "Сіль",
    "Перець",
    "Цукор",
    "Оцет",
    "Сода",
    "Чай",
    "Кава"
]

products_sold = []

commands = [
    "1. Показати список наявних товарів",
    "2. Додати новий товар до списку",
    "3. Додати список товарів",
    "4. Видалити товар за ім'ям",
    "5. Видалити товар за номер",
    "6. Відсортувати список товарів за ім'ям",
    "7. Продати товар",
    "8. Знайти номер товару за ім'ям",
    "9. Показати список проданих товарів",
    "10. Показати історію продажів",
    "11. Вийти з програми"
]

while True:
    for command in commands:
        print(command)

    command = input("\nВведіть номер дії: ")

    if command == "1":
        for i, product in enumerate(products):
            print(f"{i + 1}. {product}")

        input("\nНасніть Enter для продовження ")

    elif command == "2":
        product = input("Введіть назву товару для додавання до списку: ")

        if product not in products:
            products.append(product)
            print(f"Товар '{product}' доданий до списку")
            input("\nНасніть Enter для продовження ")
        else:
            print("Такий товар вже є у списку")
            input("\nНасніть Enter для продовження ")

    elif command == "3":
        prods = []

        while True:
            product = input("Введіть назву товара або 'stop': ")

            if not product or product == "stop":
                break

            prods.append(product)

        products.extend(prods)
        input("Список продуків розширено. Для продовження натисніть Enter ")


    elif command == "4":
        product = input("Введіть назву товару для видалення зі списку: ")

        if product in products:
            products.remove(product)
            input(f"Товар '{product}' видалено. Для продовження натисніть Enter ")
        else:
            input("Такого товару немає у списку. Насніть Enter для продовження ")

    elif command == "5":
        number = input("Введіть номер товару для видалення: ")

        if number.isdigit() and 0 < int(number) <= len(products):
            product = products.pop(int(number) - 1)
            input(f"Товар '{product}' видалено. Насніть Enter для продовження ")
        else:
            input("Ви ввели не вірний номер. Насніть Enter для продовження ")

    elif command == "6":
        products.sort()
        input("Список товарів відсортовано. Насніть Enter для продовження ")

    elif command == "7":
        product = input("Введіть назву товару для продажу: ")

        if product in products:
            products.remove(product)
            products_sold.append(product)
            input("Товар продано. Насніть Enter для продовження ")
        else:
            input("Товару немає в наявності. Насніть Enter для продовження ")

    elif command == "8":
        product = input("Введіть назву товару для пошуку: ")

        if product in products:
            index = products.index(product)
            input(f"Товар знаїодиться під номером {index + 1}. Насніть Enter для продовження ")
        else:
            input("Товару немає в наявності. Насніть Enter для продовження ")

    elif command == "9":
        for product in products_sold:
            print(product)

        input("\nНасніть Enter для продовження ")

    elif command == "10":
        sort_products_sold = products_sold[::-1]
        for product in sort_products_sold:
            print(product)

        input("\nНасніть Enter для продовження ")

    elif command == "11":
        print("Дякую за співрпацю")
        break
