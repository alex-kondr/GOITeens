from aiogram import Router, F
from aiogram.types import CallbackQuery, URLInputFile, Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from forms import FilmForm
from keyboards import FilmCallback, delete_keyboard_markup
from data import get_films as data_get_films, add_film as data_add_film, delete_film as data_delete_film
from models import FilmModel
from commands import FILM_CREATE_COMMAND


film_route = Router()


@film_route.callback_query(FilmCallback.filter())
async def get_film(callback: CallbackQuery, callback_data: FilmCallback):
    film_id = callback_data.id
    film_data = data_get_films(film_id=film_id)
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
        ),
        reply_markup=delete_keyboard_markup(film_id)
    )


@film_route.message(FILM_CREATE_COMMAND)
async def add_film(message: Message, state: FSMContext):
    await state.set_state(FilmForm.name)
    await message.answer(
        text="Введіть назву фільму",
        reply_markup=ReplyKeyboardRemove()
    )


@film_route.message(FilmForm.name)
async def film_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state((FilmForm.description))
    await message.answer(
        text="Введіть опис для фільму",
        reply_markup=ReplyKeyboardRemove()
    )


@film_route.message(FilmForm.description)
async def film_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(FilmForm.rating)
    await message.answer(
        text="Введфть рейтинг для фільму від 0 до 10",
        reply_markup=ReplyKeyboardRemove()
    )


@film_route.message(FilmForm.rating)
async def film_rating(message: Message, state: FSMContext):
    await state.update_data(rating=message.text)
    await state.set_state(FilmForm.genre)
    await message.answer(
        text="Введіть жанр для фільму",
        reply_markup=ReplyKeyboardRemove()
    )


@film_route.message(FilmForm.genre)
async def film_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await state.set_state(FilmForm.actors)
    await message.answer(
        text="Введіть список акторів через кому та пробіл ', '",
        reply_markup=ReplyKeyboardRemove()
    )


@film_route.message(FilmForm.actors)
async def film_actors(message: Message, state: FSMContext):
    await state.update_data(actors=[actor for actor in message.text.split(", ")])
    await state.set_state(FilmForm.poster)
    await message.answer(
        text="Вставте посилання на постер фільму",
        reply_markup=ReplyKeyboardRemove()
    )


@film_route.message(FilmForm.poster)
async def film_poster(message: Message, state: FSMContext):
    data = await state.update_data(poster=message.text)
    data_add_film(data)
    await state.clear()
    await message.answer(
        text="Фільм успішно доданий",
        reply_markup=ReplyKeyboardRemove()
    )


@film_route.callback_query(F.data.startswith("delete_film_"))
async def delete_film(callback: CallbackQuery, state: FSMContext):
    film_id = int(callback.data.split("_")[-1])
    data_delete_film(film_id)
    await callback.message.answer(text="Фільм успішно видалений")
