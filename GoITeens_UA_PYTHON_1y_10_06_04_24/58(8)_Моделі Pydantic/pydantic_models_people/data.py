import json
from typing import Union, List, Dict


def get_data(file_path: str = "people.json") -> List[Dict]:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def add_human(human: Dict, file_path: str = "people.json") -> None:
    people = get_data()
    people.append(human)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(people, file, indent=2, ensure_ascii=False)


def delete_human(human: Dict, file_path: str = "people.json") -> None:
    people = get_data()
    people.remove(human)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(people, file, ensure_ascii=False, indent=2)
