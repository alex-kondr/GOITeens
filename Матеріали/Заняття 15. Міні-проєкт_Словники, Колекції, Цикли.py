import string
import random
from datetime import datetime        #########################


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
# "1. Show the list of available products",
#  "2. Add a new product to the list",
#  "3. Add a list of products",
#  "4. Delete product by name",
#  "5. Delete product by number",
#  "6. Sort the list of products by name",
#  "7. Sell goods",
#  "8. Find the product number by name",
#  "9. Show the list of sold products",
#  "10. Show sales history",
#  "11. Exit the program",
#  "12. Write a review",
#  "13. Find groups of repeating characters (using all feedback)",
#  "14. Find products that are palindromes",
#  "15. Add a new employee",
#  "16. Delete the employee",
#  "17. View the list of employees",
#  "18. Change the salary of an employee",
#  "19. Change the position of an employee"
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
    "12. Написати відгук",
    "13. Знайти групи символів, які повторюються (використовуючи всі відгуки)",
    "14. Знайти продукти, які є паліндромами",
    "15. Додати нового працівника",                            #######################
    "16. Видалити працівника",                                 #######################
    "17. Переглянути список працівників",                      #######################
    "18. Змінити заробітну плату працівника",                  #######################
    "19. Змінити посаду працівника",                           #######################
    "20. Показати лог",                                        #######################
    "21. Показати список команд та їх частоту використання"    #######################
]

PASSWORD = ""
REVIEWS = []
REPEATED_GROUPS = set()
EMPLOYEES = {                    #############################
    "andrew": {
        "position": "Менеджер",
        "salary": "30000",
        "start_date": "22.02.2024",
        "name": "Андрій",
        "password": "1234567a"
    },
    "dima": {
        "position": "Продавець",
        "salary": "14000",
        "start_date": "10.03.2024",
        "name": "Дмитро",
        "password": "1234567b"
    }
}
LOG = []              ###############

HEAD = ["№", "Назва товару"]
DELIMITER = "-" * 28
TEMPLATE = "|{:^5}|{:<20}|"

# Створюємо пароль для входу
while True:
    username = input("Введіть логін: ")                    #############################
    if username in EMPLOYEES:                              #############################
        PASSWORD = EMPLOYEES[username]["password"]         #############################
        break                                              #############################

    name = input("Введіть своє ім'я: ")                    #############################
    position = input("Введіть свою посаду: ")              #############################
    command = input("\
        Введіть '1' для введення свого паролю;\n\
        Введіть '2' для автоматичної генерації паролю;\n\
        Будь яка інша команда для виходу з програми\n-> ")

    if command == "1":
        password = input("Введіть свій пароль (повинен містити не менше 8 символів, а також повинен містити хоча б одну букву та одну цифру) ")

        pass_len = True if len(password) >= 8 else False
        pass_digit = False
        pass_alpha = False

        for char in password:
            if char.isdigit():
                pass_digit = True

            if char.isalpha():
                pass_alpha = True

        if pass_len and pass_digit and pass_alpha:
            EMPLOYEES[username] = {                                 ##############
                "position": position,                               ##############
                "start_date": datetime.now().strftime("%d-%m-%Y"),  ##############
                "name": name,                                       ##############
                "password": password                                ##############
            }
            PASSWORD = password
            print("Користувача успішно створено")                   ##############
            break
        else:
            print("Пароль не пройшов перевірку, введіть новий пароль або згенеруйте автоматичний пароль")

    elif command == "2":
        chars_for_pass = string.ascii_lowercase + string.digits

        is_upper = input("Чи використовувати великі букви (1 - так, будь який інший символ - ні)? ")
        if is_upper == "1":
            chars_for_pass += string.ascii_uppercase

        is_punctuation = input("Чи використовувати спецсимволи (1 - так, будь який інший символ - ні)? ")
        if is_punctuation == "1":
            chars_for_pass += string.punctuation

        len_pass = input("Введіть довжину пароля (не менше 8) або залишити за замовчуванням (8 символів): ")
        if len_pass.isdigit() and int(len_pass) >= 8:
            len_pass = int(len_pass)
        else:
            len_pass = 8

        pass_digit = False
        pass_alpha = False

        unique_chars = input("Чи повинні символи бути унікальні (1 - Так, будь який інший символ - Ні)? ")
        if unique_chars == "1":
            password = set()
        else:
            password = []

        while not pass_digit or not pass_alpha or len(password) < len_pass:
            char_for_pass = random.choice(chars_for_pass)
            if isinstance(password, set):
                password.add(char_for_pass)
            elif isinstance(password, list):
                password.append(char_for_pass)

            if char_for_pass.isdigit():
                pass_digit = True

            if char_for_pass.isalpha():
                pass_alpha = True
        else:
            PASSWORD = "".join(password)
            EMPLOYEES[username] = {                               ##############
                "position": position,                             ##############
                "start_date": datetime.now().strftime("%d-%m-%Y"),  ##############
                "name": name,                                     ##############
                "password": PASSWORD                              ##############
            }
            print(f"Кjристувачf з паролем '{PASSWORD}' успішно створено.")
            break

    else:
        print("Ви вийшли з програми. До побачення")
        break

