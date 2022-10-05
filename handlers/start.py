from aiogram import types, Dispatcher
from keyboards.keyboard import main_keyboard


async def cmd_start(message: types.Message) -> None:
    await message.answer(text='Добро пожаловать в нашего бота!',
                         reply_markup=main_keyboard)


def register_cmd_start(dp: Dispatcher) -> None:
    dp.register_message_handler(cmd_start, commands=['start'])
