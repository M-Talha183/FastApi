from src.users.dtos import UserSchema , LoginSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException , status , Request
from src.users.models import UserModel
from src.users.models import UserModel
from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta
from src.utils.settings import settings
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

password_hash = PasswordHash.recommended()

def get_password_hash(password: str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def register(body:UserSchema , db: Session):
    is_user = db.query(UserModel).filter(UserModel.user_name == body.user_name).first()
    if is_user:
        raise HTTPException(status_code=400, detail="Username already exists!")
   
    is_user_email = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_user_email:
        raise HTTPException(status_code=400, detail="Email already exists!")    
    
    hash_password = get_password_hash(body.password)
    
    new_user = UserModel(
        name=body.name,
        user_name=body.user_name,
        hash_password=hash_password,
        email=body.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    
    return new_user

def login_user(body:LoginSchema, db:Session):
    user = db.query(UserModel).filter(UserModel.user_name == body.user_name).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    
    if not verify_password(body.password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    
    exp_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)
    token = jwt.encode({"user_id": user.id,"exp": exp_time.timestamp()}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    return {"token": token}

# TOken validation
def is_authenticated(request:Request, db:Session):
    
    try :
        token = request.headers.get("Authorization")
        if not token:
             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Yoy are not Authorized")
        token = token.split(" ")[1] 
        data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        user_id = data.get("_id")
    
    
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Yoy are not Authorized")

        return user
    except InvalidTokenError:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Yoy are not Authorized")

        