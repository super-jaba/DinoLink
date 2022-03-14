from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

from config import TOKEN
from db.db import Database

bot = Bot(TOKEN, parse_mode=ParseMode.HTML, validate_token=True)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()
