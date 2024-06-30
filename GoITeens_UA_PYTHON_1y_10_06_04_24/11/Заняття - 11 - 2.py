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
    "Кава",
    "Око",
    "Зараз"
]

PRODUCTS_SOLD = []
PASSWORD = ""
REVIEWS = ["Чудове обслуговування", "Такий собі продуктовий магазин", "свіжі товари", "не свіжі товари", "Чудовий магазин,не один раз вже тут купую продукти"]

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
    "11. Вийти з програми",
    "12. Написати відгук",         ######################################
    "13. Знайти групи символів, які повторюються (використовуючи всі відгуки)",    ############################
    "14. Знайти назви продуктів, які є паліндромами",            ################################
    "15. Показати відгуки"                               ###############################
]

DELIMITER = "-" * 28
TEMPLATE = "|{:<5}|{:<20}|"

while not PASSWORD:
    command = input("Потрібно створити пароль для можливості працювати в системі.\n"
                    "Введіть 1 - для введення свого паролю.\n"
                    "Введіть 2 - для автоматичної генерації паролю\n-> ")

    if command == "1":
        password = input("Введіть свій пароль. Довжина паролю має бути не менше 8 символіd, містити мінім одна буква та одну цифру.\n-> ")

        if len(password) >= 8:
            is_len_pass = True
        else:
            is_len_pass = False

        is_have_digit = False
        is_have_char = False

        for char in password:
            if char.isalpha():
                is_have_char = True
            elif char.isdigit():
                is_have_digit = True

        if is_len_pass and is_have_digit and is_have_char:
            PASSWORD = password
        else:
            input("Ваш пароль не пройшов перевірку. Спробуйте ще раз. 'Enter' для проовження ")

    elif command == "2":
        string_password = string.ascii_lowercase + string.digits

        len_password = input("Введіть довжину паролю, мінім 8 символів: ")
        if len_password.isdigit() and int(len_password) > 8:
            len_password = int(len_password)
        else:
            len_password = 8

        is_upper = input("Чи використовувати великі літери для генерації паролю: 1 - так, будь який інший символ - ні -> ")
        if is_upper == "1":
            string_password += string.ascii_uppercase

        is_punctuation = input("Чи використовувати спецсимволи для генерації паролю: 1 - так, будь який інший символ - ні -> ")
        if is_punctuation == "1":
            string_password += string.punctuation

        is_repeat = input("Чи можуть символи у паролю повторюватись. 1 - так, будь який інший символ - ні -> ")
        if is_repeat == "1":
            password = random.choices(string_password, k=len_password)
        else:
            password = random.sample(string_password, k=len_password)

        PASSWORD = "".join(password)

else:
    input(f"\nПароль успішно створено: '{PASSWORD}'. Запам'ятайте його. 'Enter' для продовження ")

password = input("\nВведіть пароль для входу у систему: ")

command = ""
while password == PASSWORD:
    if not command:
        print("Доброго дня. Вітаємо в нашій інформаційній системі")

    for command in COMMANDS:
        print(command)

    command = input("\nВведіть номер команди: ")

    if command == "1":
        print(DELIMITER)
        for i, product in enumerate(PRODUCTS, start=1):
            print(TEMPLATE.format(i, product))
        else:
            print(DELIMITER)

        input("\nНатисніть 'enter' для продовження\n")

    elif command == "2":
        product = input("\nВведіть новий товар для додавання до списку: ")

        if product in PRODUCTS:
            input("\nТакий товар вже доданий\nНатисніть 'enter' для продовження\n")
        else:
            PRODUCTS.append(product)
            input("\nНовий товар доданий до списку\nНатисніть 'enter' для продовження\n")

    elif command == "3":
        prods = input("\nВведіть список товарів через пробіл:\n").split()
        PRODUCTS.extend(prods)
        input("\nСписок продуктів розширено\nНатисніть 'enter' для продовження\n")

    elif command == "4":
        product = input("Введіть назву товару для видалення: ")

        if product in PRODUCTS:
            PRODUCTS.remove(product)
            input(f"\nТовар '{product}' видалено зі списку\nНатисніть 'enter' для продовження\n")
        else:
            input(f"\nТовар '{product}' відсутній у списку\nНатисніть 'enter' для продовження\n")

    elif command == "5":
        number = input("Введіть номер товару для видалення: ")

        if number.isdigit() and 0 < int(number) <= len(PRODUCTS):
            product = PRODUCTS.pop(int(number) - 1)
            input(f"\nТовар '{product}' видалено зі списку\nНатисніть 'enter' для продовження\n")
        else:
            input("\nВвели невірний номер")

    elif command == "6":
        prods = sorted(PRODUCTS)

        for i, prod in enumerate(prods, start=1):
            print(f"{i}: {prod}")

        input("\nСписок товарі відсортовано\nНатисніть 'enter' для продовження\n")

    elif command == "7":
        product = input("Введіть товар для продажу: ")

        if product in PRODUCTS:
            PRODUCTS.remove(product)
            PRODUCTS_SOLD.append(product)
            input(f"Товар '{product}' продано\nНатисніть 'enter' для продовження\n")
        else:
            input(f"Товар '{product}' відсутній у списку")

    elif command == "8":
        product = input("Введіть назву товару для пошуку: ")

        if product in PRODUCTS:
            index = PRODUCTS.index(product)
            input(f"\nТовар '{product}' знаходить під номер '{index + 1}'\nНатисніть 'enter' для продовження\n")
        else:
            input(f"\nТовар '{product}' відсутній у списку")

    elif command == "9":
        print("\nСписок проданий товарів\n")
        for i, product in enumerate(PRODUCTS_SOLD, start=1):
            print(f"{i}: {product}")

        input("\nНатисніть 'enter' для продовження\n")

    elif command == "10":
        prods_sold = PRODUCTS_SOLD[::-1]

        if not prods_sold:
            input("\nСписок проданих товарів порожній\n")

        print("\nІсторія продажу\n")
        for product in prods_sold:
            print(product)

        input("\nНатисніть 'enter' для продовження\n")

    elif command == "11":
        print("\nДякую що були з нами. Чекаємо наступної зустрічі.\n")
        break

    elif command == "12":
        review = input("Введіть свій відгук: ")
        REVIEWS.append(review)
        input("\nВаш відгук додано до системи.\nНатисніть 'enter' для продовження ")

    elif command == "13":
        reviews = " ".join(REVIEWS).lower()

        # repeated_chars = {reviews[i:j] for i in range(len(reviews)) for j in range(i+1, len(reviews)) if reviews.count(reviews[i:j]) >= 2}

        repeated_chars = set()
        for i in range(len(reviews)):
            for j in range(i+1, len(reviews)):
                if reviews.count(reviews[i:j]) >= 2:
                    repeated_chars.add(reviews[i:j])

        input(f"\nГрупи символів, які повторююьюся не менше 2-х разів:\n{repeated_chars}\nНатисніть 'enter' для продовження ")

    elif command == "14":
        palin_prod = [product for product in PRODUCTS if product.lower() == product.lower()[::-1]]

        # palin_prod = []
        # for product in PRODUCTS:
        #     if product.lower() == product.lower()[::-1]:
        #         palin_prod.append(product)

        input(f"Слова-паліндроми:\n{palin_prod}\nНатисніть 'enter' для продовження ")

    elif command == "15":
        for review in REVIEWS:
            print(review)

else:
    print("\nПароль введено не вірно. Доступ заборонено.")