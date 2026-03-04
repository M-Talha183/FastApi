from fastapi import APIRouter, Depends , status ,Request
from sqlalchemy.orm import Session
from src.users.controller import register 
from src.users.dtos import UserSchema , UserResponceModel , LoginSchema
from src.utils.db import get_db
from src.users import controller

user_router = APIRouter(prefix="/user")

@user_router.post("/register", response_model=UserResponceModel, status_code=status.HTTP_201_CREATED)
def register_user(body: UserSchema, db: Session = Depends(get_db)):
    return register(body, db)


@user_router.post("/login", status_code=status.HTTP_200_OK)
def login_user(body: LoginSchema, db: Session = Depends(get_db)):
    return controller.login_user(body, db)


@user_router.get("/is_auth", status_code=status.HTTP_200_OK, response_model=UserResponceModel)
def is_auth(request:Request , db: Session = Depends(get_db)):
    return controller.is_authenticated(request,db)