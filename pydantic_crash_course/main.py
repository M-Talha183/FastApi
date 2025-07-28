from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int 

def insert_patient (patient : Patient):
    print(patient.name)
    print(patient.age)
    print("Insert Data")
    
def insert_patient (patient : Patient):
    print(patient.name)
    print(patient.age)
    print("Insert Data")

    
patient_info = {"name":"Talha", "age":20}
# patient_info_2 = {"name":"Talha", "age":"thirty"} # Error 

patient_1 = Patient(**patient_info)
# patient_2 = Patient(**patient_info_2)
insert_patient(patient_1)
# insert_patient(patient_2)