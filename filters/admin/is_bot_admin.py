from typing import Union
from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery, InlineQuery

from data.config import ADMINS


class isBotAdmin(BaseFilter):
    async def __call__(self, update: Union[Message, CallbackQuery, InlineQuery]) -> bool:
        return update.from_user.id in ADMINS
