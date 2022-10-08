import os
import random

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile, ReplyKeyboardRemove, CallbackQuery
from aiogram.utils.exceptions import MessageNotModified

from keyboards.main_kb import main_keyboard
from keyboards.result_kb import result_keyboard

# Path to main directory project
path = os.path.join(os.path.abspath(os.path.dirname(__file__)))[:-8]

num_review = 0


# Function choice. If file have extension 'jpg', send photo. Or if extension is 'mp4', send video.
async def choice_send_review(num_of_list: int, list_of_reviews: list, callback: CallbackQuery) -> CallbackQuery:
    if list_of_reviews[num_of_list].endswith('jpg'):
        type_file = 'photo'
    else:
        type_file = 'video'
    return await callback.message.edit_media(
        types.InputMedia(media=open(path + 'data/reviews/' + list_of_reviews[num_of_list], 'rb'),
                         type=type_file,
                         caption='Нажмите необходимую кнопку на клавиатуре ниже👇\n'
                         ),
        reply_markup=result_keyboard)


# Parsing only FILE NAMES with EXTENSION from directory to list
def parsing_reviews(path_dir, ext=True) -> list:
    files_list = []
    for directory, list_dirs, files in os.walk(path_dir):
        for file in files:
            if ext:
                files_list.append(file)
            elif ext in file:
                files_list.append(file)

    return files_list


async def cmd_start(message: types.Message) -> None:
    await message.answer(text=f'{message.chat.first_name} добро пожаловать в нашего бота!',
                         reply_markup=main_keyboard)


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
        "<b>Инстаграм:</b> https://www.instagram.com/astr_wash_and_go/\n"
        "<b>Телеграм:</b> https://t.me/astr_wash_and_go\n\n"
        "Ввиду того, что часто нахожусь на работе и шумит пылесос, \n"
        "могу пропустить ваш звонок. Вы можете написать мне в личном сообщении, там я вам обязательно отвечу 😉"]
    await message.answer('\n'.join(text))
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


async def cmd_reviews(message: types.Message) -> None:
    await message.answer(text='Вы перешли к просмотру отзывов о работе!\n',
                         reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo=InputFile(path + 'data/reviews/12.jpg'),
                               caption='Нажмите необходимую кнопку на клавиатуре ниже👇\n\n'
                                       'Это первый отзыв!',
                               reply_markup=result_keyboard)

    await message.delete()


async def result_cb_handler(callback: types.CallbackQuery) -> None:
    all_reviews = parsing_reviews(path + 'data/reviews')
    global num_review
    if callback.data == 'first_review':
        num_review = 0
        await callback.message.edit_media(
            types.InputMedia(media=open(path + 'data/reviews/' + all_reviews[num_review], 'rb'),
                             type='video',
                             caption='Это первый отзыв!\n'
                                     'Нажмите необходимую кнопку на клавиатуре ниже👇\n'
                             ),
            reply_markup=result_keyboard)
    elif callback.data == 'rand_review':
        rand_review = random.randint(0, len(all_reviews) - 1)
        await choice_send_review(rand_review, all_reviews, callback)
    elif callback.data == 'next_review':
        if num_review == len(all_reviews) - 1:
            num_review = 0
        else:
            num_review += 1
        await choice_send_review(num_review, all_reviews, callback)
    elif callback.data == 'previous_review':
        if num_review == -len(all_reviews):
            num_review = -1
        else:
            num_review -= 1
        await choice_send_review(num_review, all_reviews, callback)
    elif callback.data == 'cancel_review':
        await callback.message.answer('Возврат в главное меню',
                                      reply_markup=main_keyboard)
        await callback.message.delete()
        await callback.answer()


async def error_double_send(update: types.Update, exception: MessageNotModified) -> bool:
    print("Попытка повторного нажатия!")
    return True


def register_all_keyboard_handler(dp: Dispatcher) -> None:
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_price, Text('Цена'))
    dp.register_message_handler(cmd_contacts, Text('Контакты'))
    dp.register_message_handler(cmd_about, Text('Услуги'))
    dp.register_message_handler(cmd_reviews, Text('Отзывы'))
    dp.register_callback_query_handler(result_cb_handler, lambda callback_query: callback_query.data.endswith('review'))
    dp.register_errors_handler(error_double_send, exception=MessageNotModified)
