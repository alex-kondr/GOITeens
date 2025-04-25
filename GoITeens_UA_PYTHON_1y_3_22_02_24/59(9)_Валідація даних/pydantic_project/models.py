from typing import List, Dict, Optional, Union, Annotated
from datetime import datetime

from pydantic import BaseModel, EmailStr, HttpUrl, BeforeValidator, field_validator, model_validator, Field


class Country(BaseModel):
    name: Annotated[str, Field(..., description="Назва країни", examples=["Україна"], min_length=3)]
    code: Annotated[int, Field(..., description="Код країни", examples=[380, 420])]


class City(BaseModel):
    name: Annotated[str, Field(..., description="Назва міста")]
    country: Annotated[Country, Field(..., description="Країна")]


class Address(BaseModel):
    street: Annotated[str, Field(..., description="Назва вулиці")]
    number: Annotated[int, Field(..., description="Номер будинку", gt=0)]
    city: City


class Product(BaseModel):
    name: Annotated[str, Field(..., description="Назва товару", min_length=2, max_length=100)]
    date_time: Annotated[datetime, Field(..., description="Дата та час покупки", examples=["2024-10-25T12:05:00"], default_factory=datetime.now, le=datetime.now())]
    quantity: Annotated[int, Field(1, description="Кількість товару", ge=0)]


def validate_full_name(value: str):
    names = value.split()
    if len(names) < 2:
        raise ValueError("Повне ім'я повинно складатись з принаймні двох слів")
    return value


class People(BaseModel):
    full_name: Annotated[str, BeforeValidator(validate_full_name)]
    address: Address
    # products: List[Annotated[Optional[Product], Field(None)]]
    products: List[Product] = []

    @field_validator("products")
    def validate_products(cls, products: List[Product]):
        for product in products:
            if product.quantity > 100:
                raise ValueError("У магазині може бути не більше 100 товарів")
        return products

    # @model_validator()
    # def validator_model(cls, mode="after"):
    #     pass

    class Config:
        str_min_length = 1
        str_max_length = 255

        json_schema_extra = dict(
            full_name="Вася Пупкін",
            address=dict(
                street="Перемоги",
                number=5,
                city=dict(
                    name="Одеса",
                    country=dict(
                        name="Україна",
                        code=380
                    )
                )
            ),
            products=[
                dict(
                    name="Гречка"
                ),
                dict(
                    name="Хліб"
                )
            ]
        )


# people_obj = dict(
#     full_name="Вася Пупкін",
#     address=dict(
#         street="Перемоги",
#         number=5,
#         city=dict(
#             name="Одеса",
#             country=dict(
#                 name="Україна",
#                 code=380
#             )
#         )
#     ),
#     products=[
#         dict(
#             name="Гречка"
#         ),
#         dict(
#             name="Хліб"
#         )
#     ]
# )

# people = People(**people_obj)
# print(people.model_dump_json(indent=2))
