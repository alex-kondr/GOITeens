from aiogram.types.bot_command import BotCommand
from aiogram.filters import Command


FILMS_BOT_COMMAND = Command("films")
FILM_CREATE_COMMAND = Command("create_film")
FILM_DELETE_COMMAND = Command("delete_film")

BOT_COMMANDS = [
    BotCommand(command="films", description="Список фільмів"),
    BotCommand(command="create_film", description="Додати фільм"),
    BotCommand(command="delete_film", description="Видалити фільм")
]

