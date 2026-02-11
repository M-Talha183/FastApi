from fastapi import FastAPI
app = FastAPI()

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


#  Data valaidation 

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

# data types 
def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))
