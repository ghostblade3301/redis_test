import os
import logging

import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv


load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message()
async def echo_message(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text='Wait a second...'
    )
    await message.answer(text=message.text)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
