📄 pydantic/README.md – (Add this in the pydantic folder)

# 🧠 Pydantic Model Demo in FastAPI

This folder demonstrates how to use **Pydantic**, the data validation and parsing library used internally by **FastAPI**.

📁 Folder: `pydantic`

---

## 📦 What Is Pydantic?

**Pydantic** allows you to define data models using Python type annotations. It ensures that any data coming into your system is:
- ✅ **Well-typed** (correct types like `str`, `int`, etc.)
- ✅ **Validated** (invalid data throws helpful errors)
- ✅ **Auto-parsed** (e.g., strings that can be converted to ints are auto-corrected)

---

## 🧪 Why Use Pydantic?

- To **validate incoming data** (like from JSON, requests, forms)
- To ensure **type safety** and avoid bugs from incorrect types
- To make your API **more robust and self-documented**
- Auto-generated docs in FastAPI come from these models

---

## 📁 Files in This Folder

- `main.py`: A basic example of using a Pydantic model to validate and insert patient data

---

## 🧠 How It Works

```python
from pydantic import BaseModel

# Step 1: Define a Patient Model
class Patient(BaseModel):
    name : str
    age : int

# Step 2: Accept Only Validated Data
def insert_patient (patient : Patient):
    print(patient.name)
    print(patient.age)
    print("Insert Data")

# Step 3: Example Input
patient_info = {"name":"Talha", "age":20}

# Automatically validates the data
patient_1 = Patient(**patient_info)
insert_patient(patient_1)
❌ Invalid Example (This Will Raise an Error)

patient_info = {"name":"Talha", "age":"thirty"}  # ❌ age must be int
▶️ How to Run
Install Pydantic (included with FastAPI, but for standalone use):


pip install pydantic
Run the file:


python main.py
✅ You’ll see output like:

Talha
20
Insert Data
❌ If you pass invalid data, Pydantic will raise a ValidationError.

📚 Learn More
Pydantic Docs

FastAPI + Pydantic Guide

