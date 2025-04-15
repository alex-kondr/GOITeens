from typing import Optional, List, Annotated, Union
from enum import Enum
from datetime import date, datetime

from pydantic import BaseModel, HttpUrl, Field, field_validator, ValidationError

from pydantic_extra_types.pendulum_dt import Date


class User(BaseModel):
    fullName: str = "Гаррі Джеймс Поттер"
    nickname: str = "Гаррі"
    hogwartsHouse: str = "Ґрифіндор"
    interpretedBy: str = "Daniel Radcliffe"
    image: HttpUrl = "https://raw.githubusercontent.com/fedeperin/potterapi/main/public/images/characters/harry_potter.png"
    birthdate: Annotated[Union[str, Date], Field("Jul 31, 1980")]
    index: Annotated[int, Field(25, strict=True, gt=24)]
    children: Annotated[List[str], Field([])]
    

    @field_validator("birthdate")
    def check_birth_date(cls, value: str):
        if isinstance(value, str):
            value = datetime.strptime(value, "%b %d, %Y").date()

        if value < datetime.now().date():
            return value
        raise ValueError("Дата має бути меншою за поточну")
        


user_json = '{"fullName":"Гаррі Джеймс Поттер","nickname":"Гаррі","hogwartsHouse":"Ґрифіндор","interpretedBy":"Daniel Radcliffe","image":"https://raw.githubusercontent.com/fedeperin/potterapi/main/public/images/characters/harry_potter.png","birthdate":"Jul 31, 1980","index":25}'
user = User.model_validate_json(user_json)
user.children.append("Draco")
# User.model_dump_jso
print(user)

# print(datetime(2025, 4, 15) < datetime.now())


# user = User(birthdate="Jul 31, 1980")
# user = User(birthdate=datetime(2025, 4, 14))
# print(user.birthdate)
# print(user.model_dump_json())

# print()