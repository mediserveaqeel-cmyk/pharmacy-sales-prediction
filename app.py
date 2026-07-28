import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Mediserve Pharmacy",
    page_icon="💊",
    layout="wide"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>

.stApp{
    background:#F5F7FA;
}

.main-title{
    font-size:42px;
    font-weight:bold;
    color:#1565C0;
}

.subtitle{
    font-size:20px;
    color:#2E7D32;
}

.card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0 4px 10px rgba(0,0,0,.15);
    text-align:center;
}

.footer{
    text-align:center;
    color:grey;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.image("logo.png", width=170)

st.sidebar.title("Mediserve Pharmacy")

st.sidebar.success("Healthcare • Trust • Care")

st.sidebar.divider()

st.sidebar.info("""
This application predicts monthly pharmacy sales using
Machine Learning.
""")

# ----------------------------
# Header
# ----------------------------

left,right = st.columns([1,4])

with left:
   st.image("logo.png", width=140)

with right:

    st.markdown(
        "<div class='main-title'>MEDISERVE PHARMACY</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Healthcare • Trust • Care</div>",
        unsafe_allow_html=True
    )

st.divider()

st.markdown("# 💊 AI Powered Pharmacy Sales Prediction System")

st.write("""
Welcome to the Mediserve Pharmacy Sales Prediction Dashboard.

This system uses **Multiple Linear Regression** to estimate monthly pharmacy sales based on business-related factors.
""")

st.divider()

# ----------------------------
# KPI Cards
# ----------------------------

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Algorithm","Linear Regression")

with c2:
    st.metric("Features","7")

with c3:
    st.metric("Status","Ready")

with c4:
    st.metric("Version","1.0")

st.divider()

st.subheader("🚀 What can this application do?")

st.markdown("""
- 💊 Predict Monthly Pharmacy Sales

- 📊 Display Model Analytics

- 📈 Show Prediction Results

- 📁 Upload CSV Files (Coming Soon)

- 📥 Download Prediction Reports (Coming Soon)
""")

st.divider()

st.success("Use the left sidebar to open the Sales Prediction page.")

st.markdown(
"""
<div class='footer'>

© 2026 Mediserve Pharmacy

Developed by Muhammad Aqeel

</div>
""",
unsafe_allow_html=True
)
