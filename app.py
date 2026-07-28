import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("linear_model.pkl")

st.set_page_config(page_title="Pharmacy Sales Prediction", page_icon="💊")

st.title("💊 Pharmacy Monthly Sales Prediction")

st.write("Enter the pharmacy information below.")

advertising = st.number_input("Advertising Spend", value=5000.0)
foot = st.number_input("Foot Traffic", value=300)
prescriptions = st.number_input("Number of Prescriptions", value=200)
population = st.number_input("Local Population", value=10000)
distance = st.number_input("Distance to Competitor (km)", value=2.5)
size = st.number_input("Store Size (sqft)", value=1500)
staff = st.number_input("Staff Count", value=8)

if st.button("Predict"):

    data = pd.DataFrame({
        "Advertising_Spend": [advertising],
        "Foot_Traffic": [foot],
        "Num_Prescriptions": [prescriptions],
        "Local_Population": [population],
        "Distance_to_Competitor_km": [distance],
        "Store_Size_sqft": [size],
        "Staff_Count": [staff]
    })

    prediction = model.predict(data)

    st.success(f"Predicted Monthly Sales: {prediction[0][0]:,.2f}")