from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.inline_kb_contacts import contacts_inl_kb


async def cmd_price(message: types.Message) -> None:
    text = ["Цена фиксированная!",
            "\n🔥🔥🔥🔥\n\nДиван - 1700 руб.",
            "\nКресло - 400 руб.\n",
            "Матрас 2-х спальный - 1200 руб.\n",
            "Матрас 1- 1,5 спальный 600 руб.\n",
            "Стул обычный - 150 руб.\n\n",
            "Химчистку ковров не производим. Есть специализированные сервисы по чистке ковров, можете обратиться туда."]
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


async def cmd_about(message: types.Message) -> None:
    text = [
        "👉Диван сохнет после химчистки в среднем 8-10 часов в зимнее время, и в среднем 4-5 часов в летнее время.\n\n"
        "👉Среднее время химчистки дивана 1,5-2 часа, многое зависит от "
        "загрязненности, объема дивана и количества подушек.\n\n"
        "👉Кресло в среднем занимает от 30 минут, опять же многое зависит от загрязненности\n\n"
        "👉Среднее время очистки стула занимает 15 минут\n\n"
        "👉Чистка двуспального матраса занимает 1-1.5 часа.", ]
    await message.answer('\n'.join(text))
    await message.delete()


def register_keyboard_handler(dp: Dispatcher) -> None:
    dp.register_message_handler(cmd_price, Text('Цена'))
    dp.register_message_handler(cmd_contacts, Text('Контакты'))
    dp.register_message_handler(cmd_about, Text('Об услуге'))
