import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load('parking_model.pkl')  # Your saved model

st.title("Smart Parking Slot Prediction 🚗")

# --- User Inputs ---
st.sidebar.header("Input Parking Slot Data")
hour = st.sidebar.slider("Hour of Day", 0, 23, 12)
day_of_week = st.sidebar.selectbox("Day of Week", list(range(7)))
is_weekend = 1 if day_of_week >=5 else 0
sensor_proximity = st.sidebar.number_input("Sensor Proximity", 0.0, 20.0, 5.0)
sensor_pressure = st.sidebar.number_input("Sensor Pressure", 0.0, 20.0, 2.0)
vehicle_weight = st.sidebar.number_input("Vehicle Weight", 500, 5000, 1500)
vehicle_height = st.sidebar.number_input("Vehicle Height", 1.0, 10.0, 4.0)
weather_temp = st.sidebar.number_input("Weather Temperature", -10.0, 50.0, 25.0)
weather_precip = st.sidebar.number_input("Weather Precipitation", 0, 10, 0)
prev_occupancy = st.sidebar.selectbox("Previous Occupancy", [0,1])

# --- One-hot encoded features (default 0) ---
user_type_staff = 0
user_type_visitor = 0
vehicle_type_electric = 0
vehicle_type_motorcycle = 0
traffic_low = 0
traffic_medium = 0

# --- Prepare input DataFrame ---
input_data = pd.DataFrame({
    'hour':[hour],
    'day_of_week':[day_of_week],
    'is_weekend':[is_weekend],
    'Sensor_Reading_Proximity':[sensor_proximity],
    'Sensor_Reading_Pressure':[sensor_pressure],
    'Vehicle_Type_Weight':[vehicle_weight],
    'Vehicle_Type_Height':[vehicle_height],
    'Weather_Temperature':[weather_temp],
    'Weather_Precipitation':[weather_precip],
    'prev_occupancy':[prev_occupancy],
    'User_Type_Staff':[user_type_staff],
    'User_Type_Visitor':[user_type_visitor],
    'Vehicle_Type_Electric Vehicle':[vehicle_type_electric],
    'Vehicle_Type_Motorcycle':[vehicle_type_motorcycle],
    'Nearby_Traffic_Level_Low':[traffic_low],
    'Nearby_Traffic_Level_Medium':[traffic_medium]
})

# --- Prediction ---
if st.button("Predict Parking Slot Availability"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("Parking Slot is **Occupied**")
    else:
        st.success("Parking Slot is **Free**")
