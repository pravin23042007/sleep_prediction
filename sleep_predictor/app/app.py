import streamlit as st
import pickle
import numpy as np

# Loading the model
model = pickle.load(open('../model/model.pkl', 'rb'))

st.title("🛌 Time to Fall Asleep Predictor")

st.write("Enter your daily habits:")

# Inputs
screen_time = st.slider("Screen Time Before Bed (minutes)", 0, 300, 60)
caffeine = st.slider("Caffeine Intake (cups)", 0, 5, 1)
stress = st.slider("Stress Level (1-10)", 1, 10, 5)
lighting = st.slider("Room Lighting (1-10)", 1, 10, 5)

# Predict
if st.button("Predict"):
    input_data = np.array([[screen_time, caffeine, stress, lighting]])
    prediction = model.predict(input_data)[0]

    st.success(f"😴 Estimated Time to Fall Asleep: {round(prediction, 2)} minutes")