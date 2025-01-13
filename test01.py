
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, types, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

router = Router()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Site', url = 'https://ya.ru'))
    #markup.add(types.InlineKeyboardButton(text='Call', callback_data='call_test1'))

    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=markup)

@router.message(Com)

@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())