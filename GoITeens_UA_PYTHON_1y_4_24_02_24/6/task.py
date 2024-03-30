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
        for i in range(len(products)):
            print(f"{i + 1}. {products[i]}")

        input("\nНасніть Enter для продовження ")

    elif command == "2":
        product = input("Введіть назву товару для додавання до списку: ")

        if product in products:
            print("Такий товар вже є у списку")
            input("\nНасніть Enter для продовження ")
            continue

        products.append(product)
        print(f"Товар '{product}' доданий до списку")
        input("\nНасніть Enter для продовження ")

    elif command == "3":
        prods = input("Введіть список товарів для додавання до списку через пробіл\n-> ")
        prods = prods.split()
        products.extend(prods)
        print("Список товарів розширено")
        input("\nНасніть Enter для продовження ")

    elif command == "4":
        product = input("Введіть назву товару для видалення зі списку: ")

        if product not in products:
            print("Такого товару немає у списку")
            input("\nНасніть Enter для продовження ")
            continue

        products.remove(product)
        print(f"Товар '{product}' видалено")
        input("\nНасніть Enter для продовження ")

    elif command == "5":
        number = input("Введіть номер товару для видалення: ")

        if number.isdigit() and 0 < int(number) <= len(products):
            product = products.pop(int(number) - 1)
            print(f"Товар '{product}' видалено")
            input("\nНасніть Enter для продовження ")
