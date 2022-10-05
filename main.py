import logging

from aiogram import Bot, Dispatcher, executor, types
from keyboards.main_keyboard import main_keyboard
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(os.getenv('TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot)


async def on_startup(_) -> None:
    print('Бот был успешно запущен!')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать в нашего бота!',
                           reply_markup=main_keyboard)


if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)
