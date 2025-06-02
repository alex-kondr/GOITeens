from typing import List, Union, Optional, Annotated
from datetime import datetime, date

from pydantic import Field, BaseModel, HttpUrl, field_validator


class People(BaseModel):
    index: Annotated[int, Field(..., description="Номер за порядком")]
    fullName: Annotated[str, Field(...)]
    nickname: Annotated[str, Field(...)]
    hogwartsHouse: Annotated[str, Field(...)]
    interpretedBy: Annotated[str, Field(...)]
    children: Annotated[List[str], Field(default=[], description="Список дітей")]
    image: Annotated[Optional[HttpUrl], Field(None, description="Аватарка")]
    birthdate: Annotated[Union[str, date], Field(..., description="Дата народження", examples=["Sep 19, 1979"])]

    @field_validator("birthdate")
    def check_birthdate(cls, value: Union[str, date]):
        if isinstance(value, str):
            value = datetime.strptime(value, "%b %d, %Y").date()

        if value < date.today():
            return value

        raise ValueError(f"Дата має бути у форматі 'Sep 19, 1979' та бути меншою за '{date.today()}'")


# people_dict = '''{
#     "fullName": "Рональд Біліус Візлі",
#     "nickname": "Рон",
#     "hogwartsHouse": "Ґрифіндор",
#     "interpretedBy": "Rupert Grint",
#     "children": ["Роуз Ґрейнджер-Візлі", "Гюґо Ґрейнджер-Візлі"],
#     "image": "https://raw.githubusercontent.com/fedeperin/potterapi/main/public/images/characters/ron_weasley.png",
#     "birthdate": "Mar 1, 1980",
#     "index": 2
#   }'''

# people = People.model_validate_json(people_dict)
# print(people)