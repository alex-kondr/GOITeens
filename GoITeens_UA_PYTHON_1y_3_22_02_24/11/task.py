import string
import random

PRODUCTS = [
    "Гречка",
    "леонід",
    "Цукорій",
    "Макарони",
    "Йогурт",
    "Спагеті",
    "Картопля",
    "Буряк",
    "Морква",
    "Локшина",
    "Дмитро",
    "Айзен",
    "Петух",
    "російське немовля",
    "Капуста",
    "Капуста",
    "Дондон",
    "Цибуля",
    "Часник",
    "Борошно",
    "Яйця",
    "Бульба",
    "Соняшникова олія",
    "Вершкове масло",
    "Сіль",
    "Додод",
    "Перець",
    "Цукор",
    "Оцет",
    "Сода",
    "Чай",
    "Кава",
    "Око",
    "Зараз"
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
REVIEWS = ["Дуже гарний товар", "ПРОДУКТИ НЕ ДУЖЕ", "дуже погане ставлення від працівників", "Якість товарів просто супер", "Дуже погана як", "Великий асортимент", "Я БІЛЬШЕ СЮДИ НЕ ПОВЕРНУСЬ!!!", "Мені сподобався Ваш магазин", "Якість Во👍", "Боже, яке кчне...💅"]
TEMPLATE = "|{:^5}|{:<100}|"
DELIMITER = "—" * 108
HEAD = TEMPLATE.format("№", "Назва товару")

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

    elif command == "2":
        pass_chars = string.ascii_lowercase + string.digits

        len_password = input("Введіть довжину паролю, або залиште за замовчуванням (8 символів): ")
        len_password = int(len_password) if len_password.isdigit() and int(len_password) > 8 else 8

        is_upper = input("Чи використовувати великі літери: 1 - так, інший символ - ні\n->")
        pass_chars += string.ascii_uppercase if is_upper == "1" else ""

        is_punctuation = input("Чи використовувати спецсимволи: 1 - так, інший символ - ні\n->")
        pass_chars += string.punctuation if is_punctuation == "1" else ""

        is_repeate = input("Чи можуть символи паролю повторюватись: 1 - так, інший символ - ні\n->")
        password = [] if is_repeate == "1" else set()

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

password = input("Введіть свій пароль для входу в систему: ")

command = None
while password==PASSWORD:
    if not command:
        print("Доброго дня. Вітаємо в нашій інформаційній системі")

    print()
    print(DELIMITER)
    print(HEAD)
    print(DELIMITER)
    for i, command in enumerate(COMMANDS, start=1):
        print(TEMPLATE.format(i, command))

    command = input("Введіть номер команди: ")

    if command == "1":
        print(DELIMITER)
        print(HEAD)
        print(DELIMITER)
        for i, product in enumerate(PRODUCTS, start=1):
            print(TEMPLATE.format(i, product))

        print(DELIMITER)
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

    elif command == "5 ":
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
        review = input("Залиште свій відгук:\n")
        REVIEWS.append(review)

    elif command == "13":
        reviews = " ".join(REVIEWS)

        repeated_groups = set()
        for i in range(len(reviews)):
            for j in range(i+1, len(reviews)):
                slice = reviews[i:j]
                if reviews.count(slice) >= 2:
                    repeated_groups.add(slice)

        input(f"Список груп символів, які повторюються не менше 2 разів:\n{repeated_groups}")

    elif command == "14":
        palin_prod = []
        for product in PRODUCTS:
            if product.lower() == product[::-1].lower():
                palin_prod.append(product)

        input(f"В списку товарів є такі слова-паліндроми:\n{palin_prod}") if palin_prod else input("В списку товарів відсутні слова паліндроми.")
else:
    print("Пароль невірний, доступ заборонено")
