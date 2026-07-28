import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Pharmacy Sales Prediction System",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

h1{
    color:#1565C0;
}

.stButton>button{
    width:100%;
    background:#1565C0;
    color:white;
    border-radius:10px;
    height:3em;
    font-size:18px;
    font-weight:bold;
}

.metric-box{
    background:white;
    padding:15px;
    border-radius:12px;
    text-align:center;
    box-shadow:0px 0px 8px rgba(0,0,0,.1);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("linear_model.pkl")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.image(
    "https://img.icons8.com/color/96/pharmacy-shop.png",
    width=100
)

st.sidebar.title("💊 Pharmacy Sales Predictor")

st.sidebar.info("""
This application predicts the expected monthly sales
of a pharmacy using a trained Multiple Linear Regression model.
""")

st.sidebar.success("Model: Multiple Linear Regression")

# -----------------------------
# Header
# -----------------------------
st.title("💊 Pharmacy Monthly Sales Prediction System")

st.write(
"""
Predict pharmacy monthly sales based on business factors.

Enter the pharmacy information below and click **Predict Sales**.
"""
)

st.divider()

# -----------------------------
# Input Form
# -----------------------------
left,right = st.columns(2)

with left:

    advertising = st.number_input(
        "📢 Advertising Spend",
        min_value=0.0,
        value=5000.0
    )

    foot = st.number_input(
        "🚶 Foot Traffic",
        min_value=0,
        value=300
    )

    prescriptions = st.number_input(
        "💊 Number of Prescriptions",
        min_value=0,
        value=200
    )

    population = st.number_input(
        "🏙 Local Population",
        min_value=0,
        value=10000
    )

with right:

    distance = st.number_input(
        "📍 Distance to Competitor (km)",
        min_value=0.0,
        value=2.5
    )

    size = st.number_input(
        "🏪 Store Size (sqft)",
        min_value=0,
        value=1500
    )

    staff = st.number_input(
        "👨‍⚕️ Staff Count",
        min_value=1,
        value=8
    )

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Monthly Sales"):

    data = pd.DataFrame({
        "Advertising_Spend":[advertising],
        "Foot_Traffic":[foot],
        "Num_Prescriptions":[prescriptions],
        "Local_Population":[population],
        "Distance_to_Competitor_km":[distance],
        "Store_Size_sqft":[size],
        "Staff_Count":[staff]
    })

    prediction = model.predict(data)[0][0]

    st.success("Prediction Completed Successfully!")

    c1,c2,c3 = st.columns(3)

    with c1:
        st.metric("Predicted Monthly Sales", f"£{prediction:,.2f}")

    with c2:
        st.metric("Algorithm","Linear Regression")

    with c3:
        st.metric("Features Used","7")

    st.divider()

    st.subheader("Input Summary")

    st.dataframe(data,use_container_width=True)

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
"""
Developed by Muhammad Aqeel

Machine Learning Project

Multiple Linear Regression | Python | Scikit-Learn | Streamlit
"""
)
