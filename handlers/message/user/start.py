from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.inline import kb

router = Router()

@router.message(CommandStart())
async def start(msg: Message):
    await msg.reply(
        "Hi, this is start message",
        reply_markup=kb.example_keyboard()
    )
