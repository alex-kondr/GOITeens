import json
from typing import Optional, List, Dict, Union


def get_films(file_path: str = "data.json", film_id: Optional[int] = None) -> Union[List[Dict], Dict]:
    with open(file_path, encoding="utf-8") as file:
        films = json.load(file)
        if film_id is not None and film_id < len(films):
            return films[film_id]
        return films


def add_film(film: Dict, file_path: str = "data.json"):
    films = get_films(file_path=file_path)
    films.append(film)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(films, file, indent=2, ensure_ascii=False)


def delete_film(film_id: int, file_path: str = "data.json"):
    films = get_films(file_path=file_path)
    films.pop(film_id)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(films, file, indent=2, ensure_ascii=False)
