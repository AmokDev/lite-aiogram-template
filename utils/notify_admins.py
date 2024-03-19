from aiogram import Bot
import sys

from data.config import admins

async def on_startup_notify(bot: Bot):
    if len(sys.argv) == 3 and sys.argv[1] == "--updated":
        for admin in admins:
            version = sys.argv[2]
            await bot.send_message(admin, f"✅ Бот успешно обновлен до версии <b>{version}</b>!")
    else:
        for admin in admins:
            try:
                await bot.send_message(admin, "❗️Бот Запущен")
            except Exception as err:
                print(err)