import asyncio
from typing import Optional, List

from fastapi import FastAPI, status, HTTPException, Path, Depends
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models import get_db, create_db, Cabinet, Student


if __name__ == "__main__":
    asyncio.run(create_db())