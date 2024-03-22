from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Update
from cachetools import TTLCache

from data.config import THROTTLING_RANGE

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self):
        self.cache = TTLCache(maxsize=10_000, ttl=THROTTLING_RANGE)

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        if event.chat.id in self.cache:
            return
        self.cache[event.chat.id] = None
        return await handler(event, data)
