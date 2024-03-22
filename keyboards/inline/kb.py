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

def example_admin_keyboard():
    kb = ikb()
    admin_secret_callback_button = btn(
        text = "View Secret Info",
        callback_data = "view_secret_info"
    )
    kb.row(admin_secret_callback_button)
    return kb.as_markup()
