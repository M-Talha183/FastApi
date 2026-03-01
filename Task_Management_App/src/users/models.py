from sqlalchemy import Column, String , Integer , DateTime , Boolean
from src.utils.db import Base

class UserModel(Base):
    __tablename__ = "user_table"
    
    id = Column(Integer , primary_key=True)
    name = Column(String(25))
    user_name = Column(String(100), nullable=False)
    hash_password = Column(String(255),nullable=False)
    email = Column(String(100))