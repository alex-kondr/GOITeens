import os
from datetime import datetime, timedelta
import random
import string

from dotenv import load_dotenv


load_dotenv()
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


def get_temp_pass():
    time_delta = timedelta(minutes=1)
    time_expected = datetime.now() + time_delta
    pass_char = string.ascii_letters + string.digits + string.punctuation
    temp_pass = random.choices(pass_char, k=8)