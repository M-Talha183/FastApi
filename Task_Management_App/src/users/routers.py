from fastapi import APIRouter, Depends , status
from sqlalchemy.orm import Session
from src.users.controller import register , login_user
from src.users.dtos import UserSchema , UserResponceModel
from src.utils.db import get_db

user_router = APIRouter(prefix="/user")

@user_router.post("/register", response_model=UserResponceModel, status_code=status.HTTP_201_CREATED)
def register_user(body: UserSchema, db: Session = Depends(get_db)):
    return register(body, db)


@user_router.post("/login", response_model=UserResponceModel, status_code=status.HTTP_200_OK)
def login_user(body: UserSchema, db: Session = Depends(get_db)):
    return controller.login_user(body,db)