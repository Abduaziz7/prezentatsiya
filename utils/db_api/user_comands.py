from main.models import users
from main.database_set import database


async def add_user(data: dict):
    try:
        query = users.insert().values(
            full_name=data.get('full_name'),
            phone_number=data.get('phone_number'),
            language="uz",
            chat_id=data.get("chat_id"),
        )

        new_user = await database.execute(query=query)
        return new_user
    except Exception as exc:
        print(exc)
        return False


async def get_uesr(chat_id: int):
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        user = await database.fetch_one(query=query)
        return user
    except Exception as exc:
        print(exc)
        return False


async def get_all_profil():
    try:
        query = users.select()
        all_fruits = await database.fetch_all(query)
        return all_fruits
    except Exception as exc:
        print(exc)
        return None
