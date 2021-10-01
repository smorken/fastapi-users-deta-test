from deta import Deta
import traceback
from fastapi_users_db_deta_base import DetaBaseUserDatabase
from app.models import UserDB


def get_user_db():
    deta = Deta()
    db1 = deta.Base("debug")
    try:
        db = deta.AsyncBase("users")
        yield DetaBaseUserDatabase(
            UserDB, db)
    except:
        # temporary debugging
        db1.put({"error": traceback.format_exc()})
