from aiogram import Bot, Dispatcher, executor, types

import os

bot = Bot(os.getenv('TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot)


async def on_startup(_) -> None:
    print('Бот был успешно запущен!')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать в нашего бота!')


if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)
