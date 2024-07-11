from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_products_keyboard(products: list):
    builder = InlineKeyboardBuilder()
    # builder.adjust(3, 2)
    builder.row(width=3)
    for index, product in enumerate(products):
        builder.button(text=product, callback_data=f"product_{index}")
    return builder.as_markup()


def build_product_action(product: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Видалити товар", callback_data=f"del prod:{product}")
    builder.button(text="Продати товар", callback_data=f"sold prod:{product}")
    builder.button(text="До списку товарів", callback_data="back")
    return builder.as_markup()


# def build_menu_keyboard() -> InlineKeyboardMarkup:
#    builder = InlineKeyboardBuilder()
#    builder.button(text="До списку товарів", callback_data="back")
#    return builder.as_markup()