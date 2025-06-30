import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("calorie_predictor_model.joblib")

st.title("🧮 Calorie Burn Predictor")
st.markdown("""
This app predicts the number of calories you burn during physical activity based on your personal metrics.

💡 **How it works:**  
Enter your basic details like age, gender, weight, height, heart rate, and workout duration.  
The app will calculate your **BMI** and use a trained machine learning model to estimate your **calories burned**.

> ⚠️ This is a predictive tool and should not replace medical or fitness advice.
""")

# Gender
gender = st.radio("Gender", ["Male", "Female"])
gender_encoded = 0 if gender == "Male" else 1

# Age
age = st.number_input("Age (years)", min_value=1, max_value=100, value=25)

# Height input
height_unit = st.selectbox("Select height unit", ["Centimeters", "Feet & Inches"])
if height_unit == "Centimeters":
    height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0)
else:
    height_ft = st.number_input("Height (feet)", min_value=1, max_value=8, value=5)
    height_in = st.number_input("Additional inches", min_value=0, max_value=11, value=7)
    height_cm = round((height_ft * 30.48) + (height_in * 2.54), 2)
    st.markdown(f"📏 Height converted to: **{height_cm} cm**")

# Weight
weight = st.number_input("Weight (kg)", min_value=20.0, max_value=200.0, value=70.0)

# Duration
duration = st.number_input("Exercise Duration (minutes)", min_value=1.0, max_value=300.0, value=30.0)

# Heart Rate
heart_rate = st.number_input("Average Heart Rate (bpm)", min_value=40.0, max_value=200.0, value=110.0)
with st.expander("📖 How to measure Heart Rate (BPM)?"):
    st.markdown("""
    **To manually measure your heart rate:**
    
    1. Use your index and middle finger to locate your pulse on your **wrist** or **neck**.
    2. Count the number of beats in **15 seconds**.
    3. Multiply that number by **4** to get your **BPM**.

    **Example:** If you count 22 beats in 15 seconds → `22 x 4 = 88 BPM`

    🏃 Tip: For more accurate results during or after exercise, use a **fitness tracker** or **smartwatch** if available.
    """)


# Body Temperature
body_temp = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=45.0, value=37.0)

# BMI calculation
height_m = height_cm / 100
bmi = round(weight / (height_m ** 2), 2)
st.markdown(f"🧮 Calculated BMI: **{bmi}**")

# Prepare input
input_df = pd.DataFrame([[
    gender_encoded, age, height_cm, weight, duration, heart_rate, body_temp, bmi
]], columns=["Gender", "Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp", "BMI"])

# Predict
if st.button("Predict Calories Burned"):
    prediction = model.predict(input_df)
    st.success(f"🔥 Estimated Calories Burned: **{prediction[0]:.2f} kcal**")

