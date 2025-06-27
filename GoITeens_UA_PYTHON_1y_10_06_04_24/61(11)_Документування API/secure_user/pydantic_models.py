from typing import Optional

from pydantic_settings import BaseSettings
from pydantic import BaseModel, EmailStr


class Settings(BaseSettings):
    sqlalchemy_uri: str


class UserModel(BaseModel):
    username: str
    password: str


class UserResponse(UserModel):
    id: str
    token: Optional[str] = None


class UserPassword(BaseModel):
    password: str


class ContactModel(BaseModel):
    name: str
    phone_number: str
    address: Optional[str] = None
    email: Optional[str] = None


class ContactModelResponse(ContactModel):
    id: str
    user_id: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


settings = Settings()

