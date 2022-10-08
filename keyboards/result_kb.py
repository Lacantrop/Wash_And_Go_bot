from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)

    next_btn = InlineKeyboardButton('⏩ Следующий', callback_data='next_review')
    previous_btn = InlineKeyboardButton('Предыдущий ⏪', callback_data='previous_review')
    first_btn = InlineKeyboardButton('С начала ▶️', callback_data='first_review')
    random_btn = InlineKeyboardButton('🔁 Случайный отзыв', callback_data='rand_review')
    cancel_btn = InlineKeyboardButton('В главное меню', callback_data='cancel_review')

    kb.add(previous_btn, next_btn, first_btn, random_btn, cancel_btn)

    return kb


result_keyboard = get_keyboard()
