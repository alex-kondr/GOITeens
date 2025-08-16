from typing import Optional, List, Annotated

from fastapi import APIRouter, HTTPException, status, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import get_db, Subject
from app.pydantic_models.subjects import SubjectModel, SubjectModelResponse
from app.routes.users import get_user_id
from app.db import db_actions


subjects_route = APIRouter(prefix="/subjects", tags=["Subject"])


@subjects_route.post("/", status_code=status.HTTP_201_CREATED)
async def add_subject(
    subject_model: SubjectModel,
    user_id: Annotated[int, Depends(get_user_id)],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    result = await db_actions.add_subject(subject_model=subject_model, user_id=user_id, db=db)
    if not result:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)
    return dict(msg="Новий предмет успішно додано")



@subjects_route.get("/", status_code=status.HTTP_202_ACCEPTED, response_model=List[SubjectModelResponse])
async def get_subjects(
    user_id: Annotated[int, Depends(get_user_id)],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    return await db_actions.get_subjects(db=db)


@subjects_route.get("/{subject_id}/", status_code=status.HTTP_202_ACCEPTED, response_model=SubjectModel)
async def get_subject(
    user_id: Annotated[int, Depends(get_user_id)],
    db: Annotated[AsyncSession, Depends(get_db)],
    subject_id: int = Path(...)
):
    subject: Optional[Subject] = await db_actions.get_subject(subject_id=subject_id, db=db)
    if not subject:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return subject


@subjects_route.patch("/{subject_id}/{student_id}/", status_code=status.HTTP_202_ACCEPTED)
async def add_subject_to_user(
    user_id: Annotated[int, Depends(get_user_id)],
    db: Annotated[AsyncSession, Depends(get_db)],
    subject_id: int = Path(...),
    student_id: int = Path(...)
):
    result = await db_actions.add_subject_to_user(
        user_id=user_id,
        member_id=student_id,
        db=db,
        subject_id=subject_id
    )
    if not result:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)

    return dict(msg="Предмет успішно додано до студента")


@subjects_route.delete("/{subject_id}/", status_code=status.HTTP_202_ACCEPTED)
async def remove_subject(
    user_id: Annotated[int, Depends(get_user_id)],
    db: Annotated[AsyncSession, Depends(get_db)],
    subject_id: int = Path(...)
):
    result = await db_actions.remove_subject(user_id=user_id, subject_id=subject_id, db=db)
    if not result:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)

    return dict(msg="Успішно видалено")
