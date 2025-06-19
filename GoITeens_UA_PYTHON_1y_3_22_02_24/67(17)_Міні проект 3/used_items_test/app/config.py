from datetime import timedelta

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_uri: str = "mysql://localhost:3000/db"
    secret_key: str = "secret_key"
    algorithm: str = "HS256"
    access_token_expire_min: timedelta = timedelta(minutes=1)


settings = Settings()
