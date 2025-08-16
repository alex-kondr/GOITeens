from typing import Optional, List

from pydantic import BaseModel, Field

from app.db.models import Role
from app.pydantic_models.cabinets import CabinetModel
from app.pydantic_models.subjects import SubjectModelResponse


class UserModel(BaseModel):
    name: str
    password: str
    role: Role = Field(Role.student)


class UserModelResponse(BaseModel):
    id: int
    name: str
    role: Role
    cabinet: Optional[CabinetModel] = None
    subjects: List[SubjectModelResponse] = []


class TokenModel(BaseModel):
    access_token: str
    type_token: str = "Bearer"
