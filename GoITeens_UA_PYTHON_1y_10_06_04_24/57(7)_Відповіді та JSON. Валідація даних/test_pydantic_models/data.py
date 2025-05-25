import json
from typing import List, Dict


def get_spells(file_path: str = "spells.json") -> List[Dict]:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_spells(db: List[Dict], file_path: str = "spells.json") -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(db, file, indent=2, ensure_ascii=False)
