import os
import dotenv

dotenv.load_dotenv()

# Telegram API key
TOKEN = os.getenv('TG_TOKEN')

# PostgreSQL credentials
PG_HOST = os.getenv('PG_HOST')
PG_PORT = os.getenv('PG_PORT')
PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_DATABASE = os.getenv('PG_DATABASE')
