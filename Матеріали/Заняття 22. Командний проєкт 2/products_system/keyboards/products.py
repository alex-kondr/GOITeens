from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_products_keyboard(products: list):
    builder = InlineKeyboardBuilder()
    for index, product in enumerate(products):
        builder.button(text=product, callback_data=f"product_{index}")
    return builder.as_markup()