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
    "Показати список наявних товарів",
    "Додати новий товар до списку",
    "Додати список товарів",
    "Видалити товар за ім'ям",
    "Видалити товар за номер",
    "Показати відсортований список товарів за ім'ям",
    "Продати товар",
    "Знайти номер товару за ім'ям",
    "Показати список проданих товарів",
    "Показати історію продажів",
    "Вийти з програми",
    "Написати відгук",         ######################################
    "Знайти групи символів, які повторюються (використовуючи всі відгуки)",    ############################
    "Знайти продукти, які є паліндромами"            ################################
]
PASSWORD = ""
REVIEWS = []
DELIMETER = "-" * 78
TEMPLATE = "|{:^5}|{:<70}|"

while not PASSWORD:
    command = input("Введіть 1 для введення свого паролю.\n"
                    "Введіть 2 для автоматичного створення паролю.\n"
                    "Введіть будь який інший символ для виходу з програми: ")

    if command == "1":
        password = input("Введіть свій пароль. Пароль повинен містити не менше 8 символів, містити принаймні одну літеру та одну цифру\n-> ")

        pass_len = True if len(password) >= 8 else False
        pass_alpha = False
        pass_digit = False

        for char in password:
            if char.isalpha():
                pass_alpha = True
            elif char.isdigit():
                pass_digit = True

        if pass_len and pass_alpha and pass_digit:
            PASSWORD = password
        else:
            input("\nПароль не пройшов перевірку. Спробуйте ще раз")

    elif command == "2":
        chars_for_pass = string.ascii_lowercase + string.digits

        len_password = input("Введіть довжину пароль не меншу 8, або залиште за замовчуванням (8 символів): ")
        len_password = int(len_password) if len_password.isdigit() and int(len_password) >= 8 else 8

        is_upper = input("Чи використовути великі літери? Введіть 1 - так, будь який інший символ ні: ")
        chars_for_pass += string.ascii_uppercase if is_upper == "1" else ""

        is_punctuation = input("Чи використовути спецсимволи? Введіть 1 - так, будь який інший символ ні: ")
        chars_for_pass += string.punctuation if is_punctuation == "1" else ""

        is_repeate = input("Чи можуть символи паролю повторюватись? 1 - так, будь який інший символ - ні: ")
        password = [] if is_repeate == "1" else set()
        pass_alpha = False
        pass_digit = False

        while len(password) < len_password or not pass_alpha or not pass_digit:
            char = random.choice(chars_for_pass)
            if char.isalpha():
                pass_alpha = True
            elif char.isdigit():
                pass_digit = True

            if isinstance(password, list):
                password.append(char)
            elif isinstance(password, set):
                password.add(char)
        else:
            PASSWORD = "".join(password)

    else:
        print("Ви вийшли з програми")
        break
else:
    input(f"Пароль успіщно створено '{PASSWORD}'. Запам'ятайте його. Натисніть 'enter' для продовження\n")

password = input("Введіть пароль для входу в систему: ")

command = None
while password == PASSWORD:
    if not command:
        input("\nПароль введено вірно. Вітаємо нашій інформаційній системі.\n")

    print(DELIMETER)
    print(TEMPLATE.format("№", "Команда"))
    print(DELIMETER)
    for i in range(1, len(COMMANDS)):
        print(TEMPLATE.format(i, COMMANDS[i-1]))
    print(DELIMETER)

    command = input("Введіть номер команди: ")

    if command == "1":
        print(DELIMETER)
        print(TEMPLATE.format("№", "Назва товару"))
        print(DELIMETER)
        for i, product in enumerate(PRODUCTS, start=1):
            print(TEMPLATE.format(i, product))
        print(DELIMETER)

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

    elif command == "12":
        review = input("Залиште свій відгук\n->")
        REVIEWS.append(review)
        input("Ваш відгук успішно збережено.\nНатисніть 'Enter' для продовження ")

    elif command == "13":
        reviews = " ".join(REVIEWS).lower()

        # repeated_groups = {reviews[i:j] for i in range(len(reviews)) for j in range(i+1, len(reviews)) if reviews.count(reviews[i:j]) >= 2}

        repeated_groups = set()
        for i in range(len(reviews)):
            for j in range(i+1, len(reviews)):
                if reviews.count(reviews[i:j]) >= 2:
                    repeated_groups.add(reviews[i:j])

        input(f"Групи символів, які повторюються не менше двох разів у відгуках:\n{repeated_groups}\n")

    elif command == "14":
        palin_prods = [product for product in PRODUCTS if product.lower() == product[::-1].lower()]
        input(f"\nУ списку з продуктами є такі слова-паліндроми: {palin_prods}\n")

else:
    print("Не вірний пароль. Доступ заборонено. До побачення.")