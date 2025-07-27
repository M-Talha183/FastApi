from fastapi import FastAPI ,Path ,HTTPException
import json
app = FastAPI()



def load_data():
    with open("patients.json", "r") as f:
        data  = json.load(f)
        
    return data  

@app.get("/")
def hello():
    return {"message": "Patient Managememnt System API"}



@app.get("/about")
def hello():
    return {"message": " A fully functional API to manange your patient records"}


@app.get("/view")
def view():
    data = load_data()
    
    return data


@app.get("/patient/{patient_id}")
def view_patient_id(patient_id :str= Path(...,description="ID of patient in the DB ",example="P001")):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    return HTTPException(status_code=404 , detail='Patient not found')