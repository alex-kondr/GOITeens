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

    command = input("\nВведіть номер команди: ")

    if command == "1":
        for i, product in enumerate(products, start=1):
            print(f"{i}: {product}")

        input("\nНатисніть 'enter' для продовження\n")

    elif command == "2":
        product = input("\nВведіть новий товар для додавання до списку: ")

        if product in products:
            input("\nТакий товар вже доданий\nНатисніть 'enter' для продовження\n")
        else:
            products.append(product)
            input("\nНовий товар доданий до списку\nНатисніть 'enter' для продовження\n")

    elif command == "3":
        prods = input("\nВведіть список товарів через пробіл:\n").split()
        products.extend(prods)
        input("\nСписок продуктів розширено\nНатисніть 'enter' для продовження\n")

    elif command == "4":
        product = input("Введіть назву товару для видалення: ")

        if product in products:
            products.remove(product)
            input(f"\nТовар '{product}' видалено зі списку\nНатисніть 'enter' для продовження\n")
        else:
            input(f"\nТовар '{product}' відсутній у списку\nНатисніть 'enter' для продовження\n")

    elif command == "5":
        number = input("Введіть номер товару для видалення: ")

        if number.isdigit() and 0 < int(number) <= len(products):
            product = products.pop(int(number) - 1)
            input(f"\nТовар '{product}' видалено зі списку\nНатисніть 'enter' для продовження\n")
        else:
            input("\nВвели невірний номер")

    elif command == "6":
        prods = sorted(products)

        for i, prod in enumerate(prods, start=1):
            print(f"{i}: {prod}")

        input("\nСписок товарі відсортовано\nНатисніть 'enter' для продовження\n")

    elif command == "7":
        product = input("Введіть товар для продажу: ")

        if product in products:
            products.remove(product)
            products_sold.append(product)
            input(f"Товар '{product}' продано\nНатисніть 'enter' для продовження\n")
        else:
            input(f"Товар '{product}' відсутній у списку")

    elif command == "8":
        product = input("Введіть назву товару для пошуку: ")

        if product in products:
            index = products.index(product)
            input(f"\nТовар '{product}' знаходить під номер '{index + 1}'\nНатисніть 'enter' для продовження\n")
        else:
            input(f"\nТовар '{product}' відсутній у списку")

    elif command == "9":
        print("\nСписок проданий товарів\n")
        for i, product in enumerate(products_sold, start=1):
            print(f"{i}: {product}")

        input("\nНатисніть 'enter' для продовження\n")

    elif command == "10":
        prods_sold = products_sold[::-1]

        if not prods_sold:
            input("\nСписок проданих товарів порожній\n")

        print("\nІсторія продажу\n")
        for product in prods_sold:
            print(product)

        input("\nНатисніть 'enter' для продовження\n")

    elif command =="11":
        print("\nДякую що були з нами. Чекаємо наступної зустрічі.\n")
        break
