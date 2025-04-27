import hashlib

from log import get_loger


def get_hash_password(password: str) -> str:
    get_loger("Створюємо хешований пароль")
    return hashlib.sha512(password.encode()).digest()


def check_password(password: str, password_db: str):
    if str(get_hash_password(password)) == password_db:
        get_loger("Пароль пройшов перевірку")
        return True
    else:
        get_loger("Пароль невірний")
        return False
