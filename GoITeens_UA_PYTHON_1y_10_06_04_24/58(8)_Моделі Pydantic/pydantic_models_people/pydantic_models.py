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
            return value.strftime("%b %d, %Y")

        raise ValueError(f"Дата має бути у форматі 'Sep 19, 1979' та бути меншою за '{date.today()}'")


# people_dict = '''{
#   "index": 0,
#   "fullName": "string",
#   "nickname": "string",
#   "hogwartsHouse": "string",
#   "interpretedBy": "string",
#   "children": [],
#   "image": "https://example.com/",
#   "birthdate": "Sep 19, 1979"
# }'''

# people = People.model_validate_json(people_dict)
# print(people)
# print(people.model_dump())