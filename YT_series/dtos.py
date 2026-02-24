from pydantic import BaseModel

class Product_Item (BaseModel):
    id : int
    name : str
    price : float
    description : str