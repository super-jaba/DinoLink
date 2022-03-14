from aiogram.types import Message

from loader import dp


@dp.message_handler(commands=['help'])
async def help_handler(msg: Message):
    # TODO: Handle /help command
    pass
