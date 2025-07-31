# 🏥 Patient Management System API - FastAPI

A fully functional REST API built using [FastAPI](https://fastapi.tiangolo.com/) that allows you to manage, create, update, delete, and view patient records stored in a local JSON file (`patients.json`). It uses **Pydantic** models for input validation, including dynamic computed fields like **BMI** and **health verdict**.

---

## 🚀 Features

- ✅ View all patient records
- ✅ Retrieve specific patient data by ID
- ✅ Create new patients (with full validation)
- ✅ Update existing patient info
- ✅ Delete patient records
- ✅ Sort patients by height, weight, or BMI
- ✅ Uses Pydantic's `BaseModel`, validators, `computed_field`
- ✅ Lightweight, fast, and runs locally with zero dependencies

---

## 📁 Project Structure

day_2/
├── patients.json # JSON data file storing patient records
├── main.py # FastAPI application
└── README.md # Project documentation (this file)



---

## 🧪 Requirements

Make sure you have **Python 3.7+** installed.

Install required packages:

```bash
pip install fastapi uvicorn
▶️ How to Run the API
Step-by-Step:
bash
Copy
Edit
# Clone the repository
git clone https://github.com/M-Talha183/FastApi.git
cd FastApi/day_2

# Run the FastAPI server using Uvicorn
uvicorn main:app --reload
Open in Browser:
API Root: http://127.0.0.1:8000

Swagger Docs: http://127.0.0.1:8000/docs

📌 API Endpoints
Method	Endpoint	Description
GET	/	Welcome message
GET	/about	About this API
GET	/view	View all patient records
GET	/patient/{patient_id}	View a specific patient by ID
GET	/sort	Sort by height, weight, or bmi
POST	/create	Create a new patient
PUT	/edit/{patient_id}	Update an existing patient's data
DELETE	/delete/{patient_id}	Delete a patient from the database

🧠 Pydantic Model Details
Patient Model

class Patient(BaseModel):
    id: str
    name: str
    city: str
    age: int
    gender: Literal['male', 'female', 'other']
    height: float  # meters
    weight: float  # kilograms

    @computed_field
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    def verdict(self) -> str:
        # Returns health status based on BMI
PatientUpdate Model
Used for partial updates (PUT):


class PatientUpdate(BaseModel):
    name: Optional[str]
    city: Optional[str]
    age: Optional[int]
    gender: Optional[Literal['male', 'female', 'other']]
    height: Optional[float]
    weight: Optional[float]
✅ Example JSON Input for /create

{
  "id": "P001",
  "name": "Ali Khan",
  "city": "Lahore",
  "age": 28,
  "gender": "male",
  "height": 1.75,
  "weight": 70
}
🧠 Response Will Include

{
  "bmi": 22.86,
  "verdict": "Normal"
}
🔍 Sorting Example
Request:

GET /sort?sort_by=bmi&order=asc
Query Parameters:

sort_by: Must be one of height, weight, bmi

order: asc or desc

❌ Error Handling
400 Bad Request for invalid inputs or duplicate patients

404 Not Found for missing records

Clear messages using HTTPException

🧑‍💻 Author
Muhammad Talha
GitHub: @M-Talha183
