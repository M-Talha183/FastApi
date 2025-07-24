from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def hello():
    return {"message ":"Hello IN Fast Api world"}

@app.get("/about")
def about():
    return {"message ": "Muhammad Talha is the student of the smiu "}

@app.get("/contact")
def about():
    return {"message ": "Muhammad Talha is the student of the smiu "}