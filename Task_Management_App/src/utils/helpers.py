from fastapi import Request, HTTPException, status ,Depends
from src.users.models import UserModel
from jwt.exceptions import  InvalidTokenError
from src.utils.settings import settings
import jwt
from sqlalchemy.orm import Session
from src.utils.db import get_db


# TOken validation
def is_authenticated(request:Request, db:Session = Depends(get_db)):
    
    try :
        token = request.headers.get("Authorization")
        if not token:
             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Yoy are not Authorized")
        token = token.split(" ")[1] 
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = data.get("user_id")
    
    
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Yoy are not Authorized")

        return user
    except InvalidTokenError:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Yoy are not Authorized")

        
