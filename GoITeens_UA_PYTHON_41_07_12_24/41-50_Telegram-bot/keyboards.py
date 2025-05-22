from operator import call
from typing import List, Dict, Optional

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class FilmCallback(CallbackData, prefix="film", sep=";"):
    id: int
    name: str


def films_keyboard_markup(films: List[Dict], offset: Optional[int] = None, skip: Optional[int] = None):
    builder = InlineKeyboardBuilder()

    for index, film in enumerate(films):
        callback_data = FilmCallback(id=index, **film)
        builder.button(
            text=callback_data.name,
            callback_data=callback_data.pack()
        )

    builder.adjust(3, repeat=True)
    return builder.as_markup()


def delete_keyboard_markup(film_id):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Видалити фільм",
        callback_data=f"delete_film_{film_id}"
    )
    return builder.as_markup()
