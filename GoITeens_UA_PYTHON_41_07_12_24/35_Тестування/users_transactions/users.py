import json
from typing import List, Dict, Union
from uuid import uuid4

from log import get_loger
from hash_password import get_hash_password, check_password


def get_users(file: str = "users_db.json") -> List[Dict]:
    get_loger("Відкриття файлу з користувачами")
    with open(file, "r", encoding="utf-8") as fd:
        users = json.load(fd)
    return users


def save_users(users: List[Dict], file: str = "users_db.json"):
    get_loger("Збереження інформації про користувачів")
    with open(file, "w", encoding="utf-8") as fd:
        json.dump(users, fd, ensure_ascii=False, indent=2)


def sign_up(login: str, password: str, name: str):
    users = get_users()
    print(users)
    user = next((user for user in users if user.get("login")==login), None)

    if not user:
        users.append({
            "id": uuid4().hex,
            "login": login,
            "password": str(get_hash_password(password)),
            "name": name
        })
        save_users(users)
        get_loger("Користувач успішно зареєструвався")
        return True
    else:
        get_loger("Такий користувач вже існує")
        return False


def login_user(login: str, password: str) -> Dict:
    users = get_users()
    user = next((user for user in users if user.get("login")==login), None)

    if not user or not check_password(password, user.get("password")):
        get_loger("Логін або пароль невірний")
        raise ValueError("Логін або пароль невірний")

    return user
