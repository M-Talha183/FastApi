from fastapi import APIRouter, Depends , status
from sqlalchemy.orm import Session
from src.users.controller import register
from src.users.dtos import UserSchema
from src.utils.db import get_db

user_router = APIRouter(prefix="/user")

@user_router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(body: UserSchema, db: Session = Depends(get_db)):
    return register(body, db)