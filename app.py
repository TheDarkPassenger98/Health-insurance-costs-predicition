import streamlit as st
import numpy as np
import pandas as pd
import joblib
scaler = joblib.load("scaler.pkl") 
le_diabetic = joblib.load("encoders\label_encoder_diabetic.pkl")
le_gender = joblib.load("encoders\label_encoder_gender.pkl")
le_smoker = joblib.load("encoders\label_encoder_smoker.pkl")
model = joblib.load("best_model.pkl")
st.set_page_config(page_title="Insurance Claim predictor", layout="centered")
st.title("Insurance health prediction app")
st.write("Enter the details to estimate your insurance payment amount")
with st.form("Input form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value = 0, max_value = 100, value = 30)
        bmi = st.number_input("Bmi", min_value = 10.0, max_value = 60.0, value = 25.0)
        children = st.number_input("Children", min_value=0, max_value=8, value = 0)
    with col2:
        bloodpressure = st.number_input("Bloodpressure", min_value=60, max_value=200, value = 120)
        gender = st.selectbox("Gender", options = le_gender.classes_)
        diabetic = st.selectbox("Diabetic", options = le_diabetic.classes_)
        smoker = st.selectbox("Smoker", options = le_smoker.classes_)
    
    submitted = st.form_submit_button("Predict payment")


if submitted:
    input_data = pd.DataFrame(
        {
            "age" : [age],
            "gender" : [gender],
            "bmi" : [bmi],
            "children" : [children],
            "bloodpressure" : [bloodpressure],
            "diabetic" : [diabetic],
            "children" : [children],
            "smoker" : [smoker],
        }
    )
    
    input_data["gender"] = le_gender.transform(input_data["gender"])
    input_data["diabetic"] = le_diabetic.transform(input_data["diabetic"])
    input_data["smoker"] = le_smoker.transform(input_data["smoker"])
    scaler_cols = list(scaler.feature_names_in_)
    for col in scaler_cols:
        if col not in input_data.columns:
            input_data[col] = 0  

    input_data[scaler_cols] = scaler.transform(input_data[scaler_cols])
    model_cols = model.get_booster().feature_names
    for col in model_cols:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[model_cols]
    prediction = model.predict(input_data)[0]
    st.success(f"### 💵Estimated Insurance Payment: **${prediction:,.2f}**")