from typing import Optional, List

from pydantic import BaseModel, Field


class CabinetModel(BaseModel):
    name: str = Field(..., min_length=3, description="Назва кабінету")
    number: int = Field(..., ge=1, le=100, description="Номер кабінету")


class CabinetModelResponse(CabinetModel):
    id: int
    # students: List["StudentModelResponse"] = []


class StudentModel(BaseModel):
    full_name: str = Field(..., min_length=3, description="Ім'я та прізвище учня")
    cabinet_name: Optional[str] = Field(None, description="Назва кабінету")
    cabinet_number: Optional[int] = Field(None, description="Номер кабінету")


class StudentModelResponse(BaseModel):
    id: int
    full_name: str
    cabinet: Optional[CabinetModelResponse] = None
