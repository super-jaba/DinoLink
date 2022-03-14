import asyncio
import asyncpg

from config import PG_HOST, PG_PORT, PG_USER, PG_PASSWORD, PG_DATABASE


class Database:

    def __init__(self):
        self.__conn: asyncpg.Connection = None
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__init_connection())

    @staticmethod
    async def recreate_db(host: str, port: str, user: str, password: str, database: str):
        print('Creating (or recreating) the database...')
        conn = await asyncpg.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
        )
        await conn.execute('DROP TABLE users;'
                           'CREATE TABLE users('
                           'id SERIAL PRIMARY KEY,'
                           'tg_user_id VARCHAR(255) UNIQUE NOT NULL'
                           ');')
        await conn.close()

    async def __init_connection(self):
        self.__conn = await asyncpg.connect(
            host=PG_HOST,
            port=PG_PORT,
            user=PG_USER,
            password=PG_PASSWORD,
            database=PG_DATABASE,
        )

    async def __close_connection(self):
        await self.__conn.close()

    async def add_user(self, user_id):
        try:
            await self.__conn.execute('INSERT INTO users (tg_user_id) VALUES ($1);', str(user_id))
        except:
            pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Database.recreate_db(
        host=PG_HOST,
        port=PG_PORT,
        user=PG_USER,
        password=PG_PASSWORD,
        database=PG_DATABASE
    ))
