# 🛌 Time to Fall Asleep Predictor

## 📌 Project Overview

The **Time to Fall Asleep Predictor** is a Machine Learning project that estimates how long it will take a person to fall asleep based on their daily habits.

The model uses inputs such as:

* Screen time before bed
* Caffeine intake
* Stress level
* Room lighting

It then predicts the **time (in minutes)** required to fall asleep.

---

## 🚀 Features

* Simple and interactive web interface using Streamlit
* Machine Learning model trained using Linear Regression
* Real-time prediction based on user input
* Easy to extend with more features and data

---

## 🧠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 📁 Project Structure

sleep_predictor/
│
├── data/
│   └── sleep_data.csv          # Dataset
│
├── model/
│   ├── train_model.py          # Model training script
│   └── model.pkl              # Saved ML model
│
├── app/
│   └── app.py                 # Streamlit web app
│
├── requirements.txt           # Dependencies
└── README.txt                 # Project documentation

---

## ⚙️ Installation & Setup

### Step 1: Clone or Download Project

Download the project folder and open it in VS Code.

---

### Step 2: Install Dependencies

Open terminal and run:

pip install -r requirements.txt

---

### Step 3: Train the Model

Navigate to model folder:

cd model
python train_model.py

This will generate the trained model file:
model.pkl

---

### Step 4: Run the Application

Navigate to app folder:

cd ../app
streamlit run app.py

---

## 📊 Input Parameters

| Parameter     | Description                        |
| ------------- | ---------------------------------- |
| Screen Time   | Minutes of screen usage before bed |
| Caffeine      | Number of cups consumed            |
| Stress Level  | Scale from 1 to 10                 |
| Room Lighting | Scale from 1 to 10                 |

---

## 🎯 Output

* Predicted time (in minutes) required to fall asleep

---

## ⚠️ Note

This project uses a **sample dataset** and is intended for:

* Educational purposes
* Portfolio projects
* Beginner ML practice

It is **not a medical prediction tool**.

---

## 🔥 Future Improvements

* Add larger and real-world dataset
* Use advanced ML models (Random Forest, XGBoost)
* Add sleep quality prediction
* Store user history
* Deploy as a web or mobile application

---

## 👨‍💻 Author

Developed as a Machine Learning mini project.

---

## ⭐ Acknowledgment

This project is built for learning and demonstrating basic ML workflow:
Data → Training → Prediction → Deployment
This project is built for learning and demonstrating basic ML workflow:
Data → Training → Prediction → Deployment
