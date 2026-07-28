import streamlit as st
from pathlib import Path

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Mediserve Pharmacy",
    page_icon="💊",
    layout="wide"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------
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
    font-size:22px;
    color:#2E7D32;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Logo
# --------------------------------------------------

logo = Path("logo.png")

# Sidebar Logo
if logo.exists():
    st.sidebar.image(str(logo), width=180)
else:
    st.sidebar.warning("Logo not found.")

st.sidebar.title("Mediserve Pharmacy")
st.sidebar.success("Healthcare • Trust • Care")

st.sidebar.divider()

st.sidebar.info(
    """
This application predicts monthly pharmacy sales using
Machine Learning.
"""
)

# --------------------------------------------------
# Header
# --------------------------------------------------

left, right = st.columns([1,4])

with left:
    if logo.exists():
        st.image(str(logo), width=150)

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

# --------------------------------------------------
# Welcome
# --------------------------------------------------

st.header("💊 AI Powered Pharmacy Sales Prediction System")

st.write("""
Welcome to the **Mediserve Pharmacy Dashboard**.

This system uses **Multiple Linear Regression**
to estimate pharmacy monthly sales using business data.
""")

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

c1,c2,c3,c4 = st.columns(4)

c1.metric("Algorithm","Linear Regression")
c2.metric("Features","7")
c3.metric("Status","Ready")
c4.metric("Version","1.0")

st.divider()

st.subheader("Application Features")

st.markdown("""
✅ Monthly Sales Prediction

✅ Machine Learning Model

✅ Business Analytics

🚧 CSV Upload (Coming Soon)

🚧 Download Prediction Report (Coming Soon)
""")

st.divider()

st.success("👈 Open **Sales Prediction** from the left sidebar.")

st.markdown(
"""
<div class='footer'>

© 2026 Mediserve Pharmacy

Healthcare • Trust • Care

Developed by Muhammad Aqeel

</div>
""",
unsafe_allow_html=True
)
