import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Digital Wellbeing Analyzer", layout="centered")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home - Tips", "Prediction", "What to Do"])

st.title("Digital Wellbeing Analyzer")

# Home Page with Digital Wellbeing Tips
if page == "Home - Tips":
    st.header(" Tips for Digital Wellbeing (With Resources)")
    st.markdown("""
### 1. Limit Screen Time  
Set app time limits and take regular screen breaks.  
**Source:** World Health Organization

### 2. Reduce Notifications  
Disable non-essential app notifications to reduce stress.  
**Source:** Harvard Business Review

### 3. Prioritize Sleep  
Avoid screens before bedtime and aim for 7–9 hours of sleep.  
**Source:** CDC

### 4. Use Focus Tools  
Pomodoro timers or app blockers help maintain concentration.  
**Source:** RescueTime

### 5. Monitor Mood & Anxiety  
Use mental health apps or journaling to track emotions.  
**Source:** National Alliance on Mental Illness (NAMI)

### 6. Social Media Detox  
Take regular breaks from social platforms.  
**Source:** Psychology Today
""")

# Prediction Page
elif page == "Prediction":
    st.header("Predict Your Digital Wellbeing Score")

    # Input fields
    sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, value=7.0)
    focus_score = st.slider("Focus Score (0 to 10)", 0.0, 10.0, 5.0)
    mood_score = st.slider("Mood Score (0 to 10)", 0.0, 10.0, 5.0)
    num_app_switches = st.number_input("Number of App Switches", min_value=0, max_value=1000, value=100)
    daily_screen_time_min = st.number_input("Daily Screen Time (minutes)", min_value=0, max_value=1440, value=300)
    social_media_time_min = st.number_input("Social Media Time (minutes)", min_value=0, max_value=1440, value=120)
    notification_count = st.number_input("Notification Count", min_value=0, max_value=1000, value=100)
    anxiety_level = st.slider("Anxiety Level (0 to 10)", 0.0, 10.0, 5.0)

    if st.button(" Predict Score"):
        input_data = np.array([[sleep_hours, focus_score, mood_score, num_app_switches,
                                daily_screen_time_min, social_media_time_min,
                                notification_count, anxiety_level]])
        prediction = model.predict(input_data)[0]
        st.success(f"Your predicted Digital Wellbeing Score is: **{prediction:.2f}**")

        # Store in session state for next page use
        st.session_state["latest_score"] = prediction

        # Interpretation based on descriptive statistics
        if prediction >= 65:
            st.info(" Excellent Digital Wellbeing")
        elif prediction >= 50:
            st.info(" Good Digital Wellbeing")
        elif prediction >= 40:
            st.warning(" Average - Some improvement needed")
        else:
            st.error(" Low - Digital wellbeing needs attention")

# What to Do if Score is Low
elif page == "What to Do":
    st.header(" What to Do If Your Score Is Low")

    score = st.session_state.get("latest_score", None)

    if score is not None:
        st.write(f"Your last predicted score: **{score:.2f}**")

        if score < 40:
            st.warning("Your digital wellbeing score is low. Here’s what you can do:")
            st.markdown("""
### Immediate Actions:
- Improve your **sleep schedule**
- Reduce **screen time**, especially before bed
- Take **social media breaks**
- Turn off **non-essential notifications**
- Try **breathing, journaling, or mindfulness apps**
- Seek help from a **mental health counselor**

Even small changes can lead to big improvements in digital wellbeing.
""")
        elif score < 50:
            st.info("You're in the average range. Try improving some habits like focus and screen time.")
        else:
            st.success("Your wellbeing looks good! Keep maintaining healthy digital habits.")
    else:
        st.info("You haven't made a prediction yet. Please go to the **Prediction** page.")
