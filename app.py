import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and data
model = pickle.load(open('RidgeModel.pkl', 'rb'))
data = pd.read_csv("Cleaned_data.csv")

# Page config
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

# App Header
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🏠 House Price Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #d1d1d1;'>", unsafe_allow_html=True)

st.markdown("""
<style>
    .stSelectbox > div > div {
        font-size: 16px;
    }
    .stNumberInput input {
        font-size: 16px;
    }
    .stButton button {
        background-color: #2980B9;
        color: white;
        font-size: 16px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Input form
with st.form("prediction_form"):
    st.subheader("📋 Enter Property Details")

    col1, col2 = st.columns(2)

    with col1:
        bhk = st.selectbox("Select BHK 🛏️", sorted(data['bhk'].unique()))
        bath = st.selectbox("Select Number of Bathrooms 🚿", sorted(data['bath'].unique()))
    with col2:
        sqft = st.number_input("Enter Total Square Footage 📐", step=100, min_value=500, max_value=10000)
        locations = sorted(data['location'].unique())
        location = st.selectbox("Select Location 📍", locations)

    submitted = st.form_submit_button("Predict Price 💰")

if submitted:
    # Prepare input data
    input_df = pd.DataFrame([{
        'total_sqft': sqft,
        'bath': bath,
        'bhk': bhk,
        'location': location
    }])

    # Make prediction
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"🏷️ Estimated House Price: ₹ **{round(prediction, 2)} Lakhs**")
    except Exception as e:
        st.error("Something went wrong during prediction.")
        st.exception(e)

# Footer
st.markdown("<hr style='border: 0.5px solid #d1d1d1;'>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)

