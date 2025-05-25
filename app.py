import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Digital Wellbeing Analyzer", page_icon="🧘‍♂️")

# Custom CSS for styling
st.markdown("""
    <style>
    /* Main title styling */
    .title {
        font-size: 3rem;
        font-weight: 700;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 1rem;
    }
    /* Sidebar background */
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    /* Tips card with darker, neutral background for light/dark mode */
    .tip-card {
        background: #3a3f44;  /* Dark gray - good for dark mode */
        color: #e1e4e8;       /* Light gray text */
        border-radius: 10px;
        padding: 15px 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease;
    }
    .tip-card h3 {
        color: #f5f6f7; /* Slightly brighter heading */
    }
    /* Light mode overrides */
    @media (prefers-color-scheme: light) {
        .tip-card {
            background: #dcdde1;
            color: #2f3640;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .tip-card h3 {
            color: #273c75;
        }
    }
    /* Colored headers for score interpretations */
    .excellent { color: #27ae60; font-weight: 600; }
    .good { color: #2980b9; font-weight: 600; }
    .average { color: #f39c12; font-weight: 600; }
    .low { color: #c0392b; font-weight: 600; }
    /* Button styling */
    .stButton>button {
        background-color: #2980b9;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #3498db;
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)


# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home - Tips", "Prediction", "What to Do"])

st.markdown('<h1 class="title">🧘‍♂️ Digital Wellbeing Analyzer</h1>', unsafe_allow_html=True)

# Home Page with Digital Wellbeing Tips
if page == "Home - Tips":
    st.header("💡 Tips for Digital Wellbeing (With Resources)")
    tips = [
        ("Limit Screen Time", "Set app time limits and take regular screen breaks.", "🌞", "World Health Organization"),
        ("Reduce Notifications", "Disable non-essential app notifications to reduce stress.", "🔕", "Harvard Business Review"),
        ("Prioritize Sleep", "Avoid screens before bedtime and aim for 7–9 hours of sleep.", "🛏️", "CDC"),
        ("Use Focus Tools", "Pomodoro timers or app blockers help maintain concentration.", "⏳", "RescueTime"),
        ("Monitor Mood & Anxiety", "Use mental health apps or journaling to track emotions.", "📝", "NAMI"),
        ("Social Media Detox", "Take regular breaks from social platforms.", "📵", "Psychology Today")
    ]

    for title, desc, emoji, source in tips:
        st.markdown(f"""
            <div class="tip-card">
            <h3>{emoji} {title}</h3>
            <p>{desc}</p>
            <small><em>Source: {source}</em></small>
            </div>
        """, unsafe_allow_html=True)

# Prediction Page
elif page == "Prediction":
    st.header("🔮 Predict Your Digital Wellbeing Score")

    # Create two columns for inputs to make form compact
    col1, col2 = st.columns(2)

    with col1:
        sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, value=7.0, step=0.1)
        num_app_switches = st.number_input("Number of App Switches", min_value=0, max_value=1000, value=100)
        social_media_time_min = st.number_input("Social Media Time (minutes)", min_value=0, max_value=1440, value=120)
        anxiety_level = st.slider("Anxiety Level (0 to 10)", 0.0, 10.0, 5.0)

    with col2:
        focus_score = st.slider("Focus Score (0 to 10)", 0.0, 10.0, 5.0)
        mood_score = st.slider("Mood Score (0 to 10)", 0.0, 10.0, 5.0)
        daily_screen_time_min = st.number_input("Daily Screen Time (minutes)", min_value=0, max_value=1440, value=300)
        notification_count = st.number_input("Notification Count", min_value=0, max_value=1000, value=100)

    if st.button(" Predict Score"):
        input_data = np.array([[sleep_hours, focus_score, mood_score, num_app_switches,
                                daily_screen_time_min, social_media_time_min,
                                notification_count, anxiety_level]])
        prediction = model.predict(input_data)[0]
        st.success(f"Your predicted Digital Wellbeing Score is: **{prediction:.2f}**")

        # Store in session state for next page use
        st.session_state["latest_score"] = prediction

        # Interpretation based on descriptive statistics with colored messages
        if prediction >= 65:
            st.markdown('<p class="excellent">🌟 Excellent Digital Wellbeing</p>', unsafe_allow_html=True)
        elif prediction >= 50:
            st.markdown('<p class="good">👍 Good Digital Wellbeing</p>', unsafe_allow_html=True)
        elif prediction >= 40:
            st.markdown('<p class="average">⚠️ Average - Some improvement needed</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="low">❗ Low - Digital wellbeing needs attention</p>', unsafe_allow_html=True)

# What to Do if Score is Low
elif page == "What to Do":
    st.header("🛠️ What to Do If Your Score Is Low")

    score = st.session_state.get("latest_score", None)

    if score is not None:
        st.write(f"Your last predicted score: **{score:.2f}**")

        if score < 40:
            st.warning("Your digital wellbeing score is low. Here’s what you can do:")
            st.markdown("""
            ### Immediate Actions:
            - Improve your **sleep schedule** 🛏️  
            - Reduce **screen time**, especially before bed ⏰  
            - Take **social media breaks** 📵  
            - Turn off **non-essential notifications** 🔕  
            - Try **breathing, journaling, or mindfulness apps** 🧘‍♂️  
            - Seek help from a **mental health counselor** 🩺  

            *Even small changes can lead to big improvements in digital wellbeing.*
            """)
        elif score < 50:
            st.info("You're in the average range. Try improving some habits like focus and screen time.")
        else:
            st.success("Your wellbeing looks good! Keep maintaining healthy digital habits.")
    else:
        st.info("You haven't made a prediction yet. Please go to the **Prediction** page")
