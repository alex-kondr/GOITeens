import asyncio
import logging

from fastapi import FastAPI, BackgroundTasks, status, Query, Depends, HTTPException
import uvicorn
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models import User, Message, get_db


app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test_backgroud")


async def send_message(text: str, user_id: int, db: AsyncSession = Depends(get_db)):
    message = Message(send_mail=text, user_id=user_id)
    db.add(message)
    await db.commit()
    logging.info(f"Повідомлення '{text}' успішно надіслано від користувача '{user_id}'")

    await asyncio.sleep(5)

    await db.refresh(message)
    message.incoming = f"Надійшла відповідь для користувача '{user_id}'"
    await db.commit()
    logging.info(f"Надійшла відповідь для користувача '{user_id}'")


@app.post("/send_mail/", status_code=status.HTTP_201_CREATED)
async def send_mail(
    backgroud_task: BackgroundTasks,
    text: str = Query(..., description="Повідомлення"),
    login: str = Query(..., description="Логін користувача"),
    db: AsyncSession = Depends(get_db)
):
    query = select(User).filter_by(login=login)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    backgroud_task.add_task(send_message, text=text, user_id=user.id)
    return dict(msg="Ваше повідомлення скоро буде надіслано")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
