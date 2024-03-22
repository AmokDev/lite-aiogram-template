from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery, InlineQuery

from data.config import admins

class isBotAdmin(BaseFilter):
    async def __call__(self, msg: Message) -> bool:
        if msg.from_user.id in admins:
            return True
        else:
            return False

class isBotAdminCall(BaseFilter):
    async def __call__(self, call: CallbackQuery) -> bool:
        if call.from_user.id in admins:
            return True
        else:
            return False

class isBotAdminQ(BaseFilter):
    async def __call__(self, q: InlineQuery) -> bool:
        if q.from_user.id in admins:
            return True
        else:
            return False
