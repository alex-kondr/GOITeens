from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def build_global_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Список наявних товарів")
    builder.button(text="Додати новий товар")
    builder.button(text="Список проданих товарів")
    builder.button(text="Відгуки")
    builder.button(text="Додати відгук")
    builder.button(text="Знайти групи символів,\nякі повторюються\n(використовуючи всі відгуки)")
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
    return builder.as_markup()
