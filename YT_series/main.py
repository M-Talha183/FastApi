# import fastapi
# print(fastapi.__version__)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home ():
    return "Hello FastApi "