from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from data.config import TOKEN
from utils.routers import reg_routers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from middlewares.throttling import ThrottlingMiddleware

async def reg_middlewares(dp: Dispatcher):
    dp.message.middleware(ThrottlingMiddleware())

bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

async def main():
    await set_default_commands(bot)
    await on_startup_notify(bot)
    await reg_middlewares(dp)
    await reg_routers(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
