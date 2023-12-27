from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from utils.db_api.user_comands import get_uesr
from keyboards.default.user import *
from states.user import locationStates


@dp.message_handler(text="👤 profil")
async def profil_handler(message: types.Message, state: FSMContext):
    user = await get_uesr(chat_id=message.chat.id)
    if user:
        name = user['full_name']
        phone_number = user['phone_number']

        text = f"name:{name}\n phone number: {phone_number}"
        await message.answer(text=text, reply_markup=menu_keyboards)


@dp.message_handler(text="👨🏻‍💻 admin bilan bog'lanish")
async def admin_handler(message: types.Message):
    text = f"admin telefon raqami: 88-188-72-92, \n admin ismi: Abduvoris"
    await message.answer(text=text, reply_markup=menu_keyboards)


@dp.message_handler(text="🍴 menyu")
async def menyu_handler(message: types.Message):
    text = "menyuga hush kelibsiz"
    await message.answer(text=text, reply_markup=markup1)


@dp.message_handler(text="🍕 Pizza")
async def pitsa_nemu_handler(message: types.Message):
    text = "Qanaqa Pizza hohlaysiz"
    await message.answer(text=text, reply_markup=markup2)


@dp.message_handler(text="🍕 Pipironi.")
async def bot_starts(message: types.Message):
    photo1 = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F601282db-7274-43e4-ac74-e8987d53dd6e.jpg&w=1920&q=100"
    await message.answer_photo(photo=photo1)
    await message.answer("50 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="🍕 sirli.")
async def bot_starts(message: types.Message):
    photo1 = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2Ffd253a59-c094-468e-bb31-bda637aa9dcd.jpg&w=1920&q=100"
    await message.answer_photo(photo=photo1)
    await message.answer("30 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="🍕 Goshli Miks.")
async def bot_starts(message: types.Message):
    photo1 = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2Fc14e362c-57a5-49fd-9a80-b14ce099b777.jpg&w=1920&q=100"
    await message.answer_photo(photo=photo1)
    await message.answer("90 000 So'm, Olasizmi", reply_markup=markup6)

@dp.message_handler(text="🍕 Tovuqli.")
async def bot_starts(message: types.Message):
    photo1 = "https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F5fb58b09-5c77-44de-8de8-f1be55c2aef1.jpg&w=1920&q=100"
    await message.answer_photo(photo=photo1)
    await message.answer("60 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="🌯 Lavash")
async def bot_starts(message: types.Message):
    await message.answer("Qanaqa Lavash hohlaysiz", reply_markup=markup3)


@dp.message_handler(text="🌯 Big.")
async def bot_starts(message: types.Message):
    photo1 = "http://cc.oqtepalavash.uz/api/image/33f5cfcb-0071-4f1a-bgit1f1-22dc1de28f3b.jpg"
    await message.answer_photo(photo=photo1)
    await message.answer("28 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="🌯 Mini.")
async def bot_starts(message: types.Message):
    photo1 = "http://cc.oqtepalavash.uz/api/image/3f6efb6f-1659-4899-abd2-70d61fe34560.jpg"
    await message.answer_photo(photo=photo1)
    await message.answer("23 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="🌯 Sirli.")
async def bot_starts(message: types.Message):
    photo1 = "http://cc.oqtepalavash.uz/api/image/483107e9-8235-4ba2-ad5d-44bd23de9ae5.jpg"
    await message.answer_photo(photo=photo1)
    await message.answer("30 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="🌯 Sirli Mini.")
async def bot_starts(message: types.Message):
    photo1 = "http://cc.oqtepalavash.uz/api/image/f540b1ff-39ed-4716-9edd-f4307a413ced.jpg"
    await message.answer_photo(photo=photo1)
    await message.answer("26 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="🍔 Gamburger")
async def bot_start(message: types.Message):
    await message.answer("Qanaqa Gamnburger hohlaysiz", reply_markup=markup4)


@dp.message_handler(text="🍔 Big Chizburger.")
async def bot_starts(message: types.Message):
    photo1 = "http://cc.oqtepalavash.uz/api/image/f3bf2f3a-29ff-4ea1-961c-fd84018c5fb1.jpg"
    await message.answer_photo(photo=photo1)
    await message.answer("37 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="🍔 Chizburger.")
async def bot_starts(message: types.Message):
    photo1 = "http://cc.oqtepalavash.uz/api/image/46c6f5d0-7542-4d10-bacd-3f65ee788b27.jpg"
    await message.answer_photo(photo=photo1)
    await message.answer("24 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="🍔 Gamburger.")
async def bot_starts(message: types.Message):
    photo1 = "http://cc.oqtepalavash.uz/api/image/ebf8f94e-af46-4bc1-b065-189b58bf0180.jpg"
    await message.answer_photo(photo=photo1)
    await message.answer("22 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="🍔 Big.")
async def bot_starts(message: types.Message):
    photo1 = "http://cc.oqtepalavash.uz/api/image/c8299ff7-649c-4328-9555-d6f268efe5af.jpg"
    await message.answer_photo(photo=photo1)
    await message.answer("30 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="🌭 Hot-Dog")
async def bot_start(message: types.Message):
    await message.answer("Qanaqa hot-dog hohlaysiz", reply_markup=markup5)


@dp.message_handler(text="🌭 Odi.")
async def bot_starts(message: types.Message):
    photo1 = "http://cc.oqtepalavash.uz/api/image/5707eeac-ee0a-4c55-9ce5-2a8f81e76293.jpg"
    await message.answer_photo(photo=photo1)
    await message.answer("11 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="🌭 Sirli.")
async def bot_starts(message: types.Message):
    photo1 = "http://cc.oqtepalavash.uz/api/image/584bad06-c07e-418c-a36b-df80751950c5.jpg"
    await message.answer_photo(photo=photo1)
    await message.answer("14 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="🌭 Qirollarga.")
async def bot_starts(message: types.Message):
    photo1 = "http://cc.oqtepalavash.uz/api/image/400839bb-7f05-474e-a5ff-6962b1445ff7.jpg"
    await message.answer_photo(photo=photo1)
    await message.answer("22 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="🌭 Xaggi.")
async def bot_starts(message: types.Message):
    photo1 = "http://cc.oqtepalavash.uz/api/image/0b8c355f-c7df-4335-99eb-4eb3fbe6fa2a.jpg"
    await message.answer_photo(photo=photo1)
    await message.answer("30 000 So'm, Olasizmi", reply_markup=markup6)


@dp.message_handler(text="📍 Geolokatsiya yuboring", content_types=types.ContentType.LOCATION)
async def bot_starts(message: types.Message, state: FSMContext):
    await state.update_data(longitude=message.location.longitude, latitude=message.location.latitude)
    text = "Zakazingiz uchum rahmat Yarim soatda zakazingizni olasiz "
    await message.answer(text=text, reply_markup=markup6)
    await state.finish()


@dp.message_handler(text="Orqaga◀")
async def bot_starts(message: types.Message):
    await message.answer("Sizga nima kerak ?", reply_markup=markup1)


@dp.message_handler(text="Yoq✖")
async def bot_starts(message: types.Message):
    await message.answer("Sizga nima kerak ?", reply_markup=markup1)


@dp.message_handler(text="Ha✅")
async def bot_starts(message: types.Message):
    await message.answer(f"Manzilni yuboring", reply_markup=locatsiya)
    await locationStates.location.set()

