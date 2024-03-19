from aiogram import Bot, Dispatcher

from data.config import token
from utils.routers import reg_routers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from middlewares.throttling import ThrottlingMiddleware

async def reg_middlewares(dp: Dispatcher):
    dp.message.middleware(ThrottlingMiddleware())

async def main():
    bot = Bot(token)
    dp = Dispatcher()
    await set_default_commands(bot)
    await on_startup_notify(bot)
    await reg_middlewares(dp)
    await reg_routers(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
