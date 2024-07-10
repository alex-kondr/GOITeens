from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.markdown import hbold

from functions import open_files
from keyboards.products import build_products_keyboard, build_product_action


product_router = Router()


@product_router.message(Command("products"))
@product_router.message(F.text.casefold() == "товари")
async def show_all_prods(message: Message, state: FSMContext) -> None:
    products = open_files.products
    keyboard = build_products_keyboard(products)
    await message.answer(
        text="Список товарів",
        reply_markup=keyboard
    )


@product_router.callback_query(F.data.startwith("product_"))
async def show_prod_action(callback: CallbackQuery, state: FSMContext) -> None:
    prod_id = int(callback.data.split("_")[-1])
    # product = open_files.products[prod_id]
    await edit_or_answer(callback.message, "text_kuku", build_product_action())


async def edit_or_answer(message: Message, text: str, keyboard, *args, **kwargs):
   if message.from_user.is_bot:
       await message.edit_text(text=text, reply_markup=keyboard, **kwargs)
   else:
       await message.answer(text=text, reply_markup=keyboard, **kwargs)