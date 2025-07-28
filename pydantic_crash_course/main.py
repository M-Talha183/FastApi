from pydantic import BaseModel , EmailStr , Field
from typing import List , Dict ,Optional
class Patient(BaseModel):
    name : str = Field(max_length=50)
    age : int = Field(gt=0, lt=120)
    # email : EmailStr
    weight : float = Field(gt=0)
    married : bool
    allergies : Optional[List[str]] = None
    contact_details : Dict[str,str]

def insert_patient (patient : Patient):
    print(patient.name)
    print(patient.age)
    print("Insert Data")
    
def insert_patient (patient : Patient):
    print(patient.name)
    print(patient.age)
    print("Insert Data")

    
patient_info = {"name":"Talha", "age":20 , "weight": 75.5 , "married": True , "allergies":["pollen","Dust"] , "contact_details":{"email":"abs@gmail.com","phone":"0123456789"}}
# patient_info_2 = {"name":"Talha", "age":"thirty"} # Error 

patient_1 = Patient(**patient_info)
# patient_2 = Patient(**patient_info_2)
insert_patient(patient_1)
# insert_patient(patient_2)

