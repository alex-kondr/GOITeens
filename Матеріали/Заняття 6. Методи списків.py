# pip install faker

# import random
# from faker import Faker

# fake = Faker("uk_UA")

# students = []

# for _ in range(50):
#     first_name = fake.first_name()
#     middle_name = fake.middle_name()
#     last_name = fake.last_name()

#     students.append([first_name, middle_name, last_name])

# print(students)

# for student in students:
#     if student[2].startswith("А"):
#         print(student)

# random.randint(15, 60)

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
    print("Введіть номер команди")
    for command in commands:
        print(command)

    command = input("-> ")

    if not command.isdigit():
        print("Не відома команда")
        input("Натисніть 'Enter' для продовження")
        continue

    if command == "1":
        for i in range(len(products)):
            print(f"{i + 1}. {products[i]}")

        input("Натисніть 'Enter' для продовження")

    elif command == "2":
        product = input("Введіть назву товару: ")

        if product not in products:
            products.append(product)
            print(f"Товар '{product}' додано до списку")
        else:
            print("Такий товар вже наявний у списку")

        input("Натисніть 'Enter' для продовження")

    elif command == "3":
        prods = input("Введіть список товарів через пробіл:\n")
        prods = prods.split()
        products.extend(prods)
        input("Натисніть 'Enter' для продовження")

    elif command == "4":
        product = input("Введіть назву товару для видалення: ")
        if product in products:
            products.remove(product)
        else:
            print("Такого товару немає у списку")

        input("Натисніть 'Enter' для продовження")

    elif command == "5":
        product_index = input("Введіть номер товару, щоб видалити: ")
        if not product_index.isdigit():
            print("Це не номер")
            input("Натисніть 'Enter' для продовження")
            continue

        product_index = int(product_index) - 1
        if not(0 <= product_index < len(products)):
            print("Такого номеру товару немає у списку")
            input("Натисніть 'Enter' для продовження")
            continue

        product = products.pop(product_index)
        print(f"Товар '{product}' видалено")
        input("Натисніть 'Enter' для продовження")

    elif command == "6":
        products.sort()
        print("Список відсортовано")
        input("Натисніть 'Enter' для продовження")

    elif command == "7":
        product = input("Введіть назву товару для продажу: ")

        if product not in products:
            print("Такого товару немає")
            input("Натисніть 'Enter' для продовження")
            continue

        products.remove(product)
        products_sold.append(product)
        input("Натисніть 'Enter' для продовження")

    elif command == "8":
        product = input("Введіть назву товару для пошуку: ")

        if product not in products:
            print("Такого товару немає")
            input("Натисніть 'Enter' для продовження")
            continue

        product_index = products.index(product)
        print(f"Товар '{product}' знаходиться під номером '{product_index + 1}'")
        input("Натисніть 'Enter' для продовження")

    elif command == "9":
        if not products_sold:
            print("Сьогодні ще нічого не продано")
            input("Натисніть 'Enter' для продовження")
            continue

        print("Сьогодні продано такі товари:")
        for i, product in enumerate(products_sold):
            print(f"{i + 1}. {product}")

        input("Натисніть 'Enter' для продовження")

    elif command == "10":
        if not products_sold:
            print("Сьогодні ще нічого не продано")
            input("Натисніть 'Enter' для продовження")
            continue

        products_temp = products_sold.copy()
        products_temp.reverse()
        print("Історія продажу товарів")
        for product in products_temp:
            print(product)

        input("Натисніть 'Enter' для продовження")

    elif command == "11":
        print("Дякую що були з нами")
        break
