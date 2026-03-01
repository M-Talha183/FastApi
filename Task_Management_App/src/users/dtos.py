from pydantic import BaseModel

class UserSchema(BaseModel):
    name : str 
    user_name : str
    password : str
    email : str 
    
    
class UserResponceModel(BaseModel):
    name : str 
    user_name : str
    email : str 
    id : int
    