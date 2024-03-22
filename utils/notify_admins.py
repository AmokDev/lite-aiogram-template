from aiogram import Bot
import logging

from data.config import ADMINS

async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(admin, "❗️ Bot Started")
        except Exception as err:
            logging.error(err)
