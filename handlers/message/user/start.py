from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start(msg: Message):
    await msg.reply("Hi, this is start message", protect_content=True)