password = input("Введіть пароль для входу в систему: ") if PASSWORD else quit()

command = None
while password == PASSWORD: # PASSWORD and :
    if not command:
        LOG.append({username: "login", "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")}) ##############
        print("\nПароль вірний. Гарного та продуктивного Вам дня.\n")

    print("Введіть номер команди")
    for command in COMMANDS:
        print(command)

    command = input("-> ")

    if command == "1":
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
        print(DELIMITER)
        print(TEMPLATE.format(*HEAD))
        for i in range(len(PRODUCTS)):
            print(TEMPLATE.format(i+1, PRODUCTS[i]))

        print(DELIMITER)
        input("Натисніть 'Enter' для продовження")

    elif command == "2":
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
        product = input("Введіть назву товару: ")

        if product not in PRODUCTS:
            PRODUCTS.append(product)
            print(f"Товар '{product}' додано до списку")
        else:
            print("Такий товар вже наявний у списку")

        input("Натисніть 'Enter' для продовження")

    elif command == "3":
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
        prods = input("Введіть список товарів через пробіл:\n")
        prods = prods.split()
        PRODUCTS.extend(prods)
        input("Натисніть 'Enter' для продовження")

    elif command == "4":
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
        product = input("Введіть назву товару для видалення: ")
        if product in PRODUCTS:
            PRODUCTS.remove(product)
        else:
            print("Такого товару немає у списку")

        input("Натисніть 'Enter' для продовження")

    elif command == "5":
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
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
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
        PRODUCTS.sort()
        print("Список відсортовано")
        input("Натисніть 'Enter' для продовження")

    elif command == "7":
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
        product = input("Введіть назву товару для продажу: ")

        if product not in PRODUCTS:
            print("Такого товару немає")
            input("Натисніть 'Enter' для продовження")
            continue

        PRODUCTS.remove(product)
        PRODUCTS_SOLD.append(product)
        input("Натисніть 'Enter' для продовження")

    elif command == "8":
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
        product = input("Введіть назву товару для пошуку: ")

        if product not in PRODUCTS:
            print("Такого товару немає")
            input("Натисніть 'Enter' для продовження")
            continue

        product_index = PRODUCTS.index(product)
        print(f"Товар '{product}' знаходиться під номером '{product_index + 1}'")
        input("Натисніть 'Enter' для продовження")

    elif command == "9":
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
        if not PRODUCTS_SOLD:
            print("Сьогодні ще нічого не продано")
            input("Натисніть 'Enter' для продовження")
            continue

        print("Сьогодні продано такі товари:")
        for i, product in enumerate(PRODUCTS_SOLD):
            print(f"{i + 1}. {product}")

        input("Натисніть 'Enter' для продовження")

    elif command == "10":
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
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
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
        print("Дякую що були з нами")
        break

    elif command == "12":
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
        review = input("Введіть свій відгук:\n-> ")
        REVIEWS.append(review)

    elif command == "13":
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
        reviews = " ".join(REVIEWS)

        for i in range(len(reviews)):
            for j in range(i+1, len(reviews)):
                group_str = reviews[i:j]
                sub_str = reviews[j:]
                if group_str in sub_str:
                    REPEATED_GROUPS.add(group_str)

        print(f"{REPEATED_GROUPS = }")
        input("\nНатисніть 'Enter' для продовження")

    elif command == "14":
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
        palindrome_products = [product for product in PRODUCTS if product == product[::-1]]
        if palindrome_products:
            print(f"Список продуктів, які являються паліндромами: {palindrome_products}")
        else:
            print("Не знайдено продуктів, які являються паліндромами")

        input("\nНатисніть 'Enter' для продовження")

    elif command == "20":
        for log in LOG:
            print(log)
        input("\nНатисніть 'Enter' для продовження")

    elif command == "21":
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
        commands_count = {}
        for log in LOG:
            if log[username] in commands_count:
                commands_count[log[username]] += 1
            else:
                commands_count[log[username]] = 1

        print(commands_count)
        input("\nНатисніть 'Enter' для продовження")

    else:
        LOG.append({username: command, "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
        input("Невідома команда.\nНатисніть 'Enter' для продовження")

else:
    print("Пароль введено не вірно")
