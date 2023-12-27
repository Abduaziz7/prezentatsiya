from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

lang_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek", callback_data="uz"),
            InlineKeyboardButton(text="🇷🇺 Rus", callback_data="ru"),
            InlineKeyboardButton(text="🇺🇸 Englsh", callback_data="en")
        ]
    ], row_width=True
)


obuna_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="kanalga obuna bolish", url=f"https://t.me/abduaziztest", callback_data="urls")
        ]
    ], row_width=True
)

