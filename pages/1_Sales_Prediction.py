import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Sales Prediction",
    page_icon="💊",
    layout="wide"
)

# -----------------------
# Load Model
# -----------------------
model = joblib.load("linear_model.pkl")

logo = Path("logo.png")

# -----------------------
# Sidebar
# -----------------------

if logo.exists():
    st.sidebar.image(str(logo), width=170)

st.sidebar.title("Mediserve Pharmacy")
st.sidebar.success("Healthcare • Trust • Care")

# -----------------------
# Header
# -----------------------

col1, col2 = st.columns([1,4])

with col1:
    if logo.exists():
        st.image(str(logo), width=120)

with col2:
    st.title("💊 Monthly Sales Prediction")
    st.write("Enter pharmacy information to predict monthly sales.")

st.divider()

# -----------------------
# Inputs
# -----------------------

c1, c2 = st.columns(2)

with c1:

    advertising = st.number_input(
        "Advertising Spend",
        value=5000.0
    )

    foot = st.number_input(
        "Foot Traffic",
        value=300
    )

    prescriptions = st.number_input(
        "Number of Prescriptions",
        value=200
    )

    population = st.number_input(
        "Local Population",
        value=10000
    )

with c2:

    competitor = st.number_input(
        "Distance to Competitor (km)",
        value=2.5
    )

    store = st.number_input(
        "Store Size (sqft)",
        value=1500
    )

    staff = st.number_input(
        "Staff Count",
        value=8
    )

st.divider()

# -----------------------
# Prediction
# -----------------------

if st.button("🚀 Predict Monthly Sales", use_container_width=True):

    X = pd.DataFrame({
        "Advertising_Spend":[advertising],
        "Foot_Traffic":[foot],
        "Num_Prescriptions":[prescriptions],
        "Local_Population":[population],
        "Distance_to_Competitor_km":[competitor],
        "Store_Size_sqft":[store],
        "Staff_Count":[staff]
    })

    try:

        prediction = model.predict(X)

        # Works with Series, ndarray or nested ndarray
        if hasattr(prediction, "flatten"):
            prediction = prediction.flatten()[0]
        else:
            prediction = prediction[0]

        prediction = float(prediction)

        st.success("Prediction Completed Successfully")

        st.metric(
            "Predicted Monthly Sales",
            f"${prediction:,.2f}"
        )

        st.subheader("Input Summary")
        st.dataframe(X, use_container_width=True)

    except Exception as e:

        st.error("Prediction Failed")
        st.exception(e)
