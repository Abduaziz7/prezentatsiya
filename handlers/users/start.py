from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.user import RegisterStates
from loader import dp
from aiogram.dispatcher import FSMContext
from utils.db_api.user_comands import get_uesr, add_user
from keyboards.default.user import phone_number, menu_keyboards
from keyboards.inline.user import lang_keyboard


# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     text = ('assalomu alaykum, botga obuna boling')
#     await message.answer(text=text, reply_markup=obuna_keyboard)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if await get_uesr(chat_id=message.chat.id):
        text = ('assalomu alaykum, xush kelibsiz')
        await message.answer(text=text, reply_markup=menu_keyboards)
    else:
        text = "Iltimos o'zingiz bilganingizni tanlang "
        await message.answer(text=text, reply_markup=lang_keyboard)
        await RegisterStates.language.set()


@dp.callback_query_handler(state=RegisterStates.language)
async def get_lang_handlers(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(language=call.data)
    text = 'assalomu alaykum, iltimos ismingizni kriting.'
    await call.message.answer(text=text)
    await RegisterStates.full_name.set()


@dp.message_handler(state=RegisterStates.full_name)
async def full_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text, chat_id=message.chat.id)
    text = "iltimos telefon raqamingizni kriting"
    await message.answer(text=text, reply_markup=phone_number)
    await RegisterStates.phone_number.set()


@dp.message_handler(state=RegisterStates.phone_number, content_types=types.ContentType.CONTACT)
async def phone_numbers_handlers(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    user = await add_user(data=data)
    if user:
        text = "hushkelibsiz"
        await message.answer(text=text, reply_markup=menu_keyboards)
    else:
        text = "kechirasiz botda hatolik bor"
        await message.answer(text=text, reply_markup=menu_keyboards)
    await state.finish()


