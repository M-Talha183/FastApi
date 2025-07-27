from fastapi import FastAPI ,Path ,HTTPException , Query
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
    raise HTTPException(status_code=404 , detail='Patient not found')

@app.get("/sort")
def sort_patients(sort_by:str = Query(...,description='Sort on the basis on height , weight or bmi '),
                order : str = Query('asc', description="sort in asc or dsc order")):
    
    valid_field = ['height','weight','bmi']
    
    if sort_by not in valid_field:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_field}')
    
    if order not in ["asc","desc"]:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and decs')
    
    data = load_data()
    
    sort_order = True if order == "decs" else False
    sorted_data = sorted(data.values(), key=lambda x:x.get(sort_by,0), reverse=sort_order)
    
    return sorted_data
     