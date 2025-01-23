import asyncio
from aiogram import Bot, Dispatcher
from os import getenv
from app.handlers import router
from app.database.models import async_main



TOKEN = getenv("BOT_TOKEN")


async def main(): 
    await async_main()
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    