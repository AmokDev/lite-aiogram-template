from aiogram.types import KeyboardButton as Button
from aiogram.utils.keyboard import ReplyKeyboardBuilder as Builder


def reply_menu_example():
    kb = Builder()
    button1 = Button(text="button1")
    button2 = Button(text="button2")
    button3 = Button(text="button3")
    kb.row(button1, button2)
    kb.row(button3)
    return kb.as_markup(resize_keyboard=True)
