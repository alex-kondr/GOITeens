from pydantic_settings import BaseSettings
from pydantic import BaseModel


class Settings(BaseSettings):
    sqlalchemy_uri: str


class UserModel(BaseModel):
    username: str
    password: str


class UserResponse(UserModel):
    id: str
    token: str


settings = Settings()

