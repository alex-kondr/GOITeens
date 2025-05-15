from aiogram import Router
from aiogram.types import CallbackQuery, URLInputFile

from keyboards import FilmCallback
from data import get_films
from models import FilmModel


film_route = Router()


@film_route.callback_query(FilmCallback.filter())
async def get_film(callback: CallbackQuery, callback_data: FilmCallback):
    film_id = callback_data.id
    film_data = get_films(film_id=film_id)
    film = FilmModel(**film_data)
    text = f"""Фільм: {film.name}
    Опис: {film.description}
    Рейтинг: {film.rating}
    Жанр: {film.genre}
    Актори: {", ".join(film.actors)}
    """
    await callback.message.answer_photo(
        caption=text,
        photo=URLInputFile(
            film.poster,
            filename=f"{film.name}_poster.{film.poster.split('.')[-1]}"
        )
    )
