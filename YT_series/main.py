# import fastapi
# print(fastapi.__version__)

from fastapi import FastAPI
from mock_data import products
from mock_data import mock_students
from fastapi import Request
from dtos import Product_Item
app = FastAPI()

@app.get("/")
def home ():
    return "Hello FastApi "
# ******************************** simple static Ends Point ***************
@app.get("/products")
def get_products():
    return products


# ************************************* Path Params *************************
 
@app.get("/product/{product_id}")
def path_param(product_id:int):
    
    for i in products:
        if i.get("id") == product_id:
            return i 
    
    return "Product is Not Found "

@app.get("/students")
def get_students():
    return mock_students

@app.get("/student/{std_id}")
def student_by_id(std_id:int):
    
    for i in mock_students:
        if i.get("id") == std_id:
            return i
        
    return "Student Not Found"


# Querry params 
@app.get("/greet")
def greet_user(request:Request):
    querry_params = request.query_params
    return f"Hello {querry_params.get('name')}, Welcome to FastApi"


# Txypes of Request Body or data we send in the body of the request
# body , headers , querry params , path params

# diferent types of HTTP Methods
@app.post("/create_user")
def create_user(data:Product_Item):
    product_data = data.model_dump()
    products.append(product_data)
    
    return "User Created Successfully"

@app.put("/update_product/{product_id}")
def update_data(product_id:int, data:Product_Item):
    for i, product in enumerate(products):
        if product.get("id") == product_id:
            products[i] = data.model_dump()        
    return "Product Updated Successfully"
        
# How to validate the data using pydantic models DTOS
# How to call different Https Methods 

