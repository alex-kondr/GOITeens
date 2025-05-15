import json
from typing import Optional, List, Dict, Union


def get_films(file_path: str = "data.json", film_id: Optional[int] = None) -> Union[List[Dict], Dict]:
    with open(file_path, encoding="utf-8") as file:
        films = json.load(file)
        if film_id is not None and film_id < len(films):
            return films[film_id]
        return films
