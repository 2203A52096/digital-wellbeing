import streamlit as st
import numpy as np
import pickle

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Digital Wellbeing App", layout="centered")

st.title("Digital Wellbeing Analyzer")

# Tabs for navigation
tab1, tab2, tab3 = st.tabs(["Home", "Prediction", "What to Do"])

# 1. Home Tab – Tips on Digital Wellbeing
with tab1:
    st.header("Tips for Improving Digital Wellbeing")
    st.markdown("""
    ### 1. Limit Screen Time  
    Avoid excessive screen exposure. Try the 20-20-20 rule: every 20 minutes, look 20 feet away for 20 seconds.

    ### 2. Reduce Notifications  
    Disable non-essential app notifications to minimize distractions.

    ### 3. Prioritize Sleep  
    Aim for 7–9 hours of sleep. Avoid using screens at least 30 minutes before bedtime.

    ### 4. Use Focus Tools  
    Use tools like Pomodoro timers or website blockers to improve focus and reduce multitasking.

    ### 5. Monitor Mood and Anxiety  
    Reflect daily. Use mental wellness apps or journaling.

    ### 6. Take Social Media Breaks  
    Set app limits or schedule “no social media” hours or weekends.
    """)

# 2. Prediction Tab – Input form and prediction
with tab2:
    st.header("Predict Your Digital Wellbeing Score")

    sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, value=7.0)
    focus_score = st.slider("Focus Score (0 to 10)", 0.0, 10.0, 5.0)
    mood_score = st.slider("Mood Score (0 to 10)", 0.0, 10.0, 5.0)
    num_app_switches = st.number_input("Number of App Switches", min_value=0, max_value=1000, value=100)
    daily_screen_time_min = st.number_input("Daily Screen Time (minutes)", min_value=0, max_value=1440, value=300)
    social_media_time_min = st.number_input("Social Media Time (minutes)", min_value=0, max_value=1440, value=120)
    notification_count = st.number_input("Notification Count", min_value=0, max_value=1000, value=100)
    anxiety_level = st.slider("Anxiety Level (0 to 10)", 0.0, 10.0, 5.0)

    if st.button("Predict Score"):
        input_data = np.array([[sleep_hours, focus_score, mood_score, num_app_switches,
                                daily_screen_time_min, social_media_time_min,
                                notification_count, anxiety_level]])
        prediction = model.predict(input_data)[0]
        st.subheader("Predicted Digital Wellbeing Score:")
        st.success(f"{prediction:.2f}")
        st.session_state["latest_score"] = prediction

# 3. What to Do Tab – Recommendations based on score
with tab3:
    st.header("What to Do if Your Digital Wellbeing is Low")

    score = st.session_state.get("latest_score", None)

    if score is not None:
        st.write(f"Your last predicted score: **{score:.2f}**")
        if score < 5:
            st.warning("Your digital wellbeing score seems low. Consider these steps:")
            st.markdown("""
            ### Actions to Take:
            - **Improve Sleep Quality:** Maintain consistent sleep routines and limit screens before bed.
            - **Manage Anxiety:** Try relaxation techniques, therapy, or meditation apps.
            - **Limit Screen Time:** Use screen time apps to track and reduce excessive usage.
            - **Reduce App Switching:** Focus on one task at a time.
            - **Control Notifications:** Turn off unnecessary alerts to stay calm and focused.
            - **Seek Help:** Don’t hesitate to talk to a mental health professional.
            """)
        else:
            st.success("Your digital wellbeing score looks healthy! Keep following good habits.")
    else:
        st.info("No prediction made yet. Visit the Prediction tab to get started.")
