from typing import Optional, Annotated

from pydantic import BaseModel, Field, ConfigDict


class UserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Annotated[Optional[str], Field(None, description="Ім'я користувача")]
    email: Annotated[str, Field(..., description="Електронна пошта")]
    password: Annotated[str, Field(..., description="Пароль", min_length=6)]


class UserModelResponse(BaseModel):
    id: int
    name: Optional[str]
    email: str
