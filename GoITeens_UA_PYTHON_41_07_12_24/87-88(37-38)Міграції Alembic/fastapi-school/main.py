import asyncio
from typing import Optional, List, Annotated

from fastapi import FastAPI, status, HTTPException, Path, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_, and_
import uvicorn

from models import get_db, create_db, Cabinet, Student
from pydantic_models import StudentModel, StudentModelResponse, CabinetModel, CabinetModelResponse


app = FastAPI()


@app.post("/cabinets/", status_code=status.HTTP_201_CREATED, response_model=CabinetModelResponse)
async def add_cabinet(
    cabinet_model: CabinetModel,
    db: Annotated[AsyncSession, Depends(get_db)]
    # db: AsyncSession = Depends(get_db)
):
    # query1 = select(Cabinet).filter_by(name=cabinet_model.name)
    # query2 = select(Cabinet).filter_by(number=cabinet_model.number)
    # cabinet1 = await db.scalar(query1)
    # cabinet2 = await db.scalar(query2)

    query = select(Cabinet).where(or_(Cabinet.name==cabinet_model.name, Cabinet.number==cabinet_model.number))
    cabinet = await db.scalar(query)
    # if cabinet1 or cabinet2:
    if cabinet:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Кабінет з такими параметрами вже існує")

    cabinet = Cabinet(**cabinet_model.model_dump())
    db.add(cabinet)
    await db.commit()
    return cabinet


@app.get("/cabinets/", status_code=status.HTTP_200_OK, response_model=List[CabinetModelResponse])
async def get_cabinets(
    db: Annotated[AsyncSession, Depends(get_db)],
    offset: int = Query(0),
    limit: int = Query(10, gt=0)
):
    query = select(Cabinet).offset(offset).limit(limit)
    return await db.scalars(query)


if __name__ == "__main__":
    # asyncio.run(create_db())
    uvicorn.run("main:app", reload=True)