from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_global_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="Список наявних товарів", callback_data="products")
    builder.button(text="Додати новий товар", callback_data="add_product")
    builder.button(text="Список проданих товарів", callback_data="products_sold")
    builder.button(text="Відгуки", callback_data="reviews")
    builder.button(text="Додати відгук", callback_data="add_review")
    builder.adjust(1)
    return builder.as_markup()


def build_products_keyboard(products: list):
    builder = InlineKeyboardBuilder()
    for index, product in enumerate(products):
        builder.button(text=product, callback_data=f"product_{index}")
    builder.adjust(4)
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