from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_products_keyboard(products: list):
    builder = InlineKeyboardBuilder()
    for index, product in enumerate(products):
        builder.button(text=product, callback_data=f"product_{index}")
    return builder.as_markup()


def build_product_action():
    builder = InlineKeyboardBuilder()
    builder.button(text="Видалити товар", callback_data="del prod")
    builder.button(text="Продати товар", callback_data="sold prod")
    return builder.as_markup()