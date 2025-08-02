.
🤖 Insurance Premium Predictor API with FastAPI & Streamlit
A machine learning-powered API built with FastAPI that predicts the insurance premium category of users based on their health, city, income, and lifestyle data. This project includes a Streamlit frontend for user interaction and a trained classification model served using an API endpoint.


📦 Project Structure

fastapi_ML_project/
├── model.pkl           # Trained ML model (classification)
├── main.py             # FastAPI backend server
├── frontend.py         # Streamlit frontend interface
└── README.md           # Project documentation



🚀 Features
🏥 Predict insurance premium category (Low, Medium, High)

🔬 Uses BMI, age group, lifestyle risk, city tier, income & occupation

🌐 FastAPI for building the backend REST API

🎛️ Streamlit for an interactive frontend

📊 Returns prediction, confidence score, and class probabilities

⚙️ Requirements
Ensure Python 3.7+ is installed.

Install dependencies:

pip install fastapi uvicorn pydantic scikit-learn pandas streamlit
▶️ How to Run
1. Start FastAPI Backend
Make sure the trained model (model.pkl) is in the same directory.

uvicorn main:app --reload
📍 Visit API docs at: http://127.0.0.1:8000/docs

2. Start Streamlit Frontend
In a separate terminal, run:

streamlit run frontend.py
📍 Interface available at: http://localhost:8501

📥 Example Input (via API or UI)

{
  "age": 35,
  "weight": 70.0,
  "height": 1.75,
  "income_lpa": 12.5,
  "smoker": true,
  "city": "Mumbai",
  "occupation": "private_job"
}
🧠 Behind the Scenes
BMI: Computed from weight and height

Life Risk:

high: if smoker and BMI > 30

medium: if smoker or BMI > 27

low: otherwise

Age Group: young, adult, middle_aged, senior

City Tier:

Tier 1: Metro cities

Tier 2: Growing cities

Tier 3: All others

🔁 API Endpoint
POST /predict

Field	Type	Description
age	int	Age of the user (1–119)
weight	float	Weight in kg (> 0)
height	float	Height in meters (> 0)
income_lpa	float	Annual income in LPA (> 0)
smoker	bool	Whether the user is a smoker
city	string	City of residence
occupation	string	Occupation (student, private_job, etc.)

Example Response:

{
  "response": {
    "predicted_category": "high",
    "confidence": 0.88,
    "class_probabilities": {
      "low": 0.02,
      "medium": 0.10,
      "high": 0.88
    }
  }
}
🎯 Use Cases
Insurance company portals

Health risk profiling

Data science education/demo project

📚 Future Improvements
Add authentication

Use real-time database instead of a static model

Expand to regression for premium cost prediction

Add logging and model versioning

🛠️ Tech Stack
FastAPI – for RESTful API

Streamlit – for interactive frontend

Scikit-learn – model training & prediction

Pandas – data manipulation

Pydantic – input validation

🙌 Acknowledgements
Built as part of a hands-on ML and API integration project using FastAPI and Streamlit. Inspired by real-world insurance and health analytics.

