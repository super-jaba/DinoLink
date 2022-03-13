from aiogram.types import Message

from loader import dp


@dp.message_handler(commands=['start'])
async def start_handler(msg: Message):
    # TODO: Add the user to DB

    return await msg.answer(f'Hello, {msg.from_user.username}!\n'
                            f'My name is Dino \U0001F996 and I can make QR codes!')
