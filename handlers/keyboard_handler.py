from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.inline_kb_contacts import contacts_inl_kb


async def cmd_price(message: types.Message) -> None:
    text = ["Цена фиксированная!",
            "\n🔥🔥🔥🔥\n\nДиван - 1500 руб.",
            "\nКресло - 300 руб.\n",
            "Матрас 2-х спальный - 1000 руб.\n",
            "Матрас 1- 1,5 спальный 500 руб.\n",
            "Стул обычный - 125 руб.",
            "\n\nХимчистку ковров не производим. Есть специализированные сервисы по чистке ковров, можете обратиться туда."]
    await message.answer('\n'.join(text))
    await message.delete()


async def cmd_contacts(message: types.Message) -> None:
    text = [
        "<b>Контакты</b>\n\n"
        "<b>Номер:</b> +7 (999) 601-47-37\n"
        "<b>Почта:</b> Kharyushina1995@mail.ru\n"
        "<b>Инстаграм:</b> https://www.instagram.com/astr_wash_and_go/\n\n"
        "Ввиду того, что часто нахожусь на работе и шумит пылесос, \n"
        "могу к моему сожалению пропустить звонок, поэтому пишите в личные сообщения, там я Вам однозначно отвечу."]
    await message.answer('\n'.join(text), reply_markup=contacts_inl_kb)
    await message.delete()


def register_keyboard_handler(dp: Dispatcher) -> None:
    dp.register_message_handler(cmd_price, Text('Цена'))
    dp.register_message_handler(cmd_contacts, Text('Контакты'))
