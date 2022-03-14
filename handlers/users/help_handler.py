from aiogram.types import Message

from loader import dp


@dp.message_handler(commands=['help'])
async def help_handler(msg: Message):
    return await msg.answer('<b>A brief guide</b>:\n'
                            'Use "/qr" or "/qr <i>[data you want to QR]</i>" '
                            'to create QR-code of any data you want')
