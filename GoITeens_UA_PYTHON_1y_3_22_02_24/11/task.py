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
    "6. Показати відсортований список товарів за ім'ям",
    "7. Продати товар",
    "8. Знайти номер товару за ім'ям",
    "9. Показати список проданих товарів",
    "10. Показати історію продажів",
    "11. Вийти з програми",
    "12. Написати відгук",         ######################################
    "13. Знайти групи символів, які повторюються (використовуючи всі відгуки)",    ############################
    "14. Знайти продукти, які є паліндромами"            ################################
]
PASSWORD = ""

while not PASSWORD:
    command = input("Введіть 1 для введення свого паролю;\nВведіть 2 для автоматичної генерації паролю.\nАбо будь який символ для виходу з програми\n-> ")

    if command == "1":
        password = input("Введіть свій пароль. Пароль повинен бути не менше 8 символів, а також містити 1 букву та 1 цифру\n-> ")

        pass_len = False if len(password) < 8 else True
        pass_digit = False
        pass_char = False

        for char in password:
            if char.isdigit():
                pass_digit = True
            if char.isalpha():
                pass_char = True

        if pass_len and pass_digit and pass_char:
            PASSWORD = password
        else:
            print("Пароль не пройшов перевірку. Спробуйте ще раз.\n")

    if command == "2":
        pass_chars = string.ascii_lowercase + string.digits

        len_password = input("Введіть довжину паролю, або залиште за замовчуванням (8 символів): ")
        if len_password.isdigit() and int(len_password) >= 8:
            len_password = int(len_password)
        else:
            len_password = 8

        is_upper = input("Чи використовувати великі літери: 1 - так, інший символ - ні\n->")
        if is_upper == "1":
            pass_chars += string.ascii_uppercase

        is_punctuation = input("Чи використовувати спецсимволи: 1 - так, інший символ - ні\n->")
        if is_punctuation == "1":
            pass_chars += string.punctuation

        is_repeate = input("Чи можуть символи паролю повторюватись: 1 - так, інший символ - ні\n->")
        if is_repeate == "1":
            password = []
        else:
            password = set()

        pass_digit = False
        pass_char = False

        while len(password) < len_password or not pass_digit or not pass_char:
            char = random.choice(pass_chars)

            if char.isdigit():
                pass_digit = True
            elif char.isalpha():
                pass_char = True

            if isinstance(password, list):
                password.append(char)
            elif isinstance(password, set):
                password.add(char)
        else:
            PASSWORD = "".join(password)
else:
    print(f"\nВаш пароль '{PASSWORD}' успішно створено. Запам'ятайте його для входу в систему.\n")

while True:
    print()
    for command in COMMANDS:
        print(command)

    command = input("Введіть номер команди: ")

    if command == "1":
        for i, product in enumerate(PRODUCTS, start=1):
            print(f"{i}. {product}")

        input("\nНатисніть 'Enter' для продовження ")

    elif command == "2":
        product = input("Введіть новий товар для додавання до списку: ")

        if product not in PRODUCTS:
            PRODUCTS.append(product)
            input(f"\nТовар '{product}' доданий до списку. Натисніть 'Enter' для продовження ")
        else:
            input("\nТакий товар вже є у списку. Натисніть 'Enter' для продовження ")

    elif command == "3":
        prods = input("Введіть список товар для додавання через пробіл\n-> ")
        prods = prods.split()
        PRODUCTS.extend(prods)
        input("\nСписок товарів розширено. Натисніть 'Enter' для продовження ")

    elif command == "4":
        product = input("Введіть назву товару для видалення зі списку товарів: ")

        if product in PRODUCTS:
            PRODUCTS.remove(product)
            input(f"\nТовар '{product}' видалено зі списку. Натисніть 'Enter' для продовження ")
        else:
            input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")

    elif command == "5":
        index = input("Введіть номер товару для видалення: ")

        if index and index.isdigit() and 0 < int(index) <= len(PRODUCTS):
            product = PRODUCTS.pop(int(index) - 1)
            input(f"Товар '{product}' видалено. Натисніть 'Enter' для продовження ")
        else:
            input("Ви ввели не вірний номер товару. Натисніть 'Enter' для продовження ")

    elif command == "6":
        print()
        prods = sorted(PRODUCTS)
        for product in prods:
            print(product)

        input("\nНатисніть 'Enter' для продовження ")

    elif command == "7":
        product = input("Введіть назву товару для продажу: ")

        if product in PRODUCTS:
            PRODUCTS.remove(product)
            PRODUCTS_SOLD.append(product)
            input(f"\nТовар '{product}' продано. Натисніть 'Enter' для продовження ")
        else:
            input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")

    elif command == "8":
        product = input("Введіть назву товару для пошуку: ")

        if product in PRODUCTS:
            index = PRODUCTS.index(product)
            input(f"Товар '{product}' знаходиться під номером {index + 1}. Натисніть 'Enter' для продовження ")
        else:
            input("\nТакого товару немає у списку. Натисніть 'Enter' для продовження ")

    elif command == "9":
        if not PRODUCTS_SOLD:
            print("Список проданих товарів пустий")

        for product in PRODUCTS_SOLD:
            print(product)

        input("\nНатисніть 'Enter' для продовження ")

    elif command == "10":
        prods_sold = PRODUCTS_SOLD[::-1]
        for product in prods_sold:
            print(product)

        input("\nНатисніть 'Enter' для продовження ")

    elif command == "11":
        print("До побачення")
        break
