from typing import List, Dict, Union, Optional, Annotated
from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl, EmailStr, field_validator, Field


class UserModel(BaseModel):
    # name: str = "Alex"
    # name: str = Field(default="Alex", examples=["Alex", "Alex12"], description="Ім'я користувача")
    name: Annotated[str, Field(default="Alex", examples=["Alex", "Alex12"], description="Ім'я користувача", min_length=2)]
    login: Annotated[str, Field(..., description="Логін", min_length=3)]
    password: Annotated[str, Field(..., examples=["1aA&45"], description="Пароль", min_length=6)]
    created: Annotated[datetime, Field(default=datetime.now())]

    @field_validator("password")
    def check_password(cls, value: str):
        if value == "1aA&45":
            raise ValueError("Не використовуйте приклад!")

        if any([value.isdigit(), value.isalpha()]):
            raise ValueError("Пароль повинен містити мінімум одну літеру та цифру")

        is_upper = False
        is_lower = False
        for char in value:
            if not is_upper and char.isupper():
                is_upper = True
            if not is_lower and char.islower():
                is_lower = True
            if all([is_lower, is_upper]):
                break
        else:
            raise ValueError("Пароль повинен містити велику та малу літеру")

        return value


# user = UserModel(
#     name="Alex",
#     login="Kondr",
#     password="1234A5l6"
# )

# print(user)


class BookModel(BaseModel):
    name: Annotated[str, Field(..., description="Назва книги")]
    # created: Annotated[datetime, Field(..., examples="2001-10-21", description="Дата виходу книги")]

    # @field_validator("created")
    # def check_created(cls, value: Union[str, datetime]):
    #     if isinstance(value, str):
    #         return datetime.strptime(value, "%Y %m %d")
    #     return value


# book = BookModel(
#     name="Зелена книга",
#     created="2005 04 21"
# )

# print(book)