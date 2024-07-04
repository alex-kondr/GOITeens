import random
import string


def is_verify_password(password: str) -> bool:
    pass_len = False if len(password) < 8 else True
    pass_digit = False
    pass_char = False

    for char in password:
        if char.isdigit():
            pass_digit = True
        if char.isalpha():
            pass_char = True

    return True if pass_len and pass_digit and pass_char else False


def generate_password(
    len_password: int = 8,
    is_upper: bool = False,
    is_punctuation: bool = False,
    is_repeat: bool = True
) -> str:

    pass_chars = string.ascii_lowercase + string.digits
    pass_chars += string.ascii_uppercase if is_upper else ""
    pass_chars += string.punctuation if is_punctuation else ""
    password = random.choices(pass_chars, k=len_password) if is_repeat else random.sample(pass_chars, k=len_password)
    return "".join(password)


def create_password() -> str:
    command = input("Введіть 'create' для введення свого паролю будь який символ для автоматичної генерації -> ")
    if command == "create":
        password = input("Введіть свій пароль (повинен містити не менше 8 символів, а також повинен містити хоча б одну букву та одну цифру): ")

    else:
        len_pass = input("Введіть довжину пароля (не менше 8) або залишити за замовчуванням (8 символів): ")
        if len_pass.isdigit() and int(len_pass) > 8:
            len_pass = int(len_pass)
        else:
            len_pass = 8

        is_upper = True if input("Чи використовувати великі букви (1 - так, будь який інший символ - ні)? ") == "1" else False
        is_punctuation = True if input("Чи використовувати спецсимволи (1 - так, будь який інший символ - ні)? ") == "1" else False
        is_repeat = True if input("Чи можуть символи повторюватись (1 - Так, будь який інший символ - Ні)? ") == "1" else False

        password = generate_password(len_password=len_pass, is_punctuation=is_punctuation, is_upper=is_upper, is_repeat=is_repeat)

    return password
