# import fastapi
# print(fastapi.__version__)

from fastapi import FastAPI
from mock_data import products
from mock_data import mock_students
app = FastAPI()

@app.get("/")
def home ():
    return "Hello FastApi "
# ******************************** simple static Ends Point ***************
@app.get("/products")
def get_products():
    return products


# ************************************* Path Params *************************
 
# @app.get("/product/{product_id}")
# def path_param(product_id:int):
    
#     for i in products:
#         if i.get("id") == product_id:
#             return i 
    
#     return "Product is Not Found "

@app.get("/students")
def get_students():
    return mock_students

@app.get("/student/{std_id}")
def student_by_id(std_id:int):
    
    for i in mock_students:
        if i.get("id") == std_id:
            return i
        
    return "Student Not Found"
