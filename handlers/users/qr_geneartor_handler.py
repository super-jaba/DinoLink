from aiogram.types import Message

from loader import dp


@dp.message_handler(commands=['qr'])
async def generate_qr_handler(msg: Message):
    # TODO: Generate QR-code for data specified
    # TODO: Add watermark on QR
    pass