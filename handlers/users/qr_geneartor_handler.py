from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from loader import dp
from states.qr_generator_states import QRGeneratorStates
from utils.qr_generator import *


@dp.message_handler(commands=['qr'])
async def qr_generator_entry(msg: Message):
    data = msg.get_args()
    if not data:
        await msg.answer('Please, send the data you want to encode (links, text, etc.)')
        return await QRGeneratorStates.WAIT_FOR_DATA_STATE.set()
    filename = f'{msg.from_user.id} {datetime.now().strftime("%H:%M:%S")}'
    generate_qr_of(data, save_as=filename)
    await msg.answer_photo(photo=open(f'./client_images/{filename}.png', 'rb'), caption='Here is your QR \U0001F4E6')
    delete_client_image(filename)


@dp.message_handler(state=QRGeneratorStates.WAIT_FOR_DATA_STATE)
async def qr_generator(msg: Message, state: FSMContext):
    data = msg.text
    filename = f'{msg.from_user.id} {datetime.now().strftime("%H:%M:%S")}'
    generate_qr_of(data, save_as=filename)
    await msg.answer_photo(photo=open(f'./client_images/{filename}.png', 'rb'), caption='Here is your QR \U0001F4E6')
    delete_client_image(filename)

    return await state.finish()
