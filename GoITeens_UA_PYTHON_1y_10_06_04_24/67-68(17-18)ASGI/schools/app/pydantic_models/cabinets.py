from typing import Optional

from pydantic import BaseModel


class CabinetModel(BaseModel):
    name: str
