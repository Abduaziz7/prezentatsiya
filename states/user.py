from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterStates(StatesGroup):
    language = State()
    full_name = State()
    phone_number = State()


class locationStates(StatesGroup):
    location = State()

