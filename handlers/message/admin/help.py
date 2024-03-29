from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from filters.admin.is_bot_admin import isBotAdmin
from filters.user.chat_type import ChatType
from keyboards.inline import kb

router = Router()
router.message.filter(
    isBotAdmin(),
    ChatType(chat_type = ["private"])
)

@router.message(Command("help"))
async def help(msg: Message):
    await msg.reply(
        "Hi, this is admin-secret message",
        protect_content=True,
        reply_markup=kb.example_admin_keyboard()
    )
