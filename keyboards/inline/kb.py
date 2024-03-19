from aiogram.utils.keyboard import InlineKeyboardBuilder as ikb
from aiogram.types import (
    InlineKeyboardButton as btn,
    WebAppInfo
)

def example_keyboard():
    kb = ikb()
    url_button = btn(
        text = "Open URL",
        url = "https://t.me/amokek"
    )
    callback_button = btn(
        text = "View Info",
        callback_data = "view_info"
    )
    kb.row(callback_button)
    kb.row(url_button)
    return kb.as_markup()
