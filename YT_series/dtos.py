from pydantic import BaseModel

class Product_Item (BaseModel):
    id : int
    title : str
    price : float
    count: int