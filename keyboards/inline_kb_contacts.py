from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_inline_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    inline_btn = InlineKeyboardButton('Связать со мной', url='t.me/astr_wash_and_go', callback_data='send_msg')

    ikb.add(inline_btn)

    return ikb


contacts_inl_kb = get_inline_keyboard()
