import os
from datetime import datetime, timedelta
import random
import string

from dotenv import load_dotenv

from app.db import Session, User


load_dotenv()
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


def get_temp_pass() -> tuple[str, datetime]:
    time_expected = datetime.now() + timedelta(minutes=1)
    pass_char = string.ascii_letters + string.digits
    temp_pass = "".join(random.choices(pass_char, k=8))
    return temp_pass, time_expected


def get_user(user_name, password, temp_pass):
    with Session() as session:
        if temp_pass:
            user = session.query(User).where(User.temp_pass == temp_pass).first()
            if user and user.time_expected > datetime.now():
                return user

        user = session.query(User).where(User.user_name == user_name).where(User.password == password).first()
        if user:
            user.temp_pass, user.time_expected = get_temp_pass()
            session.commit()
            return user
