from pydantic import BaseModel


class SubjectModel(BaseModel):
    name: str


class SubjectModelResponse(SubjectModel):
    id: int
