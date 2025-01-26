# Створіть програму, яка приймає від користувача дві строки та порівнює їх лексикографічно (за алфавітом).
# Виведіть результат порівняння у вигляді логічного значення (True або False).

# string_1 = input("Введіть перший рядок: ")
# string_2 = input("Введіть другий рядок: ")
# print(string_1 == string_2)
# 03
# string1 = input("Введіть перший рядок: ")
# string2 = input("Введіть другий рядок: ")

# print(string1 > string2)




# Створіть програму, яка приймає від користувача рядок
# та знаходить кількість слів у цьому рядку
# (слово — це послідовність символів, розділених пробілами).
# Виведіть цю кількість.

# string_1 = input("Введіть строку: ")
# word_count = len(string_1.split())

# print(f"Кількість слів у рядку: {word_count}")



# def count_words():

#     user_input = input("Введіть строку: ")

#     words = user_input.split()

#     word_count = len(words)

#     print(f"Кількість слів у строку: {word_count}")
# count_words()


# Потрібно написати програму, що верифікує пароль
# Умовами верифікації є:
#  - довжина більше 6 символів;
#  - містить хоча б одну цифру, але не лише цифри;
#  - якщо пароль довший за 9 - попередня умова (про цифри) не вимагається;
#  - рядок не повинен містити слово "password" в жодному регістрі


import re

password = input("Введіть пароль: ")

def verify_password(password):
    
    if len(password) <= 6:
        return False
    
    # if re.search(r'password', password, re.IGNORECASE):
    if "password" in password.lower():
        return False
    
    if len(password) > 9:
        return True

































verify_password

