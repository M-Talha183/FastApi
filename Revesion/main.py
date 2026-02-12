from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name : str 
    price : float
    is_offer : bool | None = None 
    

#  Handle the Root path 
@app.get("/")
def read_home():
    return {"Hello":"world"}

@app.get("/items")
def myitems():
    return ["item 1 ","item 2 ","item 3 ","item 4 ","item 5 ",]
# Handle the dynamic id 
@app.get("/items/{item_id}")
def get_dynamic_item(item_id : int , q : str | None = None):
    return {"item_id": item_id, "q": q}

# Handle the put request where data is vaidate by pydantic 
@app.put("/items/{item_id}")
def update_item (item_id : int , item :Item):
    return{"Item name ":item.name , "Item_id":item_id}


# ## FastAPI Overview: The Modern High-Performance Framework

# ### 1. Purpose

# FastAPI solves the "productivity vs. performance" tradeoff in Python web development. It provides a way to build production-ready, highly performant APIs with minimal boilerplate, while leveraging Python's type system to eliminate common developer errors (like data type mismatches) and automate documentation.

# ---

# ### 2. Core Idea

# The main concept is **"Declare once, use everywhere."** By using standard Python type hints in your function signatures, FastAPI automatically handles data validation, serialization, and the generation of interactive API documentation (OpenAPI).

# ---

# ### 3. Key Components

# * **FastAPI Class:** The main entry point that creates the application instance.
# * **Pydantic (BaseModel):** The engine used for data validation and schema definition.
# * **Starlette:** The underlying ASGI framework handling the high-performance web routing.
# * **Path Operations:** Decorators like `@app.get()` or `@app.put()` that link URL paths to Python functions.
# * **Uvicorn/FastAPI CLI:** The lightning-fast server used to run the application.

# ---

# ### 4. Code Breakdown

# ```python
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI() # 1. Initialize the API

# class Item(BaseModel): # 2. Define data structure with Pydantic
#     name: str
#     price: float
#     is_offer: bool | None = None

# @app.put("/items/{item_id}") # 3. Define path and HTTP method
# def update_item(item_id: int, item: Item): # 4. Declare types for params and body
#     return {"item_name": item.name, "item_id": item_id} # 5. Return dict (auto-converted to JSON)

#  ```

# 1. **`app = FastAPI()`**: Creates the central object that coordinates routes and docs.
# 2. **`class Item(BaseModel)`**: Defines what a valid "Item" looks like. If a request lacks a `price`, FastAPI will automatically reject it.
# 3. **`@app.put(...)`**: Tells FastAPI that requests using the `PUT` method at this URL should trigger the following function.
# 4. **`item_id: int, item: Item`**:
# * `item_id` is pulled from the URL path and converted to an integer.
# * `item` is pulled from the JSON request body and validated against the `Item` model.


# 5. **`return`**: The Python dictionary is automatically converted into a JSON response.

# ---

# ### 5. Execution Flow

# 1. **Request Arrival:** A client sends an HTTP request.
# 2. **Parsing & Validation:** FastAPI extracts data from the path, query parameters, or body. It uses **Pydantic** to verify the data matches your type hints.
# 3. **Error Handling:** If validation fails (e.g., sending a string for an `int` field), FastAPI sends a detailed 422 Unprocessable Entity error back to the client immediately.
# 4. **Business Logic:** If valid, your function executes.
# 5. **Serialization:** FastAPI takes your returned Python object and converts it to JSON.
# 6. **Response:** The client receives the JSON and the appropriate HTTP status code.

# ---

# ### 6. Practical Example

# Imagine building a **Product Management System**.

# * **Input:** You define a model for products (name, price, stock).
# * **Safety:** If a junior dev tries to send a product without a price, the API blocks it automatically.
# * **Documentation:** You send the `/docs` link to your Frontend team; they can see exactly what the data looks like and test the endpoints directly in the browser without needing a separate tool like Postman.

# ---

# ### 7. Key Takeaways

# * **Auto-Documentation:** You get Swagger UI and ReDoc for free, synchronized with your code in real-time.
# * **Standard Python:** Uses modern type hints (`variable: type`), meaning excellent IDE autocompletion and no new syntax to learn.
# * **Performance:** It's built on Starlette and Uvicorn, making it one of the fastest Python frameworks available (comparable to Go or Node.js).
# * **Data Integrity:** Automatic conversion of network data to Python objects and vice versa, with strict validation included.

# Would you like me to create a boilerplate project structure for a more complex FastAPI application?


