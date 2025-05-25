from typing import List, Dict, Union, Optional, Annotated
import re
import string

from pydantic import BaseModel, Field, field_validator, EmailStr



class SpellModelResponse(BaseModel):
    index: Annotated[int, Field(0, description="Номер за порядком", examples=[0, 1, 2], ge=0)]
    spell: Annotated[str, Field(..., description="Заклинання", examples=["Sectumsempra", "Crucio"], min_length=3, max_length=100)]
    use: Annotated[str, Field(..., description="Застосування", examples=["Спричиняє важкі порізи", "Заклинання щось робить"], min_length=3, max_length=100)]


class SpellModel(SpellModelResponse):
    @field_validator("index")
    def index_validator(cls, value: int):
        if value > 71:
            return value
        raise ValueError("Індекс повинен бути більше 71")

    @field_validator("spell")
    def spell_validator(cls, value: str):
        if 3 < len(value) < 100:
            return value
        raise ValueError("Кількість символів має бути у діапазоні від 3 до 100.")


class UserModel(BaseModel):
    first_name: Annotated[str, Field(..., min_length=2, description="Ім'я")]
    last_name: Annotated[str, Field(..., min_length=2, description="Прізвище")]
    email: Annotated[Optional[EmailStr], Field(None, description="Електронна пошта користувача")]
    password: Annotated[str, Field(..., min_length=8, description="Мінімум 8 символів, повинен містити хоча б одну велику літеру, одну маленьку літеру, одну цифру та один спеціальний символ")]
    phone_number: Annotated[Optional[str], Field(None, description="Номер телефону у форматі '+38(099)123-45-78'", examples=['+38(099)123-45-78'])]

    @field_validator("first_name")
    def first_name_validator(cls, value: str):
        if value.isalpha():
            return value
        raise ValueError("Повинні бути тільки літери")

    @field_validator("phone_number")
    def phone_number_validator(cls, value: Optional[str]):
        if value and not re.search(r"\+38\(0\d{2}\)\d{3}-\d{2}-\d{2}", value):
            raise ValueError("Номер телефону повинен бути у форматі '+38(099)123-45-78'")
        return value

    @field_validator("password")
    def password_validator(cls, value: str):
        is_upper = False
        is_lower = False
        is_digit = False
        is_punctuation = False

        for char in value:
            if not is_upper and char.isupper():
                is_upper = True

            if not is_lower and char.islower():
                is_lower = True

            if not is_digit and char.isdigit():
                is_digit = True

            if not is_punctuation and char in string.punctuation:
                is_punctuation = True

        if all([is_upper, is_lower, is_digit, is_punctuation]):
            return value

        raise ValueError("Мінімум 8 символів, повинен містити хоча б одну велику літеру, одну маленьку літеру, одну цифру та один спеціальний символ")
