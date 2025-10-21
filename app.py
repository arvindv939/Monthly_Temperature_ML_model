import streamlit as st
import numpy as np
import joblib

# Load the saved model
model = joblib.load('bangalore_temp_model.pkl')

# App title
st.title("🌧️ Bangalore Rainfall & Temperature Prediction")
st.write("This app predicts the average temperature based on weather data.")

# Input fields
tmin = st.number_input("Minimum Temperature (°C):", min_value=-10.0, max_value=50.0, value=20.0)
tmax = st.number_input("Maximum Temperature (°C):", min_value=-10.0, max_value=60.0, value=30.0)
prcp = st.number_input("Rainfall (mm):", min_value=0.0, max_value=500.0, value=10.0)
month = st.slider("Month:", 1, 12, 6)

# Predict button
if st.button("Predict Average Temperature"):
    # Prepare the input data
    input_data = np.array([[tmin, tmax, prcp, month]])
    prediction = model.predict(input_data)
    st.success(f"🌡️ Predicted Average Temperature: {prediction[0]:.2f} °C")