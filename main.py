import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv

from handlers.keyboard_handler import register_all_keyboard_handler

logger = logging.getLogger(__name__)

# Initialize bot
load_dotenv(find_dotenv())
bot = Bot(os.getenv('TOKEN'), parse_mode="HTML")


def register_all_handlers(dp) -> None:
    register_all_keyboard_handler(dp)


async def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Information about start function
    async def on_startup(_) -> None:
        print('Бот был успешно запущен!')

    # Initialize Dispatcher
    dp = Dispatcher(bot)

    register_all_handlers(dp)

    # Start
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
