from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    weather_api: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
