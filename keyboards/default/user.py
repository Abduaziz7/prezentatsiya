from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📞 Telefon raqamni yuborish', request_contact=True)
        ]
    ], resize_keyboard=True
)

locatsiya = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Geolokatsiya yuboring", request_location=True)
        ]
    ], resize_keyboard=True
)


menu_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
         KeyboardButton(text="👤 profil"),
        ],
        [
         KeyboardButton(text="🍴 menyu"),
         KeyboardButton(text="👨🏻‍💻 admin bilan bog'lanish")
        ],
    ],resize_keyboard=True
)






markup1 = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🍕 Pizza"),
            KeyboardButton("🌯 Lavash")
        ],
        [
            KeyboardButton("🍔 Gamburger"),
            KeyboardButton("🌭 Hot-Dog")
        ]
    ],
    resize_keyboard=True
)


markup2 = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🍕 Pipironi."),
            KeyboardButton("🍕 sirli.")
        ],
        [
            KeyboardButton("🍕 Goshli Miks."),
            KeyboardButton("🍕 Tovuqli.")
        ],
        [
            KeyboardButton("Orqaga◀")
        ]
    ],
    resize_keyboard=True
)


markup3 = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🌯 Big."),
            KeyboardButton("🌯 Mini.")
        ],
        [
            KeyboardButton("🌯 Sirli."),
            KeyboardButton("🌯 Sirli Mini.")
        ],
        [
            KeyboardButton("Orqaga◀")
        ]
    ],
    resize_keyboard=True
)


markup4 = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🍔 Big Chizburger."),
            KeyboardButton("🍔 Chizburger.")
        ],
        [
            KeyboardButton("🍔 Gamburger."),
            KeyboardButton("🍔 Big.")
        ],
        [
            KeyboardButton("Orqaga◀")
        ]
    ],
    resize_keyboard=True
)


markup5 = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🌭 Odi."),
            KeyboardButton("🌭 Sirli.")
        ],
        [
            KeyboardButton("🌭 Qirollarga."),
            KeyboardButton("🌭 Xaggi.")
        ],
        [
            KeyboardButton("Orqaga◀")
        ]
    ],
    resize_keyboard=True
)


markup6 = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Ha✅"),
            KeyboardButton("Yoq✖")
        ]
    ],
    resize_keyboard=True
)