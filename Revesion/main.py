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