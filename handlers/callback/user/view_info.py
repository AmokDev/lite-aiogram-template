from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(F.data == "view_info")
async def view_info(call: CallbackQuery):
    await call.answer(
        "My reaction to that information -> 😶‍🌫️",
        show_alert = True
    )
