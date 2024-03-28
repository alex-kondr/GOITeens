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
    print()
    for command in commands:
        print(command)

    command = input("Введіть номер команди: ")

    if command == "1":
        for i in range(len(products)):
            print(f"{i + 1}. {products[i]}")

        input("\nНатисніть 'Enter' для продовження ")

    elif command == "2":
        product = input("Введіть новий товар для додавання до списку: ")

        if product in products:
            print("\nТакий товар вже є у списку")
            input("\nНатисніть 'Enter' для продовження ")
            continue

        products.append(product)
        print(f"Товар '{product}' доданий до списку")
        input("\nНатисніть 'Enter' для продовження ")

    elif command == "3":
        prods = input("Введіть список товар для додавання через пробіл\n-> ")
        products.extend(prods)
        print("Список товарів розширено")
        input("\nНатисніть 'Enter' для продовження ")

    elif command == "4":
        product = input("Введіть назву товару для видалення зі списку товарів: ")

        if product not in products:
            print("Такого товару немає у списку")
            input("\nНатисніть 'Enter' для продовження ")
            continue

        products.remove(product)
        print(f"Товар '{product}' видалено зі списку")
        input("\nНатисніть 'Enter' для продовження ")


# my_list1 = []
# my_list2 = []
# my_list1.extend(my_list2)
# my_list1.sort()
# print(my_list1)

students = [["Андрій", "Іванов"], ["Андрій", "Нікітенко"], ["Адам", "Баранов"]]

count = 0
for student in students:
    if student[0] == "Андрій":
        count += 1

print(count)
# print(students.count(["Андрій", "Іванов"]))