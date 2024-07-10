from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.markdown import hbold

from functions import open_files
from keyboards.products import build_products_keyboard


product_router = Router()


@product_router.message(Command("products"))
@product_router.message(F.text.casefold() == "products")
async def show_all_prods(message: Message, state: FSMContext) -> None:
    products = open_files.products
    keyboard = build_products_keyboard(products)
    await message.answer(
        text="Список товарів",
        reply_markup=keyboard
    )