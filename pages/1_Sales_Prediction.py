import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# --------------------------
# Page Configuration
# --------------------------
st.set_page_config(
    page_title="Sales Prediction",
    page_icon="💊",
    layout="wide"
)

# --------------------------
# Load Model
# --------------------------
model = joblib.load("linear_model.pkl")

logo = Path("logo.png")

# --------------------------
# Sidebar
# --------------------------

if logo.exists():
    st.sidebar.image(str(logo), width=170)

st.sidebar.title("Mediserve Pharmacy")
st.sidebar.success("Healthcare • Trust • Care")

# --------------------------
# Header
# --------------------------

left, right = st.columns([1,4])

with left:
    if logo.exists():
        st.image(str(logo), width=120)

with right:
    st.title("💊 Monthly Sales Prediction")
    st.write("Predict pharmacy monthly sales using Machine Learning.")

st.divider()

# --------------------------
# Input Fields
# --------------------------

col1,col2=st.columns(2)

with col1:

    advertising=st.number_input(
        "Advertising Spend (£)",
        min_value=0.0,
        value=5000.0
    )

    foot=st.number_input(
        "Foot Traffic",
        min_value=0,
        value=300
    )

    prescriptions=st.number_input(
        "Number of Prescriptions",
        min_value=0,
        value=200
    )

    population=st.number_input(
        "Local Population",
        min_value=0,
        value=10000
    )

with col2:

    distance=st.number_input(
        "Distance to Competitor (km)",
        min_value=0.0,
        value=2.5
    )

    size=st.number_input(
        "Store Size (sqft)",
        min_value=0,
        value=1500
    )

    staff=st.number_input(
        "Staff Count",
        min_value=1,
        value=8
    )

st.divider()

# --------------------------
# Prediction
# --------------------------

if st.button("🚀 Predict Monthly Sales", use_container_width=True):

    X=pd.DataFrame({

        "Advertising_Spend":[advertising],
        "Foot_Traffic":[foot],
        "Num_Prescriptions":[prescriptions],
        "Local_Population":[population],
        "Distance_to_Competitor_km":[distance],
        "Store_Size_sqft":[size],
        "Staff_Count":[staff]

    })

    prediction=model.predict(X)[0]

    st.success("Prediction Successful")

    st.metric(
        "Predicted Monthly Sales",
        f"£{prediction:,.2f}"
    )

    st.subheader("Input Summary")

    st.dataframe(X,use_container_width=True)
