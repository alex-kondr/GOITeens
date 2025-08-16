from typing import Optional, List

from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import User, UserThemAssoc, Subject, Cabinet, Role
from app.config import settings
from app.pydantic_models.users import UserModel, UserModelResponse, TokenModel
from app.pydantic_models.subjects import SubjectModel


async def get_user(id: int, db: AsyncSession) -> Optional[User]:
    return await db.scalar(select(User).filter_by(id=id))


async def sign_up(user_model: UserModel, db: AsyncSession) -> None:
    user = User(**user_model.model_dump())
    db.add(user)
    await db.commit()


async def sign_in(name: str, password: str, db: AsyncSession) -> Optional[str]:
    user: Optional[User] = await db.scalar(select(User).filter_by(name=name))
    if not user:
        return

    return user.get_token(pwd=password)


async def add_subject(subject_model: SubjectModel, db: AsyncSession, user_id: int) -> bool:
    user: Optional[User] = await db.scalar(select(User).filter_by(id=user_id, role=Role.admin))
    if not user:
        return False

    subject = await db.scalar(select(Subject).filter_by(name=subject_model.name))
    if subject:
        return False

    subject = Subject(**subject_model.model_dump())
    db.add(subject)
    await db.commit()
    return True


async def get_subject(subject_id: int, db: AsyncSession) -> Optional[Subject]:
    return await db.scalar(select(Subject).filter_by(id=subject_id))


async def get_subjects(db: AsyncSession) -> List[Subject]:
    return await db.scalars(select(Subject))


async def add_subject_to_user(user_id: int, member_id: int, subject_id: int, db: AsyncSession) -> bool:
    user: Optional[User] = await db.scalar(select(User).filter(User.id == user_id, or_(User.role == Role.admin, User.role == Role.editor)))
    if not user:
        return False

    user_them_assoc = await db.scalar(select(UserThemAssoc).filter_by(user_id=member_id, subject_id=subject_id))
    if user_them_assoc:
        return False

    user_them_assoc = UserThemAssoc(user_id=member_id, subject_id=subject_id)
    db.add(user_them_assoc)
    await db.commit()
    return True


async def remove_subject(user_id: int, subject_id: int, db: AsyncSession) -> bool:
    user: Optional[User] = await db.scalar(select(User).filter_by(id=user_id, role=Role.admin))
    if not user:
        return False

    subject: Optional[Subject] = await db.scalar(select(Subject).filter_by(id=subject_id))
    if not subject:
        return False

    await db.delete(subject)
    await db.commit()
    return True
