from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    sqlalchemy_uri: str = "mysql+aiomysql://127.0.0.1:5432/db_name"
    secret_key: str = "your secret key"
    algorithm: str = "algorithm"
    exp_time_minutes: int = 30

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
