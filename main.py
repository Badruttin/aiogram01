import asyncio
from aiogram import Bot, Dispatcher
from os import getenv
from app.handlers import router



TOKEN = getenv("BOT_TOKEN")


async def main(): 
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    