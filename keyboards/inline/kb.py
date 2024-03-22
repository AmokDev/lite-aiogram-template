from aiogram.utils.keyboard import InlineKeyboardBuilder as Builder
from aiogram.types import (
    InlineKeyboardButton as Button,
    WebAppInfo
)

def example_keyboard():
    kb = Builder()
    url_button = Button(
        text = "Open URL",
        url = "https://t.me/amokek"
    )
    callback_button = Button(
        text = "View Info",
        callback_data = "view_info"
    )
    kb.row(callback_button)
    kb.row(url_button)
    return kb.as_markup()

def example_admin_keyboard():
    kb = Builder()
    admin_secret_callback_button = Button(
        text = "View Secret Info",
        callback_data = "view_secret_info"
    )
    kb.row(admin_secret_callback_button)
    return kb.as_markup()
