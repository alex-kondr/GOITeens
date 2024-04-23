import string
import random


PRODUCTS = [
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
PRODUCTS_SOLD = []
COMMANDS = [

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
PASSWORD = ""

# Створюємо пароль для входу
while True:
    command = input("\
        Введіть 1 для введення свого паролю;\n\
        Введіть 2 для автоматичної генерації паролю;\n\
        Будь яка інша команда для виходу з програми")

    if command == "1":
        password = input("Введіть свій пароль (повинен містити не менше 8 символів, а також повинен містити хоча б одну букву та одну цифру)")

        pass_len = True if len(password) >= 8 else False
        pass_digit = False
        pass_alpha = False

        for char in password:
            if char.isdigit():
                pass_digit = True

            if char.isalpha():
                pass_alpha = True

        if pass_len and pass_digit and pass_alpha:
            PASSWORD = password
            print("Пароль успішно створено")
            break
        else:
            print("Пароль не пройшов перевірку, введіть новий пароль або згенеруйте автоматичний пароль")

    elif command == "2":
        chars_for_pass = string.ascii_lowercase + string.digits

        is_upper = input("Чи використовувати великі букви? 1 - так, будь який інший символ - ні")
        if is_upper == "1":
            chars_for_pass += string.ascii_uppercase

        is_punctuatio = input("Чи використовувати спецсимволи? (1 - так, будь який інший символ - ні)")
        if is_punctuatio == "1":
            chars_for_pass += string.punctuation

        len_pass = input("Введіть довжину пароля (не менше 8)")
        pass_digit = False
        pass_alpha = False
        password = ""
        # while not: pass
        #     password = random.choice(chars_for_pass)


        #     for char in password:
        #         if char.isdigit():
        #             pass_digit = True

        #         if char.isalpha():
        #             pass_alpha = True


    else:
        print("Ви вийшли з програми. До побачення")
        break

while PASSWORD:
    print("Введіть номер команди")
    for command in COMMANDS:
        print(command)

    command = input("-> ")

    if not command.isdigit():
        print("Не відома команда")
        input("Натисніть 'Enter' для продовження")
        continue

    if command == "1":
        for i in range(len(PRODUCTS)):
            print(f"{i + 1}. {PRODUCTS[i]}")

        input("Натисніть 'Enter' для продовження")

    elif command == "2":
        product = input("Введіть назву товару: ")

        if product not in PRODUCTS:
            PRODUCTS.append(product)
            print(f"Товар '{product}' додано до списку")
        else:
            print("Такий товар вже наявний у списку")

        input("Натисніть 'Enter' для продовження")

    elif command == "3":
        prods = input("Введіть список товарів через пробіл:\n")
        prods = prods.split()
        PRODUCTS.extend(prods)
        input("Натисніть 'Enter' для продовження")

    elif command == "4":
        product = input("Введіть назву товару для видалення: ")
        if product in PRODUCTS:
            PRODUCTS.remove(product)
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
        if not(0 <= product_index < len(PRODUCTS)):
            print("Такого номеру товару немає у списку")
            input("Натисніть 'Enter' для продовження")
            continue

        product = PRODUCTS.pop(product_index)
        print(f"Товар '{product}' видалено")
        input("Натисніть 'Enter' для продовження")

    elif command == "6":
        PRODUCTS.sort()
        print("Список відсортовано")
        input("Натисніть 'Enter' для продовження")

    elif command == "7":
        product = input("Введіть назву товару для продажу: ")

        if product not in PRODUCTS:
            print("Такого товару немає")
            input("Натисніть 'Enter' для продовження")
            continue

        PRODUCTS.remove(product)
        PRODUCTS_SOLD.append(product)
        input("Натисніть 'Enter' для продовження")

    elif command == "8":
        product = input("Введіть назву товару для пошуку: ")

        if product not in PRODUCTS:
            print("Такого товару немає")
            input("Натисніть 'Enter' для продовження")
            continue

        product_index = PRODUCTS.index(product)
        print(f"Товар '{product}' знаходиться під номером '{product_index + 1}'")
        input("Натисніть 'Enter' для продовження")

    elif command == "9":
        if not PRODUCTS_SOLD:
            print("Сьогодні ще нічого не продано")
            input("Натисніть 'Enter' для продовження")
            continue

        print("Сьогодні продано такі товари:")
        for i, product in enumerate(PRODUCTS_SOLD):
            print(f"{i + 1}. {product}")

        input("Натисніть 'Enter' для продовження")

    elif command == "10":
        if not PRODUCTS_SOLD:
            print("Сьогодні ще нічого не продано")
            input("Натисніть 'Enter' для продовження")
            continue

        PRODUCTS_temp = PRODUCTS_SOLD.copy()
        PRODUCTS_temp.reverse()
        print("Історія продажу товарів")
        for product in PRODUCTS_temp:
            print(product)

        input("Натисніть 'Enter' для продовження")

    elif command == "11":
        print("Дякую що були з нами")
        break
