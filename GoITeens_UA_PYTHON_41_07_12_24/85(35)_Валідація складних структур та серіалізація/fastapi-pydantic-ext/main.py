from typing import Optional, List, Dict

from fastapi import FastAPI, Header, Query, Body, status, HTTPException
import uvicorn
from pydantic import BaseModel, Field, EmailStr


class Number(BaseModel):
    number: str = Field(..., max_length=16, min_length=10, description="Номер телефону")


class Email(BaseModel):
    email: Optional[EmailStr] = Field(None, description="Email")


class Contact(BaseModel):
    first_name: str
    last_name: str = Field(..., max_length=20, min_length=3, description="Прізвище")
    number: List[Number] = Field(..., description="Список номерів")
    email: List[Email] = Field([], description="Список електронних адрес")


app = FastAPI()
CONTACTS: List[Contact] = []


@app.get("/contacts/", response_model=List[Contact])
async def get_contacts(token: str = Header(..., description="Токен авторизації")):
    if token and token == "secret_token":
        return CONTACTS

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен не пройшов перевірку")


@app.post("/contacts/", status_code=status.HTTP_201_CREATED, response_model=Contact)
async def add_contact(contact: Contact = Body(...)):
    if contact not in CONTACTS:
        CONTACTS.append(contact)
        return contact

    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Такий контакт вже існує")



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
