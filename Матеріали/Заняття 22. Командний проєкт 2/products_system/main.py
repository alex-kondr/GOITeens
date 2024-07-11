from dotenv import load_dotenv
from os import getenv
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.types import Message

from routers.products import product_router #Імпорт роутера логіки з товарами
from functions import open_files
from keyboards.products import build_global_menu

# Завантажимо дані середовища з файлу .env(За замовчуванням)
load_dotenv()


# Усі обробники варто закріплювати за Router або Dispatcher
root_router = Router()
root_router.include_routers(product_router) #Включення роутера в головний


# Обробник для команди /start
@root_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    products = open_files.products
    keyboard = build_global_menu()
   #  keyboard = build_products_keyboard(products)
    text = (
      #   f"Вітаю, {hbold(message.from_user.full_name)}, в інформаційній системі продуктового магазину!\n"
        "\nОсь список товарів доступних для продажу:"
    )
    # await edit_or_answer(
    await message.answer(
        text="Список товарів",
        reply_markup=keyboard
    )

# Головна функція пакету
async def main() -> None:
   # Дістанемо токен бота з середовища
   TOKEN = getenv("TELEGRAM_API")
   # Створимо об'єкт Bot
   bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

   dp = Dispatcher()
   dp.include_router(root_router)
   # Почнемо обробляти події для бота
   await dp.start_polling(bot)


# Точка входу
if __name__ == "__main__":
   logging.basicConfig(level=logging.INFO, stream=sys.stdout)
   asyncio.run(main())