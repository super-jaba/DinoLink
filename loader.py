from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode

from config import TOKEN


bot = Bot(TOKEN, parse_mode=ParseMode.HTML, validate_token=True)
dp = Dispatcher(bot)
