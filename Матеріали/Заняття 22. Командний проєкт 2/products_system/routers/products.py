from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from functions import open_files
from keyboards.products import build_products_keyboard, build_product_action
from functions import products as funcs_prods
from form.form import ProdCreateForm


product_router = Router()


@product_router.message(F.text == "Список наявних товарів")
async def show_all_prods(message: Message, state: FSMContext) -> None:
    products = open_files.products
    keyboard = build_products_keyboard(products)
    await edit_or_answer(
        message,
        "Список товарів",
        keyboard
    )


@product_router.callback_query(F.data.startswith("product_"))
async def show_prod_action(callback: CallbackQuery, state: FSMContext) -> None:
    prod_id = int(callback.data.split("_")[-1])
    product = open_files.products[prod_id]
    await edit_or_answer(
        callback.message,
        product,
        build_product_action(product),
        ReplyKeyboardRemove())


async def edit_or_answer(message: Message, text: str, keyboard=None, *args, **kwargs):
   if message.from_user.is_bot:
       await message.edit_text(text=text, reply_markup=keyboard, **kwargs)
   else:
       await message.answer(text=text, reply_markup=keyboard, **kwargs)


@product_router.callback_query(F.data.startswith("del prod"))
async def del_prod_action(callback: CallbackQuery, state: FSMContext) -> None:
    product = callback.data.split(":")[-1]
    funcs_prods.del_prod_by_name(product)
    text = f"Товар '{product}' видалено"
    await edit_or_answer(callback.message, text)
    return await show_all_prods(callback.message, state)


@product_router.callback_query(F.data.startswith("sold prod"))
async def sold_prod_action(callback: CallbackQuery, state: FSMContext):
    product = callback.data.split(":")[-1]
    funcs_prods.sold_prod(product)
    text = f"Товар '{product}' продано"
    await edit_or_answer(callback.message, text)
    return await show_all_prods(callback.message, state)


@product_router.callback_query(F.data == "back")
async def back_handler(callback: CallbackQuery, state: FSMContext) -> None:
    state.clear()
    return await show_all_prods(callback.message, state)


@product_router.message(F.text == "Додати новий товар")
async def add_new_prod_action(message: Message, state: FSMContext):
    await state.set_state(ProdCreateForm.name)
    await edit_or_answer(message, "Введіть назву товару")


@product_router.message(ProdCreateForm.name)
async def 