from fastapi import FastAPI , Path ,HTTPException , Query 
import json
from pydantic import BaseModel , Field , computed_field
from typing import Annotated , Literal ,Optional
from fastapi.responses import JSONResponse


app = FastAPI()

class Patient(BaseModel):
    
    id : Annotated[str , Field(...,description="ID of the patient ", examples=["P001"])]
    name : Annotated[str , Field(...,description="Name of the patient  ")]
    city : Annotated[str , Field(...,description="City Where the patient is living ", )]
    age : Annotated[int , Field(...,gt=0,lt=120,description="ID of the patient ", examples=["P001"])]
    gender : Annotated[Literal['male','female','other'], Field(...,description="Gender of the patient ")]
    height : Annotated[float,Field(...,gt=0,description="Height of the patient in mts ")]
    weight : Annotated[float,Field(...,gt=0,description="Weight of the patient in kgs ")]
    
    @computed_field
    @property
    def bmi (self) ->float :
        bmi = round(self.weight / (self.height**2),2)
        return bmi 
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Normal"
        else :
            return  "Obese"
    
    
class PatientUpdate (BaseModel):


    name : Annotated[Optional[str] , Field(default=None)]
    city : Annotated[Optional[str] , Field(default=None)]
    age : Annotated[Optional[int] , Field(default=None, gt=0)]
    gender : Annotated[Optional[Literal['male','female','other']], Field(default=None)]
    height : Annotated[Optional[float],Field(default=None)]
    weight : Annotated[Optional[float],Field(default=None)]
     
    
    


def load_data():
    with open("patients.json", "r") as f:
        data  = json.load(f)
        
    return data  

def save_data(data):
    with open('patients.json',"w") as f:
        json.dump(data,f)
        
        

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
     

@app.post("/create")
def create_patient(patient:Patient):
    #  Load Existing Data 
    data = load_data()
    #  Check if the existing data alredy exist or not 
    
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already Exist ")
    
    # new patient add to the database 
    
    data[patient.id] = patient.model_dump(exclude=['id'])
    #  save into the json 
    save_data(data)
    
    return JSONResponse(status_code=201, content={'message':'Patient Create Successfully '})


@app.put('/edit/{patient_id}')
def update_patient(patient_id: str , patient_update : PatientUpdate):
    
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient Not found ")
    
    existing_patient_info =data[patient_id] 
    
    updated_patient_info = patient_update.model_dump(exclude_unset=True)
    
    for key , value in updated_patient_info.items():
        existing_patient_info [key] = value
        
    existing_patient_info ['id'] = patient_id
    patient_pydantic_object = Patient(**existing_patient_info)
    
    existing_patient_info =patient_pydantic_object.model_dump(exclude='id')
    
    data[patient_id] = existing_patient_info
    
    save_data(data)
    
    return JSONResponse(status_code=200, content={'message':'patient Updated '})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # load data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient deleted'})


