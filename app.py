import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model and data columns
model = pickle.load(open('RidgeModel.pkl', 'rb'))
data = pd.read_csv("Cleaned_data.csv")

st.title("🏠 House Price Prediction App")

# Input fields
bhk = st.selectbox("Select BHK", sorted(data['bhk'].unique()))
bath = st.selectbox("Select Number of Bathrooms", sorted(data['bath'].unique()))
sqft = st.number_input("Enter Total Square Footage", step=100, min_value=500, max_value=10000)

# Location input
locations = sorted(data['location'].unique())
location = st.selectbox("Select Location", locations)

# Predict button
if st.button("Predict Price"):
    # Create input vector for the model
    loc_ohe = [0] * len(locations)
    if location in locations:
        loc_ohe[locations.index(location)] = 1

    x = np.array([sqft, bath, bhk] + loc_ohe).reshape(1, -1)
    prediction = model.predict(x)[0]

    st.success(f"Estimated House Price: ₹ {round(prediction, 2)} Lakhs")
