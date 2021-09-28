import asyncio
from deta import Deta
from fastapi_users_db_deta_base import DetaBaseUserDatabase
from fastapi_users_db_deta_base import deta_base_async
from app.models import UserDB


def get_user_db():
    loop = asyncio.get_event_loop()
    deta = Deta()
    db = deta.Base("users")
    yield DetaBaseUserDatabase(
        UserDB, deta_base_async.wrap_deta_base_async(loop, db))
