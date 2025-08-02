# from fastapi import FastAPI 
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel , Field , computed_field
# from typing import Literal , Annotated
# import pandas as pd 
# import pickle



# tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
# tier_2_cities = [
#     "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
#     "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
#     "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
#     "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
#     "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
#     "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
# ]


# # import our model 
# with open("model.pkl" , "rb") as f:
#     model = pickle.load(f) 

# #  crreate the object of fastapi 
 
# app = FastAPI()

# #  create pydantic model to validate the user input 

# class UserInput (BaseModel):
    
#     age : Annotated[int, Field(..., gt=0,lt=120 , description="Name of the user ")]
#     weight : Annotated[float , Field(..., gt=0 , description="Weight of the user ")]
#     height : Annotated[float , Field(..., gt=0 , description="height of the user ")]
#     income_lpa : Annotated[float , Field(..., gt=0 , description="Annual salary of the usser in LPA ")]
#     smoker :  Annotated[bool , Field(..., description="Is user is a smoker")]
#     city : Annotated[str , Field(..., description="The city User Belong To ")]
#     occupation :  Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
#        'business_owner', 'unemployed', 'private_job'] , Field(..., description="Occupation of the user ")]
    
#     @computed_field
#     @property
#     def bmi (self) ->float:
#         return self.weight / (self.height **2)
    
#     @computed_field
#     @property
#     def life_risk(self) -> str :
#         if self.smoker and self.bmi > 30:
#             return "high"
#         elif self.smoker or self.bmi > 27:
#             return "medium"
#         else:
#             return "low"

#     @computed_field
#     @property
#     def age_group(self) -> str:
#         if self.age < 25:
#             return "young"
#         elif self.age < 45:
#             return "adult"
#         elif self.age < 60:
#             return "middle_aged"
#         return "senior"
    
#     @computed_field
#     @property
#     def city_tier(self) -> int:
#         if self.city in tier_1_cities:
#             return 1
#         elif self.city in tier_2_cities:
#             return 2
#         else:
#             return 3

# @app.post('/predict')
# def predict_premium (data : UserInput):
    
#     input_df = pd.DataFrame([{
#         "bmi" : data.bmi,
#         "age_group":data.age_group,
#         "life_style_risk" : data.life_risk,
#         "city_tier": data.city_tier,
#         "income_lpa": data.income_lpa,
#         "occupation": data.occupation
#     }])
    
#     prediction = model.predict(input_df)[0]
    
#     return JSONResponse(status_code=200 , content={"predicted_catagory": prediction})
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pandas as pd
import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

app = FastAPI()

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120)]
    weight: Annotated[float, Field(..., gt=0)]
    height: Annotated[float, Field(..., gt=0)]
    income_lpa: Annotated[float, Field(..., gt=0)]
    smoker: Annotated[bool, Field(...)]
    city: Annotated[str, Field(...)]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
                                   'business_owner', 'unemployed', 'private_job'], Field(...)]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)

    @computed_field
    @property
    def life_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3

@app.post("/predict")
def predict_premium(data: UserInput):
    input_df = pd.DataFrame([{
        "bmi": data.bmi,
        "age_group": data.age_group,
    "lifestyle_risk": data.life_risk,  # ✅ fixed spelling
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }])

    predicted_category = model.predict(input_df)[0]

    try:
        proba = model.predict_proba(input_df)[0]
        class_probs = {
            str(cls): float(prob) for cls, prob in zip(model.classes_, proba)
        }
        confidence = max(proba)
    except:
        class_probs = {"unknown": 1.0}
        confidence = 1.0

    return JSONResponse(status_code=200, content={
        "response": {
            "predicted_category": predicted_category,
            "confidence": round(confidence, 4),
            "class_probabilities": class_probs
        }
    })
