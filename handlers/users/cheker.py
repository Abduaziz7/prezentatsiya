from aiogram import Bot
from data.config import chek

async def check(user_id):
    bot = Bot.get_current()
    member = await bot.get_chat_member(user_id=user_id, chat_id=chek[0])
    return member.is_chat_member()


