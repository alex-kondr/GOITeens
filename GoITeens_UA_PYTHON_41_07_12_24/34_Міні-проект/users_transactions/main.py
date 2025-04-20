from typing import List, Dict

from users import get_users, save_users, sign_up, login_user
from log import get_loger


def register_user() -> bool:
    print("Введіть необхідні дані дя реєстрації")
    name = input("Введіть своє ім'я: ")
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")
    return sign_up(name=name, password=password, login=login)


def sign_in() -> Dict:
    login = input("Введіть логін: ")
    password = input("Введіть свій пароль: ")

    try:
        return login_user(login, password)
    except ValueError as error:
        print(error)


def main():
    while True:
        action = input("Введіть 1 - для реєстрації\n2 - для входу у систему: ")
        if action == "1":
            if not register_user():
                continue

        user = sign_in()
        if not user:
            continue

        print(user)
        # user["password"] = "new_password"
        break


if __name__ == "__main__":
    main()
