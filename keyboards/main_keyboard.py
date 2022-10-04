from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_price = KeyboardButton('Цена')
    btn_contacts = KeyboardButton('Контакты')
    btn_reviews = KeyboardButton('Отзывы')
    btn_difference = KeyboardButton('До/После')
    btn_about = KeyboardButton('Об услуге')

    kb.add(btn_price, btn_contacts).add(btn_reviews, btn_difference).add(btn_about)

    return kb


main_keyboard = get_keyboard()
