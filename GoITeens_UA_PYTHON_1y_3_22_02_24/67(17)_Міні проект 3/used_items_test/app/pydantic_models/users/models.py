from pydantic import BaseModel


class UserModel(BaseModel):
    username: str
    password: str


class UserModelDB(BaseModel):
    id: str
    username: str
    disabled: bool


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
