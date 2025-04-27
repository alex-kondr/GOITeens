import json


users_db = [
    {"id": {
        "name": "Alex",
        "age": 47,
        "login": "111",
        "password": "123"
    }}
]


with open("users_db.txt", "w", encoding="utf-8") as file:
    file.write(str(users_db))


with open("users_db.json", "w", encoding="utf-8") as file:
    json.dump(users_db, file, ensure_ascii=False, indent=2)
