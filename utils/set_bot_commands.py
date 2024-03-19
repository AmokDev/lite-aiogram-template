from aiogram.types import BotCommand
from aiogram import Bot

async def set_default_commands(bot: Bot):
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Запустить бота")
        ]
    )