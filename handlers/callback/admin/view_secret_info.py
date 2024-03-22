from aiogram import Router, F
from aiogram.types import CallbackQuery

from filters.admin.is_bot_admin import isBotAdmin

router = Router()
router.callback_query.filter(
    isBotAdmin()
)

@router.callback_query(F.data == "view_secret_info")
async def view_info(call: CallbackQuery):
    await call.answer("pashalkoo uraa")
