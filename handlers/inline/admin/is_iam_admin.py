from aiogram import Router, F
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle

from filters.admin.isBotAdmin import isBotAdminQ

router = Router()
router.inline_query.filter(
    isBotAdminQ()
)

@router.inline_query(F.query == "admin")
async def is_iam_admin(q: InlineQuery):
    query_result = InlineQueryResultArticle(
        id = "2",
        title = "Is I'm admin?",
        input_message_content = InputTextMessageContent(
            message_text = f"Yes, I'm an admin!"
        )
    )
    await q.answer(
        [query_result],
        cache_time = 1
    )
