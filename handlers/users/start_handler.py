from aiogram.types import Message

from loader import dp, db


@dp.message_handler(commands=['start'])
async def start_handler(msg: Message):
    await db.add_user(msg.from_user.id)

    return await msg.answer(f'Hello, {msg.from_user.username}!\n'
                            f'My name is Dino \U0001F996 and I can make QR codes!\n'
                            f'Use /help command to take a look at my abilities')
