# 🏥 Patient Management System API - FastAPI

A simple yet functional REST API built using [FastAPI](https://fastapi.tiangolo.com/) that allows you to manage and view patient records from a local JSON file (`patients.json`).

---

## 🚀 Features

- View all patient records
- Retrieve specific patient data by ID
- Lightweight, fast, and easy to run locally

---

## 📁 Project Structure

├── patients.json # Data source (sample patient data in JSON format)
├── main.py # Main FastAPI app
└── README.md # Project documentation 


---

## 🧪 Requirements

Make sure you have Python 3.7 or above installed.

Install required packages:

```bash
pip install fastapi uvicorn

▶️ How to Run the API
Clone the Repository

git clone https://github.com/M-Talha183/FastApi.git
cd FastApi/day_2

Run the FastAPI app using Uvicorn

uv run uvicorn main:app --reload

Open in Browser

API Root: http://127.0.0.1:8000

Swagger Docs: http://127.0.0.1:8000/docs

| Method | Endpoint                | Description                   |
| ------ | ----------------------- | ----------------------------- |
| GET    | `/`                     | Welcome message               |
| GET    | `/about`                | About the API                 |
| GET    | `/view`                 | View all patient records      |
| GET    | `/patient/{patient_id}` | View a specific patient by ID |

