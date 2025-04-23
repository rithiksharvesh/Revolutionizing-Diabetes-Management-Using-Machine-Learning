# app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open('diet_model.pkl', 'rb'))

# UI Title
st.title("🍽️ Diabetes Diet Recommendation System")

# Input fields
age = st.slider("Age", 10, 100, 30)
weight = st.number_input("Weight (kg)", 30, 200, 70)
height = st.number_input("Height (cm)", 100, 220, 170)
glucose = st.slider("Glucose Level (mg/dL)", 50, 300, 110)
insulin = st.slider("Insulin Usage (units)", 0, 100, 10)
bmi = weight / ((height / 100) ** 2)

# Create input data
input_data = pd.DataFrame([[age, weight, height, glucose, insulin, bmi]],
                          columns=["Age", "Weight", "Height", "Glucose", "Insulin", "BMI"])

if st.button("Get Diet Recommendation"):
    prediction = model.predict(input_data)[0]
    st.success(f"Recommended Diet: {prediction}")
