from aiogram import Router, F
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle

router = Router()

@router.inline_query(F.query == "getid")
async def get_my_id(q: InlineQuery):
    query_result = InlineQueryResultArticle(
        id = "1",
        title = "Get my ID",
        input_message_content = InputTextMessageContent(
            message_text = f"My id is <code>{q.from_user.id}</code>"
        )
    )
    await q.answer(
        [query_result],
        cache_time = 1
    )
