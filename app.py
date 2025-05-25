import streamlit as st
import numpy as np
import pickle

# Load the saved model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# App title
st.title("🧠 Digital Wellbeing Score Predictor")
st.markdown("Enter your digital behavior data to predict your wellbeing score.")

# Input fields
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, value=7.0)
focus_score = st.slider("Focus Score (0 to 10)", 0.0, 10.0, 5.0)
mood_score = st.slider("Mood Score (0 to 10)", 0.0, 10.0, 5.0)
num_app_switches = st.number_input("Number of App Switches", min_value=0, max_value=1000, value=100)
daily_screen_time_min = st.number_input("Daily Screen Time (minutes)", min_value=0, max_value=1440, value=300)
social_media_time_min = st.number_input("Social Media Time (minutes)", min_value=0, max_value=1440, value=120)
notification_count = st.number_input("Notification Count", min_value=0, max_value=1000, value=100)
anxiety_level = st.slider("Anxiety Level (0 to 10)", 0.0, 10.0, 5.0)

# Predict button
if st.button("Predict"):
    # Create input array
    input_data = np.array([[sleep_hours, focus_score, mood_score, num_app_switches,
                            daily_screen_time_min, social_media_time_min,
                            notification_count, anxiety_level]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Show result
    st.success(f"📊 Predicted Digital Wellbeing Score: **{prediction:.2f}**")
