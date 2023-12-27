# from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
# from middlewares.subscription import CheckSub


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())

