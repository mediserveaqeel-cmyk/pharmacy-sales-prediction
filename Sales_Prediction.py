import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Sales Prediction",
    page_icon="💊",
    layout="wide"
)

# -------------------------
# Load Model
# -------------------------
model = joblib.load("linear_model.pkl")

logo = Path("logo.png")

# -------------------------
# Sidebar
# -------------------------

if logo.exists():
    st.sidebar.image(str(logo), width=150)

st.sidebar.title("Sales Prediction")

# -------------------------
# Header
# -------------------------

left,right = st.columns([1,4])

with left:
    if logo.exists():
        st.image(str(logo), width=120)

with right:
    st.title("💊 Monthly Sales Prediction")
    st.write("Enter the pharmacy information below.")

st.divider()

# -------------------------
# Input Form
# -------------------------

col1,col2 = st.columns(2)

with col1:

    advertising = st.number_input(
        "Advertising Spend",
        value=5000.0
    )

    foot = st.number_input(
        "Foot Traffic",
        value=300
    )

    prescriptions = st.number_input(
        "Prescriptions",
        value=200
    )

    population = st.number_input(
        "Population",
        value=10000
    )

with col2:

    distance = st.number_input(
        "Distance to Competitor",
        value=2.5
    )

    size = st.number_input(
        "Store Size",
        value=1500
    )

    staff = st.number_input(
        "Staff Count",
        value=8
    )

st.divider()

# -------------------------
# Predict Button
# -------------------------

if st.button("Predict Monthly Sales", use_container_width=True):

    X = pd.DataFrame({

        "Advertising_Spend":[advertising],
        "Foot_Traffic":[foot],
        "Num_Prescriptions":[prescriptions],
        "Local_Population":[population],
        "Distance_to_Competitor_km":[distance],
        "Store_Size_sqft":[size],
        "Staff_Count":[staff]

    })

    prediction = model.predict(X)[0][0]

    st.success("Prediction Successful")

    st.metric(
        "Predicted Monthly Sales",
        f"£{prediction:,.2f}"
    )

    st.subheader("Input Summary")

    st.dataframe(X, use_container_width=True)
