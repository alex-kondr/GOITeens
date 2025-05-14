import os
import asyncio
import logging
import sys

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from data import get_films
from keyboards import films_keyboard_markup
from commands import FILMS_BOT_COMMAND


load_dotenv()
TOKEN = os.getenv(("TBOT"))
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer((f"Привіт, {message.from_user.full_name}!"))


@dp.message(Command("help"))
async def echo_handler(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Error")


@dp.message(Command("films"))
async def films(message: Message):
    data = get_films()
    markup = films_keyboard_markup(films=data)
    await message.answer(
        "Перелік фільмів",
        reply_markup=markup
    )


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands(commands=[FILMS_BOT_COMMAND])
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

