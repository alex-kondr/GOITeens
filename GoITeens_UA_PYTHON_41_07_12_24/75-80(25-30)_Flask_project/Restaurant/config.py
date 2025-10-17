from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    sqlalchemy_uri: str = "posgresql+psycopg2://user:password@localhost:5432/db_name"
    secret_key: str = "your secret key"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
